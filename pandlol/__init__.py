from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_swagger import swagger


# Application with settings
app = Flask(__name__, template_folder='../www/public', static_folder='../www/public/assets')
# Read URI БД DATABASE_URL=
load_dotenv("pandlol/.env", verbose=True)
# Load configuration
app.config.from_object("pandlol.default_config.DevelopmentConfig")

# Connect to DB
# db = SQLAlchemy(app)
mongo_engine = MongoEngine(app)
mongo_db = PyMongo(app)

# Object API
api = Api(app)

# Object JWT authorization
jwt = JWTManager(app)

# Blacklist for user logout
blacklist = set()


# Check token in blacklist for user logout
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist


# Endpoint for user
from pandlol.resources.user import UserRegister, UserLogin, TokenRefresh, UserLogout, UserProfile

api.add_resource(UserRegister, '/api/signup')
api.add_resource(UserLogin, '/api/login')
api.add_resource(TokenRefresh, '/api/refresh')
api.add_resource(UserLogout, '/api/logout')
api.add_resource(UserProfile, '/api/profile')


# Endpoint for champion_list
from pandlol.resources.champion_list import ChampionList, ChampionEventSkill

api.add_resource(ChampionList, '/api/champions')
api.add_resource(ChampionEventSkill, '/api/skills')


# homepage
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/spec")
def spec():
    return jsonify(swagger(app))
