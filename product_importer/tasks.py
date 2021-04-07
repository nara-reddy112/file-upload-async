import boto3
import csv
from celery.decorators import task

from product_importer.bulk_create_manager import BulkCreateManager
from product_importer.models import Product


def get_s3_object_key_from_url(url):
    """
    Return S3 Object key from resource url
    """
    return url.split('/')[-1]


def load_file(url):
    """
    Load file to /tmp and return file location
    """
    key = get_s3_object_key_from_url(url)
    file_location = '/tmp/{}'.format(key)
    s3 = boto3.client('s3', region_name='ap-south-1')
    s3.download_file('fulfilio-product-importer', key, file_location)
    return file_location

@task()
def import_data(url):
    """
    Open and read from file
    Import data from file with BulkCreateManager
    """
    file = load_file(url)

    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        bulk_mgr = BulkCreateManager(chunk_size=1000)
        for row in reader:
            print(row)
            bulk_mgr.add(Product(sku=row[1], name=row[0], description=row[2]))
            print("Woohoo")
        bulk_mgr.done()