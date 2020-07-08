from datetime import datetime
from werkzeug.security import generate_password_hash

from pandlol import db


class UserModel(db.Model):
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password_hash = db.Column(db.String(80))
    avatar = db.Column(db.String(80))
    create_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, password, avatar):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.avatar = avatar

    def __repr__(self):
        return f'User {self.email}'

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "avatar": self.avatar
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
