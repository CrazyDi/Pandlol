import os
import logging
from datetime import timedelta
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# Базовые настройки приложения
class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.urandom(24)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    PROPAGATE_EXCEPTIONS = True
    MONGO_URI = os.environ.get('MONGO_URI')
    MONGODB_SETTINGS = {
        'db': 'pandlol',
        'host': os.environ.get('MONGO_HOST'),
        'port': int(os.environ.get('MONGO_PORT'))
    }
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
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
    PRESERVE_CONTEXT_ON_EXCEPTION = False


# Настройки для продакшна
class ProductionConfig(Config):
    logging.basicConfig(format=u'%(levelname)-8s - %(name)s [%(asctime)s] %(message)s', level=logging.ERROR)
    PRODUCTION = True
    DEBUG = False
