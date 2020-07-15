import psycopg2

from datetime import datetime
from sqlalchemy.exc import IntegrityError
from logging import getLogger
from werkzeug.security import generate_password_hash

from pandlol import db


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
        except IntegrityError as e:
            logger.exception("Exception {} occurred in proc find_by_email".format(e.orig.pgcode))
            return None

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "avatar": self.avatar
        }

    def save_to_db(self) -> int:
        try:
            db.session.add(self)
            db.session.commit()
            return 0
        except IntegrityError as e:
            logger.exception("Exception {} occurred in proc save_to_db".format(e.orig.pgcode))
            if e.orig.pgcode == '23505':
                return 102
            else:
                return 503

    def delete_from_db(self) -> int:
        try:
            db.session.delete(self)
            db.session.commit()
            return 0
        except IntegrityError as e:
            logger.exception("Exception {} occurred in proc delete_from_db".format(e.orig.pgcode))
            return 503
