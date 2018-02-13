import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
