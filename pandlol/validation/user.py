import re
from typing import Dict
from werkzeug.security import check_password_hash

from pandlol.models.user import UserModel


class CheckUser:
    """
    Проверка данных пользоавтеля
    """
    def __init__(self, email, password, confirm_password=""):
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_email_format(self) -> Dict:
        """
        Проверка формата введенного email
        """
        if len(self.email) == 0:
            return {"code": 100,
                    "message": "email is empty"}

        email_regex = re.compile("[^@]+@[^@]+\.[^@]+")
        if not email_regex.fullmatch(self.email):
            return {"code": 101,
                    "message": "wrong email format"}

        return {}

    def validate_email_exists(self) -> Dict:
        """
        Проверка существования такого пользователя в БД
        """
        if UserModel.find_by_email(self.email):
            return {"code": 102,
                    "message": "email exists"}
        return {}

    def validate_password_format(self) -> Dict:
        """
        Проверка формата введенного пароля
        """
        if len(self.password) == 0:
            return {"code": 103,
                    "message": "password is empty"}

        if len(self.password) < 6:
            return {"code": 106,
                    "message": "password length couldn't be less than 6"}

        return {}

    def validate_confirm_password(self) -> Dict:
        """
        Проверка подтверждения пароля
        """
        if not self.confirm_password:
            return {"code": 107,
                    "message": "confirm password is empty"}

        if self.password != self.confirm_password:
            return {"code": 104,
                    "message": "password and confirm password are not equal"}

        return {}

    def validate_password(self) -> Dict:
        """
        Проверка пароля пользователя
        """
        if len(self.password) == 0:
            return {"code": 103,
                    "message": "password is empty"}

        user = UserModel.find_by_email(self.email)

        if user:
            if not check_password_hash(user.password_hash, self.password):
                return {"code": 105,
                        "message": "wrong password"}

        return {}

    def validate_email_not_exists(self) -> Dict:
        """
        Проверка существования такого пользователя в БД
        """
        if not UserModel.find_by_email(self.email):
            return {"code": 108,
                    "message": "email doesn't exist"}
        return {}