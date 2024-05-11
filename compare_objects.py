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

        list_name_source = get_list_of_objects_name(s3_src, source_bucket_name)
        list_name_destination = get_list_of_objects_name(s3_dst, destination_bucket_name)

        set_list_name_source = set(list_name_source)
        set_list_name_destination = set(list_name_destination)

        i = list(set_list_name_source.difference(set_list_name_destination))
        i.extend(
            list(set_list_name_destination.difference(set_list_name_source)))
        print(set(i))

    except ClientError as e:
        logging.error(e)
