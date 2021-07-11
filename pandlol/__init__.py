from dotenv import load_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_restful import Api


# Приложение с настройками
app = Flask(__name__, template_folder='../www/public', static_folder='../www/public/assets')
# Считываем URI БД DATABASE_URL=
load_dotenv("pandlol/.env", verbose=True)
# Загружаем конфигурацию
app.config.from_object("pandlol.default_config.DevelopmentConfig")

# Объект коннекта к БД
# db = SQLAlchemy(app)
mongo_engine = MongoEngine(app)
mongo_db = PyMongo(app)


# Объект API
api = Api(app)

# Объект JWT авторизации
jwt = JWTManager(app)

# Черный список для выхода пользователя
blacklist = set()


# Проверка токена в черном списке для выхода пользователя
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist


# Загрузка endpoint для пользователя
from pandlol.resources.user import UserRegister, UserLogin, TokenRefresh, UserLogout, UserProfile

api.add_resource(UserRegister, '/api/signup')  # регистрация пользователя
api.add_resource(UserLogin, '/api/login')  # вход пользователя
api.add_resource(TokenRefresh, '/api/refresh')  # обновление access token
api.add_resource(UserLogout, '/api/logout')  # выход пользователя
api.add_resource(UserProfile, '/api/profile')  # профиль пользователя (скорее для проверки)


# Загрузка edpoint для списка чемпионов
from pandlol.resources.champion_list import ChampionList, ChampionEventSkill

api.add_resource(ChampionList, '/api/champions')  # запрос на список чемпионов
api.add_resource(ChampionEventSkill, '/api/skills')

# домашняя страница
@app.route('/')
def home():
    return render_template('index.html')
