#Using GreenQloud Public APIs

###GreenQloud: Compute and Storage on demand

GreenQloud offers a compute API that can be used to create and run virtual servers to run software which is called **ComputeQloud**.
GreenQloud also offers an object/web storage service that can be used to store arbitrary files or data which is called **StorageQloud**.

###ComputeQloud

ComputeQloud is GreenQloud's compute service with an API compatible with Amazon's EC2 service. There are several command line tools that can be used to call the service. The most popular open source tool is called **euca2ools**, but GreenQloud also supports Amazon's official **ec2-api-tools**.

###StorageQloud

StorageQloud is GreenQloud's storage service with an API compatible with Amazon's S3 service. There are several command line tools that can be used to call the service. Examples of these are **s3cmd** and **s3sync**.

###Installation of client tools

###Euca2ools

Instructions to install euca2ools for GreenQloud can be found [here](http://support.greenqloud.com/entries/20020852-using-greenqloud-s-compute-api)

A User Guide of euca2ools can also be found [here](http://open.eucalyptus.com/wiki/Euca2oolsGuide_v1.3)

Once the tool is installed one can run commands such as:

	euca-describe-images
	
To list up available OS images

And to run up a virtual machine one can run a command such as:

	euca-run-instances -k default -t t1.micro qmi-9ac92558

to start up an Ubuntu 11.04 instance of size t1.micro

To get the address of this instance type:

	euca-describe-instances
	
	INSTANCE	i-xxxxx	qmi-9ac92558	i-46-149-xxx-xxx.compute.is-1.greenqloud.com		running 	default 	0 	 	t1.micro 	2012-05-23T16:53:50.000+00:00 	is-1a

And to log into this instance with ssh you have to pass in the private key used to start up the instance (in the example above the key 'default' was used):

	ssh -i [path_to_default_private_key] ubuntu@i-46-149-xxx-xxx.compute.is-1.greenqloud.com

###ec2-api-tools

Instructions for the Amazon tools can also be found [here](http://support.greenqloud.com/entries/20020852-using-greenqloud-s-compute-api). GreenQloud supports most commands of the API, and a list of supported commands can be found [here](http://support.greenqloud.com/entries/20182286-supported-commands-for-the-compute-api).

Similarly as with the euca2ools the ec2 api command to start up an instance  can be done with:

	ec2-run-instances -k default -t t1.micro qmi-9ac92558


###S3cmd

Instructions to install s3cmd for Ubuntu can be found [here](http://support.greenqloud.com/entries/20176218-using-s3cmd-and-s3fs-with-the-storage-api-ubuntu-11-04) and for CentOs [here](http://support.greenqloud.com/entries/20177662-using-s3cmd-and-s3fs-with-the-storage-api-centos-5-6)

Once the tool is installed one can run command such as:

	s3cmd ls
	
to list up buckets for the account.

To create a storage bucket with name testbucket type:

	s3cmd mb s3://testbucket
	
And to remove this bucket call:

	s3cmd rb s3://testbucket

To upload a file to the file 'testfile' to bucket 'testbucket' call:

	s3cmd put testfile s3://testbucket

For other command get the help by:

	s3cmd --help

Note that bucket names are unique globally, so no user can have the same bucket name as another.

###S3Sync

S3sync is a solution to sync folders towards an S3 compatible storage service such as StorageQloud

Instructions to set up for Linux can be found on:

[http://support.greenqloud.com/entries/20210281-using-s3sync-with-the-storage-api](http://support.greenqloud.com/entries/20210281-using-s3sync-with-the-storage-api)

Instructions to set up for Windows/.Net can be found on

[http://sprightlysoft.com/blog/?p=94](http://sprightlysoft.com/blog/?p=94)


#Raspberry Pi device

For accessing the local Raspberry Pi device with SSH it can be done with:

	ssh -p 10000 pi@i-46-149-21-114.compute.is-1.greenqloud.com
	
SSH Password is on the blackboard
	
For accessing through VNC it can be done with:

	i-46-149-21-114.compute.is-1.greenqloud.com on port 10001

VNC Password is on the blackboard
	

###Other Tools

There are other tools that may be used to call GreenQlouds APIs. 

**Boto** is a popular Python library for calling EC2/S3 services:

	https://github.com/boto/boto
	
**Sample Code** for accessing GreenQloud through python/boto can be found in the folder within this github repository (You will have to modify it by providing your API/Secret keys):

	greenqloud-boto-sample
	python greenqloud_simple_test.py
	
Within this github repository

**AWS Java SDK** is Amazons library for calling EC2/S3 that works with Greenqloud:

	http://aws.amazon.com/sdkforjava/
	
**Sample Code** for accessing GreenQloud through Java can be found in the folder within this github repository (You will have to modify it by providing your API/Secret keys):

	GreenQloud-JavaSDKGettingStarted
	ant GettingStartedApp


**Cyberduck** is a popular GUI (Mac/Windows) tool for accessing StorageQloud:

	http://cyberduck.ch/
	
Instructions for adding a GreenQloud Profile in Cyberduck can be found on [http://trac.cyberduck.ch/wiki/help/en/howto/greenqloud](http://trac.cyberduck.ch/wiki/help/en/howto/greenqloud)

**CloudBerry** is a popular Windows client to use GreenQloud's StorageQloud:

	http://www.cloudberrylab.com/

**s3fs** is a tool for mounting s3 compatible storage such as StorageQloud as a filesystem directory structure on Linux (through FUSE).

	http://code.google.com/p/s3fs/

Instructions can be found in the same articles as describing the installation of s3cmd [here](http://support.greenqloud.com/entries/20176218-using-s3cmd-and-s3fs-with-the-storage-api-ubuntu-11-04)



###Notes

Other tips and tricks can be found on GreenQlouds support site:

[http://support.greenqloud.com/](http://support.greenqloud.com/)

For more information about GreenQloud visit:

[http://www.greenqloud.com/](http://www.greenqloud.com/)


The GreenQloud team

