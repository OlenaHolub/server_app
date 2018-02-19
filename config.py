class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'SECRET_KEY_APP'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    BUNDLE_ERRORS = True
