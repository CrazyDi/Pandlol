from flask_jwt_extended import \
    (create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
     get_jwt)
from flask_restful import Resource, reqparse

from pandlol import blacklist
from pandlol.models.user import UserModel
from pandlol.validation.check import Check
from pandlol.validation.user import CheckUser


user_parser = reqparse.RequestParser()
user_parser.add_argument("email", default="", type=str)
user_parser.add_argument("password", default="", type=str)
user_parser.add_argument("confirm_password", default="", type=str)
user_parser.add_argument("avatar", type=str)


class UserRegister(Resource):
    """
    User registration
    """
    def post(self):
        # parameters
        data = user_parser.parse_args()

        # validation
        check_user = CheckUser(data["email"], data["password"], data["confirm_password"])
        check = Check()

        if not check.validate(
                email=[check_user.validate_email_format, check_user.validate_email_exists],
                password=[check_user.validate_password_format],
                confirm_password=[check_user.validate_confirm_password]):
            return {"status": "ERROR", "errors": check.errors}

        # if validation is true - create object of user
        user = UserModel(
            email=data["email"],
            password=data["password"],
            avatar=data["avatar"]
        )

        # add user to data
        user.save()
        res_code = 200

        return {"status": "OK"}, res_code


class UserLogin(Resource):
    """
    Login
    """
    def post(self):
        # parameters
        data = user_parser.parse_args()

        # validation
        check_user = CheckUser(data["email"], data["password"], data["confirm_password"])
        check = Check()

        # check exist
        if not check.validate(email=[check_user.validate_email_format, check_user.validate_email_not_exists]):
            return {"status": "ERROR", "errors": check.errors}

        # check password
        if not check.validate(password=[check_user.validate_password]):
            return {"status": "ERROR", "errors": check.errors}

        # create tokens
        access_token = create_access_token(identity=data["email"])
        refresh_token = create_refresh_token(identity=data["email"])

        return {"status": "OK",
                "user": {"access_token": access_token,
                         "refresh_token": refresh_token}}


class TokenRefresh(Resource):
    """
    Refresh access token for user. Requires refresh token
    """
    @jwt_required(refresh=True)
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
    """
    View data of user. Now return only username
    Requires access token
    """
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
    """
    User logout. Requires access token
    """
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        blacklist.add(jti)
        return {"status": "OK"}
