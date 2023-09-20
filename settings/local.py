from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('DEV_SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']

