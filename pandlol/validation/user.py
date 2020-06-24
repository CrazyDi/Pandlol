import re
from typing import Dict

from pandlol.models.user import UserModel


class CheckUser:
    def __init__(self, user: UserModel, confirm_password: str):
        self.user = user
        self.confirm_password = confirm_password

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
        # if UserModel.find_by_email(self.user.email):
        #     return {"code": 102,
        #             "message": "email exists"}
        return {}

    def validate_password_format(self) -> Dict:
        if len(self.user.password) == 0:
            return {"code": 103,
                    "message": "password is empty"}

        if self.user.password != self.confirm_password:
            return {"code": 104,
                    "message": "password and confirm password are not equal"}

        return {}
