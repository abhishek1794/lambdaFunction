#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import boto3

class s3Main:
  
    ''' the class is meant to do so and so things '''
    def __init__(self, config_json):
        self.config_json = config_json
      
  ## the following method is to check the access of s3Bucket
    def s3Connection(self):
        self.service_name = config_json['service_name']
        self.aws_access_key_id = config_json['aws_access_key_id']
        self.aws_secret_access_key = config_json['aws_secret_access_key']
        self.region_name = config_json['region_name']
    
        self.s3Client = boto3.client(service_name = self.service_name,
                              aws_access_key_id = self.aws_access_key_id,
                              aws_secret_access_key = self.aws_secret_access_key,
                                  region_name = self.region_name)

    
    def s3ConnCheck(self):
        try:
            response= self.s3Client.list_buckets()
            print('Connection is Healthy')
        
        except Exception as e:
            print(e)
            
class s3Action(s3Main):
    def __init__(self, config_json):
        super().__init__(config_json)
        self.s3Connection()
        
    def get_bucket_list(self):
        response= self.s3Client.list_buckets()['Buckets']
        return response
    
    def get_bucket_policy(self, bucket_name):
        try:
            self.bucket_name = bucket_name
            self.result = self.s3Client.get_bucket_policy(Bucket=self.bucket_name)
            policy = self.result['Policy']
            return policy
        except Exception as e:
            print(e)
            
    def create_bucket_policy(self, bucket_name, policy_json):
        try:
            self.bucket_name = bucket_name
            self.policy_json = policy_json
            bucket_policy = json.dumps(self.policy_json)
            self.s3Client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
            print('Policy Created')
        except Exception as e:
            print(e)
            
    def delete_bucket_policy(self, bucket_name):
        try:
            self.bucket_name = bucket_name
            self.s3Client.delete_bucket_policy(Bucket=bucket_name)
            print('Bucket Policy Deleted')
        except Exception as e:
            print(e)

