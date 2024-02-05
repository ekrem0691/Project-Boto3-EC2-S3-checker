'''
Required imports 
    - boto3 for AWS
    - json for all JSON processing
    - datetime to 

'''

import boto3
import json
from datetime import datetime


'''
    Define the ec2 and s3 boto3 clint which we can use as needed.
'''

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')


'''
    Define the tag-key values which will determine the instance needs to be stopped and/or started.
    If instance doesnt have these tags, the scheduler will ignore the instance.
'''

label_start_time = "SchedulerStartTime"
label_stop_time = "SchedulerStartTime"







































def lambda_handler(event, context):
    
    
    
if __name__ == "__main__":
    lambda_handler(None,None)