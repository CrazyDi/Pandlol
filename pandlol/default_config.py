import os
import logging


# Базовые настройки приложения
class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.urandom(24)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Настройки приложения для разработки
class DevelopmentConfig(Config):
    logging.basicConfig(format=u'%(levelname)-8s - %(name)s [%(asctime)s] %(message)s', level=logging.DEBUG)
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


# Настройки для тестирования
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


# Настройки для продакшна
class ProductionConfig(Config):
    logging.basicConfig(format=u'%(levelname)-8s - %(name)s [%(asctime)s] %(message)s', level=logging.ERROR)
    PRODUCTION = True
    DEBUG = False
