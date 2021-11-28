from logging import Filter
import boto3
import json
from boto3.session import Session

Get = boto3.Session(region_name='us-west-2',profile_name='atul')
s3 = Get.client('ec2')
instances = s3.describe_instances(Filters=[{'Name':'tag:Name', 'Values': ['Test']}])
for i in range(len(instances['Reservations'])):
        print(i)
        print(instances['Reservations'][i]['Instances'][0]['InstanceId'])
