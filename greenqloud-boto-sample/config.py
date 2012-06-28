#!/usr/bin/python
# -*- coding: utf-8 -
import os
import sys
import ConfigParser

p = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
c = ConfigParser.ConfigParser()
c.read(p('settings.cfg'))

s3_uri = c.get('S3', 'uri')
s3_public_key = c.get('S3', 'public_key')
s3_private_key = c.get('S3', 'private_key')
s3_is_secure = c.getboolean('S3', 'is_secure')

ec2_uri = c.get('EC2', 'URI')
ec2_path = c.get('EC2', 'path')
ec2_port = c.getint('EC2', 'PORT')
ec2_is_secure = c.getboolean('EC2', 'secure')
ec2_public_key = c.get('EC2', 'public_key')
ec2_private_key = c.get('EC2', 'private_key')
ec2_region = c.get('EC2', 'region')
ec2_zone = c.get('EC2', 'zone')
ec2_test_image_id = c.get('EC2', 'test_image_id')
ec2_test_image_user = c.get('EC2', 'test_image_user')
ec2_use_ipv6 = c.getboolean('EC2', 'use_ipv6')
