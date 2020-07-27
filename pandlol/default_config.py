import os
import logging


class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.urandom(24)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    logging.basicConfig(format = u'%(levelname)-8s - %(name)s [%(asctime)s] %(message)s', level=logging.DEBUG)
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    logging.basicConfig(format=u'%(levelname)-8s - %(name)s [%(asctime)s] %(message)s', level=logging.ERROR,
                        filename=u'pandlol.log')
    PRODUCTION = True
    DEBUG = False
