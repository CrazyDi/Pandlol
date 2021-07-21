from datetime import datetime
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import mongo_engine


logger = getLogger(__name__)  # log object


class UserModel(mongo_engine.Document):
    """
    User model
    """
    meta = {'collection': 'user_list'}

    email = mongo_engine.StringField(required=True)  # Username
    password = mongo_engine.StringField(required=True)  # hashed password
    password_hashed = mongo_engine.BooleanField(default=False)  # sign of password hash
    avatar = mongo_engine.StringField()  # Путь к аватару
    create_date = mongo_engine.DateTimeField(default=datetime.utcnow(), required=True)  # create time of user

    def clean(self):
        if not self.password_hashed:
            self.password = generate_password_hash(self.password)
            self.password_hashed = True
