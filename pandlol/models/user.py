from datetime import datetime
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import mongo_db


logger = getLogger(__name__)  # объект логирования


class UserModel(mongo_db.Document):
    """
    Модель пользователя
    """
    meta = {'collection': 'user_list'}

    email = mongo_db.StringField(required=True)  # Имя пользователя
    password = mongo_db.StringField(required=True)  # Захешированный пароль
    password_hashed = mongo_db.BooleanField(default=False)  # Признак хеширования пароля
    avatar = mongo_db.StringField()  # Путь к аватару
    create_date = mongo_db.DateTimeField(default=datetime.utcnow(), required=True)  # Время создания пользователя

    def clean(self):
        if not self.password_hashed:
            self.password = generate_password_hash(self.password)
            self.password_hashed = True
