import datetime
import os

AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY")

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

AWS_S3_CUSTOM_DOMAIN = 'd1ue9nf4jqhjr9.cloudfront.net'

DEFAULT_FILE_STORAGE = 'rejuvahome.libs.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'rejuvahome.libs.aws.utils.StaticRootS3BotoStorage'

COMPRESS_STORAGE = STATICFILES_STORAGE

AWS_STORAGE_BUCKET_NAME = 'rejuvahome'
S3DIRECT_REGION = 'ap-south-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + 'media/'
# AWS_HOST = os.environ.get("AWS_S3_HOST", "s3.amazonaws.com")
MEDIA_ROOT = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = AWS_S3_CUSTOM_DOMAIN + 'static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False

AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = [
    'image/svg+xml',
    'text/css',
    'text/javascript',
    'application/javascript',
    'application/xx-javascript',
]

AWS_S3_USE_SSL = True
