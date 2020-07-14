from datetime import datetime
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import db


logger = getLogger(__name__)


class UserModel(db.Model):
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
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
        return cls.query.filter_by(email=email).first()

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "avatar": self.avatar
        }

    def save_to_db(self) -> bool:
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            logger.exception("Exception occurred in proc save_to_db")
            return False

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            logger.exception("Exception occurred in proc delete_from_db")
            return False
