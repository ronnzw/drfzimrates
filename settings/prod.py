from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('PROD_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST')]


#Put Database here when available