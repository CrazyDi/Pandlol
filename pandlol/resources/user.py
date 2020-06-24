from flask_restful import Resource, reqparse

from pandlol.models.user import UserModel
from pandlol.validation.check import Check
from pandlol.validation.user import CheckUser

user_parser = reqparse.RequestParser()
user_parser.add_argument("email", type=str)
user_parser.add_argument("password", type=str)
user_parser.add_argument("confirm_password", type=str)
user_parser.add_argument("avatar", type=str)


class UserRegister(Resource):
    def post(self):
        data = user_parser.parse_args()
        user = UserModel(data["email"], data["password"], data["avatar"])

        check_user = CheckUser(user, data["confirm_password"])
        check = Check()

        if not check.validate(email=[check_user.validate_email_format, check_user.validate_email_exists],
                              password=[check_user.validate_password_format]):
            return {"status": "ERROR", "errors": check.errors}

        return {"status": "OK"}
