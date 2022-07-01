import os

from .settings import *




# Stripe API configuration


EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = "high@trailingcoin.com"
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True