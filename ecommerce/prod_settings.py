import os

from .settings import *




# Stripe API configuration
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True