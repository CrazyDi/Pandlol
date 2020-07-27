from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


app = Flask(__name__, template_folder='../www/public', static_folder='../www/public/assets')
load_dotenv("pandlol/.env", verbose=True)
app.config.from_object("pandlol.default_config.DevelopmentConfig")


db = SQLAlchemy(app)
api = Api(app)

jwt = JWTManager(app)
blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


from pandlol.resources.user import UserRegister, UserLogin, TokenRefresh, UserLogout, UserProfile


api.add_resource(UserRegister, '/api/signup')
api.add_resource(UserLogin, '/api/login')
api.add_resource(TokenRefresh, '/api/refresh')
api.add_resource(UserLogout, '/api/logout')
api.add_resource(UserProfile, '/api/profile')


@app.route('/')
def home():
    return render_template('index.html')
