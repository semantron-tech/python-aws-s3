import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIASGVV2WXEBERRFBFN'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'pythons3sample'

data = open('test.txt', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='test.txt', Body=data)

print ("Done")
