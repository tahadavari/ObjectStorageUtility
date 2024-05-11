import boto3
import logging
from botocore.exceptions import ClientError
import configparser

from get_list_of_bucket_object import get_list_of_objects_name

config = configparser.ConfigParser()
config.read('config.ini')
transfer_config = config['TRANSFER']
logging.basicConfig(level=logging.INFO)

try:
    # S3 resource
    s3_src = boto3.resource(
        's3',
        endpoint_url=transfer_config['SRC_ENDPOINT'],
        aws_access_key_id=transfer_config['SRC_ACCESS_KEY_ID'],
        aws_secret_access_key=transfer_config['SRC_SECRET_ACCESS_KEY']
    )
    s3_dst = boto3.resource(
        's3',
        endpoint_url=transfer_config['DST_ENDPOINT'],
        aws_access_key_id=transfer_config['DST_ACCESS_KEY_ID'],
        aws_secret_access_key=transfer_config['DST_SECRET_ACCESS_KEY']
    )

except Exception as exc:
    logging.error(exc)
else:
    try:
        source_bucket_name = transfer_config['SRC_BUCKET_NAME']
        destination_bucket_name = transfer_config['DST_BUCKET_NAME']

        source_bucket = s3_src.Bucket(source_bucket_name)
        objects = source_bucket.objects.all()

        list_name = get_list_of_objects_name(s3_dst, destination_bucket_name)

        n = 1
        for obj in objects:
            logging.info(f"START {n} : {obj.key}")
            source_key = obj.key
            destination_key: str = source_key
            if destination_key not in list_name and not destination_key.endswith('/'):
                s3_dst.meta.client.copy_object(
                    CopySource={'Bucket': source_bucket_name, 'Key': source_key},
                    Bucket=destination_bucket_name,
                    Key=destination_key,
                    ACL='public-read'
                )
            logging.info(f"END {n} : {obj.key}")
            n += 1

    except ClientError as e:
        logging.error(e)
