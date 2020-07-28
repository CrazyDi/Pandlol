from datetime import datetime
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import db
from utils import log_database_error


logger = getLogger(__name__)  # объект логирования


class UserModel(db.Model):
    """
    Модель пользователя
    """
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)  # Идентификатор пользователя
    email = db.Column(db.String(80), unique=True)  # Имя пользователя
    password_hash = db.Column(db.String(180))  # Захешированный пароль
    avatar = db.Column(db.String(80))  # Путь к аватару
    create_date = db.Column(db.DateTime, default=datetime.utcnow())  # Время создания пользователя

    def __init__(self, email: str, password: str, avatar: str):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.avatar = avatar

    def __repr__(self):
        return f'User {self.email}'

    @classmethod
    def find_by_email(cls, email: str):
        """
        Поиск пользователя в БД по email
        """
        try:
            return cls.query.filter_by(email=email).first()
        except:
            logger.exception("Exception occurred in func find_by_email")
            return None

    def json(self):
        """
        Вывод информации о пользователе в JSON-формате
        """
        return {
            "id": self.id,
            "email": self.email,
            "avatar": self.avatar
        }

    @log_database_error(logger)
    def _save_to_db(self):
        """
        Сохранение пользователя в БД
        """
        db.session.add(self)
        db.session.commit()
        return None

    @log_database_error(logger)
    def _delete_from_db(self):
        """
        Удаление пользователя из БД
        """
        db.session.delete(self)
        db.session.commit()
        return None

    def insert(self):
        """
        Добавление нового пользователя в систему
        """
        res = self._save_to_db()
        if res is None:
            return {"status": "OK"}
        elif res == '23505':
            return {"status": "ERROR",
                    "errors":
                        {"email":
                            {"code": 102,
                             "message": "email exists"
                            }
                        }
                    }
        else:
            return {"status": "INTERNAL ERROR"}

    def update(self):
        """
        Обновление данных о пользователе в БД 
        """
        res = self._save_to_db()
        if res is None:
            return {"status": "OK"}
        else:
            return {"status": "INTERNAL ERROR"}

    def delete(self):
        """
        Удаление сведений о пользователе из БД
        """
        res = self._delete_from_db()
        if res is None:
            return {"status": "OK"}
        else:
            return {"status": "INTERNAL ERROR"}
