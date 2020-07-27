from flask_jwt_extended import \
    (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity,
     get_raw_jwt)
from flask_restful import Resource, reqparse

from pandlol import blacklist
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

        check_user = CheckUser(user, data["confirm_password"], len(data["password"]))
        check = Check()

        if not check.validate(email=[check_user.validate_email_format, check_user.validate_email_exists],
                              password=[check_user.validate_password_format]):
            return {"status": "ERROR", "errors": check.errors}

        res = user.insert()
        res_code = 200
        if res['status'] == "INTERNAL ERROR":
            res_code = 503

        return res, res_code


class UserLogin(Resource):
    def post(self):
        data = user_parser.parse_args()
        user = UserModel.find_by_email(data["email"])

        check_user = CheckUser(user, data["password"], len(data["password"]))
        check = Check()

        if not check.validate(password=[check_user.validate_password]):
            return {"status": "ERROR", "errors": check.errors}

        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        return {"status": "OK",
                "user": {"access_token": access_token,
                         "refresh_token": refresh_token}}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user is None:
            return {"status": "ERROR",
                    "errors": {"code": 110,
                               "message": "refresh token is not valid"}}
        else:
            access_token = create_access_token(identity=current_user)

        return {"status": "OK",
                "user": {"access_token": access_token}}


class UserProfile(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user is None:
            return {"status": "ERROR",
                    "errors": {"code": 110,
                               "message": "access token is not valid"}}
        else:
            return {"status": "OK",
                    "user": {"username": current_user}}


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {"status": "OK"}
