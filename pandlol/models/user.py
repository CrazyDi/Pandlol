from datetime import datetime
from pandlol import db


class UserModel(db.Model):
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    avatar = db.Column(db.String(80))
    create_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, password, avatar):
        self.email = email
        self.password = password
        self.avatar = avatar

    def __repr__(self):
        return f'User {self.email}'

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
