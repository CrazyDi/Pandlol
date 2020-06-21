from flask_restful import Resource, reqparse

from pandlol.models.user import UserModel

user_parser = reqparse.RequestParser()
user_parser.add_argument("email", type=str)
user_parser.add_argument("password", type=str)
user_parser.add_argument("avatar", type=str)


class UserRegister(Resource):
    def post(self):
        data = user_parser.parse_args()
        user = UserModel(**data)

        if UserModel.find_by_email(user.email):
            return {"status": "ERROR",
                    "errors":
                        {"email":
                             {"code": 101,
                              "message": "email exists"}
                         }
                    }
