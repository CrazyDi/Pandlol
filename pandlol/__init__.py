from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


app = Flask(__name__, template_folder='../www/public', static_folder='../www/public/assets')
load_dotenv("pandlol/.env", verbose=True)
app.config.from_object("pandlol.default_config.DevelopmentConfig")


db = SQLAlchemy(app)


api = Api(app)


from pandlol.resources.user import UserRegister


api.add_resource(UserRegister, '/api/signup')


@app.route('/')
def home():
    return render_template('index.html')
