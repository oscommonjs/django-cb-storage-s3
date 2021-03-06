import os
import sys


DEBUG = True
if sys.platform[0:3] == 'win':
    TEMP = os.environ.get('TEMP', '')
else:
    TEMP = '/tmp'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memoery:'
    }
}
INSTALLED_APPS = [
    'cuddlybuddly.storage.s3'
]
STATIC_ROOT = MEDIA_ROOT = os.path.join(TEMP, 'cbs3test')
SECRET_KEY = 'placeholder'

DEFAULT_FILE_STORAGE = 'cuddlybuddly.storage.s3.S3Storage'
from cuddlybuddly.storage.s3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# Below should contain:
#
# MEDIA_URL = 'http://yourbucket.s3.amazonaws.com/'
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = ''
from cuddlybuddly.storage.s3.tests3credentials import *

CUDDLYBUDDLY_STORAGE_S3_CACHE = 'cuddlybuddly.storage.s3.cache.FileSystemCache'
CUDDLYBUDDLY_STORAGE_S3_FILE_CACHE_DIR = TEMP+'/cbs3testcache'
