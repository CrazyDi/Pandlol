from datetime import datetime
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import db
from utils import log_database_error


logger = getLogger(__name__)


class UserModel(db.Model):
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(180))
    avatar = db.Column(db.String(80))
    create_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email: str, password: str, avatar: str):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.avatar = avatar

    def __repr__(self):
        return f'User {self.email}'

    @classmethod
    def find_by_email(cls, email: str):
        try:
            return cls.query.filter_by(email=email).first()
        except:
            logger.exception("Exception occurred in func find_by_email")
            return None

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "avatar": self.avatar
        }

    @log_database_error(logger)
    def _save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return None

    @log_database_error(logger)
    def _delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        return None

    def insert(self):
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
        res = self._save_to_db()
        if res is None:
            return {"status": "OK"}
        else:
            return {"status": "INTERNAL ERROR"}

    def delete(self):
        res = self._delete_from_db()
        if res is None:
            return {"status": "OK"}
        else:
            return {"status": "INTERNAL ERROR"}
