from .settings import *

DEBUG = False

SESSION_COOKIE_AGE = 72000
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = "high@trailingcoin.com"
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True