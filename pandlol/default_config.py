import os


class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False
