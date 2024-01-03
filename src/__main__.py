import os
import json
import pulumi
from pulumi_aws import s3

config = pulumi.Config()
bucket_list = config.get("bucket_path")

with open(bucket_list) as bucket_data:
    buckets = json.load(bucket_data)

for bucket in buckets:
    s3.Bucket(bucket)
