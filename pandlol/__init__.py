from dotenv import load_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Приложение с настройками
app = Flask(__name__, template_folder='../www/public', static_folder='../www/public/assets')
# Считываем URI БД DATABASE_URL=
load_dotenv("pandlol/.env", verbose=True)
# Загружаем конфигурацию
app.config.from_object("pandlol.default_config.ProductionConfig")

# Объект коннекта к БД
db = SQLAlchemy(app)

# Объект API
api = Api(app)

# Объект JWT авторизации
jwt = JWTManager(app)
# Черный список для выхода пользователя
blacklist = set()


# Проверка токена в черном списке для выхода пользователя
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


# Загрузка endpoint для пользователя
from pandlol.resources.user import UserRegister, UserLogin, TokenRefresh, UserLogout, UserProfile


api.add_resource(UserRegister, '/api/signup')  # регистрация пользователя
api.add_resource(UserLogin, '/api/login')  # вход пользователя
api.add_resource(TokenRefresh, '/api/refresh')  # обновление access token
api.add_resource(UserLogout, '/api/logout')  # выход пользователя
api.add_resource(UserProfile, '/api/profile')  # профиль пользователя (скорее для проверки)


# домашняя страница
@app.route('/')
def home():
    return render_template('index.html')
