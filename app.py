from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv

app = Flask(__name__, template_folder='www/public', static_folder='www/public/assets')
load_dotenv(".env", verbose=True)
# app.config.from_object("default_config")
# app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
