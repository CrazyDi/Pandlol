from flask_jwt_extended import \
    (create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
     get_jwt)
from flask_restful import Resource, reqparse

from pandlol import blacklist
from pandlol.models.user import UserModel
from pandlol.validation.check import Check
from pandlol.validation.user import CheckUser

# Парсер данных пользователя
user_parser = reqparse.RequestParser()
user_parser.add_argument("email", default="", type=str)
user_parser.add_argument("password", default="", type=str)
user_parser.add_argument("confirm_password", default="", type=str)
user_parser.add_argument("avatar", type=str)


class UserRegister(Resource):
    """
    Регистрация пользователя
    """
    def post(self):
        # собираем данные параметров
        data = user_parser.parse_args()

        # валидация
        check_user = CheckUser(data["email"], data["password"], data["confirm_password"])
        check = Check()

        if not check.validate(
                email=[check_user.validate_email_format, check_user.validate_email_exists],
                password=[check_user.validate_password_format],
                confirm_password=[check_user.validate_confirm_password]):
            return {"status": "ERROR", "errors": check.errors}

        # если прошли валидацию - создаем объект пользователя
        user = UserModel(
            email=data["email"],
            password=data["password"],
            avatar=data["avatar"]
        )

        # добавляем пользователя в базу
        user.save()
        res_code = 200

        return {"status": "OK"}, res_code


class UserLogin(Resource):
    """
    Вход пользователя
    """
    def post(self):
        # собираем данные из параметров
        data = user_parser.parse_args()

        # валидация
        check_user = CheckUser(data["email"], data["password"], data["confirm_password"])
        check = Check()

        # проверяем, есть ли такой пользователей
        if not check.validate(email=[check_user.validate_email_format, check_user.validate_email_not_exists]):
            return {"status": "ERROR", "errors": check.errors}

        # если пользователь есть, проверяем пароль
        if not check.validate(password=[check_user.validate_password]):
            return {"status": "ERROR", "errors": check.errors}

        # если прошла валидация, создаем токены
        access_token = create_access_token(identity=data["email"])
        refresh_token = create_refresh_token(identity=data["email"])

        return {"status": "OK",
                "user": {"access_token": access_token,
                         "refresh_token": refresh_token}}


class TokenRefresh(Resource):
    """
    Обновление access token для пользоателя. Требует refresh token
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
    Просмотр данных о пользователе. Пока что возвращает только имя пользователя.
    Требует access token
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
    Выход пользователя. Требует access token
    """
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        blacklist.add(jti)
        return {"status": "OK"}
