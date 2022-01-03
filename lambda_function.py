#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import boto3
import logging 

from Request import s3Main



def lambda_handler(event, context):
    # TODO implement
    config_json = {'service_name':'s3','aws_access_key_id':"AKIA26MMEZXEIHDDPXUV",'aws_secret_access_key':"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",'region_name':"ap-south-1"} 
    # s_event = s3Main(config_json)
    s1 = s3Main(config_json)
    return s1
    
    s1.s3Connection()
    s1.s3ConnCheck()

    s2 = Request.s3Action(config_json)
    
    s2.delete_bucket_policy(bucket_name = 'appsummarizer')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
   

    

