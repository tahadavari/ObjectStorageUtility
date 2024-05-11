import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_list_of_bucket_object(s3_resource, bucket_name):
    list_of_objects = []
    try:
        bucket = s3_resource.Bucket(bucket_name)
        n = 0
        for obj in bucket.objects.all():
            logging.info(f"object_name: {obj.key}, last_modified: {obj.last_modified}")
            list_of_objects.append(obj)
            n += 1
        logging.info(f"count of object: {n}")
    except ClientError as e:
        logging.error(e)
    finally:
        return list_of_objects


def get_list_of_objects_name(s3_resource, bucket_name):
    list_of_objects = get_list_of_bucket_object(s3_resource, bucket_name)
    list_of_objects_name = []
    for obj in list_of_objects:
        list_of_objects_name.append(obj.key)
    return list_of_objects_name


if __name__ == "__main__":
    s3_src = boto3.resource(
        's3',
        endpoint_url='',
        aws_access_key_id='',
        aws_secret_access_key=''
    )
    bucket_name = ''
    list_of_objects_name = get_list_of_objects_name(s3_src, bucket_name)
