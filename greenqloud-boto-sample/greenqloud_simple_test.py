#!/usr/bin/python
'''
supported instance operations
DescribeInstances -
RunInstances -
RebootInstances -
StartInstances -
StopInstances -
TerminateInstances -
'''
from _socket import socket
from boto.ec2.regioninfo import RegionInfo
from boto.ec2.connection import EC2Connection

import socket
import commands 
import os
import sys
#import base
import random
#import paramiko
from time import time,sleep


#sys.path.append('/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1]))

from config import *

class GreenQloudSimpleTest:


    def create_connection(self, pub_key=ec2_public_key, pri_key=ec2_private_key):
        """
        Returns a boto ec2 connection for the current environment.
        """
        region = RegionInfo(name=ec2_region, endpoint=ec2_uri)
        return EC2Connection(aws_access_key_id=pub_key,
                                aws_secret_access_key=pri_key,
                                is_secure=ec2_is_secure,
                                host=ec2_uri,
                                path=ec2_path,
                                port=ec2_port,
                                region=region)

    def setUp(self):
        self.conn = self.create_connection(pub_key=ec2_public_key,
                                           pri_key=ec2_private_key)

    def tearDown(self):
        pass


    def test_000_describe_images(self):
        print "test_001_describe_images"
        print self.conn.get_all_images()


    def test_001_describe_instances(self):
        print self.conn.get_all_instances()

    def test_002_can_create_keypair(self):
        print TEST_KEY
        key = self.create_key_pair(self.conn, TEST_KEY)
        self.assertEqual(key.name, TEST_KEY)

    def test_003_create_instance(self):
        # Run Instance
        self.data['instance_start_time'] = time()
        reservation = self.conn.run_instances(ec2_test_image_id,key_name=TEST_KEY,instance_type='t1.nano')
        print "reservation: ",reservation, "instance: ", reservation.instances[0]
        self.assertEqual(len(reservation.instances), 1)
        self.data['instance_id'] = reservation.instances[0].id

    def test_004_instance_runs_within_480_seconds(self):
        reservations = self.conn.get_all_instances([self.data['instance_id']])
        instance = reservations[0].instances[0]
        t1 = time()
        started = self.wait_for_running(instance,tries=48, wait=10)
        self.assertTrue(started, "Instance failed to start within 240 seconds ("
                                 +str(time()-t1) + ")")
        self.report_to_db('instance_startup_time', value=time()-t1,
                          message="instance id: %s" % self.data['instance_id'], userid=TEST_USER, instance=self.data['instance_id'])

    def test_005_ip_allocated(self):
        reservations = self.conn.get_all_instances([self.data['instance_id']])
        i = reservations[0].instances[0]
        print("instance network: ", i.public_dns_name, i.private_dns_name,
              i.ip_address, i.private_ip_address)
        ip = i.ip_address
        self.failIf(ip == '0.0.0.0')
        self.data['ip'] = ip

    def test_006_can_ssh(self):
        self.data['SSH_FAIL'] = False
        for x in xrange(15):
            try:
                print("SSH to ",self.data['ip']," with key: ",TEST_KEY)
                conn = self.connect_ssh(self.data['ip'], TEST_KEY)
                sshtime = time() - self.data['instance_start_time']
                self.report_to_db('start_to_ssh', value=sshtime, userid=TEST_USER, instance=self.data['instance_id'])
                conn.close()
            except socket.error as (errno, strerror):
                print "socket.error error({0}): {1}".format(errno, strerror)
                sleep(10)
            except paramiko.AuthenticationException as e:
                #todo remove this print debug
                print "Authentication error: " , e
                sleep(10)
            else:
                break
        else:
            self.report_to_db("unable to ssh to instance", success=False,
                           message="instance id:%s" % self.data['instance_id'],
                           userid=TEST_USER, instance=self.data['instance_id'])
            self.data['SSH_FAIL'] = True
            self.send_alarm_email(TEST_KEY, TEST_GROUP, TEST_USER)
            self.fail('could not ssh to instance')

    def test_099_can_terminate_instance(self):
        if self.data['SSH_FAIL'] == True:
            print "SSH fail, not doing anything"
            return
        if self.data.has_key('instance_id'):
            self.conn.terminate_instances([self.data['instance_id']])
        self.delete_key_pair(self.conn, TEST_KEY)


    def do_not_t3st_999_cleanup(self):
        try:
            reservations = self.conn.get_all_instances()
            instances = [i for r in reservations for i in r.instances]
            for ins in instances:
                print(ins.id)
                self.conn.terminate_instances(ins.id)
        except:
            print("unable to destroy all running instances, carring on:", sys.exc_info()[0])

if __name__ == '__main__':
    test = GreenQloudSimpleTest()
    test.setUp()
    test.test_000_describe_images()
