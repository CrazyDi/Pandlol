import re
from typing import Dict
from werkzeug.security import check_password_hash

from pandlol.models.user import UserModel


class CheckUser:
    def __init__(self, user: UserModel, confirm_password: str, password_len: int):
        self.user = user
        self.confirm_password = confirm_password
        self.password_len = password_len

    def validate_email_format(self) -> Dict:
        if len(self.user.email) == 0:
            return {"code": 100,
                    "message": "email is empty"}

        email_regex = re.compile("[^@]+@[^@]+\.[^@]+")
        if not email_regex.fullmatch(self.user.email):
            return {"code": 101,
                    "message": "wrong email format"}

        return {}

    def validate_email_exists(self) -> Dict:
        if UserModel.find_by_email(self.user.email):
            return {"code": 102,
                    "message": "email exists"}
        return {}

    def validate_password_format(self) -> Dict:
        if len(self.user.password_hash) == 0:
            return {"code": 103,
                    "message": "password is empty"}

        if self.password_len < 6:
            return {"code": 106,
                    "message": "password length couldn't be less than 6"}

        if not check_password_hash(self.user.password_hash, self.confirm_password):
            return {"code": 104,
                    "message": "password and confirm password are not equal"}

        return {}

    def validate_password(self) -> Dict:
        if len(self.user.password_hash) == 0:
            return {"code": 103,
                    "message": "password is empty"}

        if not check_password_hash(self.user.password_hash, self.confirm_password):
            return {"code": 105,
                    "message": "wrong password"}

        return {}