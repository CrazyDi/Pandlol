import unittest
import json

from pandlol.tests.test_base import BaseCase
from pandlol.models.user import UserModel


class TestUserRegistrationCase(BaseCase):
    """
    Тестирование /signup
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password,
            "confirm_password": password
        }

    def testUser_Register_Successful(self):
        """
        Тест успешной регистрации
        """
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")

    def testUser_Register_EmailEmpty(self):
        """
        Тест регистрации с пустым полем email
        """
        self.payload["email"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 100)

    def testUser_Register_EmailWrongFormat(self):
        """
        Тест регистрации с неверным форматом email
        """
        self.payload["email"] = "kate"
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 101)

    def testUser_Register_EmailExists(self):
        """
        Тест регистрации существующим логином
        """
        user = UserModel(self.payload["email"], self.payload["password"])
        user.insert()

        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 102)

    def testUser_Register_PasswordEmpty(self):
        """
        Тест регистрации с пустым полем пароля
        """
        self.payload["password"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 103)

    def testUser_Register_PasswordNotEqualConfirm(self):
        """
        Тест регистрации, когда не совпадает поле пароля и подтверждение пароля
        """
        self.payload["confirm_password"] = "222222"
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["confirm_password"]["code"], 104)

    def testUser_Register_PasswordShort(self):
        """
        Тест регистрации со слишком коротким паролем
        """
        self.payload["password"] = "1"
        self.payload["confirm_password"] = "1"
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 106)

    def testUser_Register_ConfirmPasswordEmpty(self):
        """
        Тест регистрации с пустым полем подтверждения пароля
        """
        self.payload["confirm_password"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["confirm_password"]["code"], 107)


class TestUserLoginCase(BaseCase):
    """
    Тестирование /login
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel("test1@test.com", "111111")
        user.insert()

    def testUser_Login_Successful(self):
        """
        Тест успешного логина
        """
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")
        self.assertIn("access_token", json_data["user"].keys())
        self.assertIn("refresh_token", json_data["user"].keys())

    def testUser_Login_EmailEmpty(self):
        """
        Тест логина с пустым email
        """
        self.payload["email"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 100)

    def testUser_Login_EmailWrongFormat(self):
        """
        Тест логина с неверным форматом email
        """
        self.payload["email"] = "1"
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 101)

    def testUser_Login_EmailNotExists(self):
        """
        Тест логина для несуществующего пользователя
        """
        self.payload["email"] = "test2@test.com"
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 108)

    def testUser_Login_PasswordEmpty(self):
        """
        Тест логина с пустым паролем
        """
        self.payload["password"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 103)

    def testUser_Login_PasswordWrong(self):
        """
        Тест логина с неверным паролем
        """
        self.payload["password"] = "222222"
        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 105)


class TestUserRefreshTokenCase(BaseCase):
    """
    Тестирование /refresh
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel("test1@test.com", "111111")
        user.insert()

        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.access_token = json_data["user"]["access_token"]
        self.refresh_token = json_data["user"]["refresh_token"]

    def testUser_Refresh_Successful(self):
        """
        Тест успешного обновления access_token
        """
        authorization = 'Bearer ' + self.refresh_token
        response = self.client.post('http://127.0.0.1:5000/api/refresh', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")
        self.assertIn("access_token", json_data["user"].keys())

    def testUser_Refresh_TokenWrong(self):
        """
        Тест обновления с неверным токеном
        """
        authorization = 'Bearer ' + self.refresh_token + "111"
        response = self.client.post('http://127.0.0.1:5000/api/refresh', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 422)


class TestUserLogoutCase(BaseCase):
    """
    Тестирование /logout
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel("test1@test.com", "111111")
        user.insert()

        response = self.client.post('http://127.0.0.1:5000/api/login', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.access_token = json_data["user"]["access_token"]

    def testUser_Logout_Successful(self):
        """
        Тест успешного выхода пользователя
        """
        authorization = 'Bearer ' + self.access_token
        response = self.client.post('http://127.0.0.1:5000/api/logout', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")

    def testUser_Logout_TokenWrong(self):
        """
        Тест выхода пользователя с неверным токеном
        """
        authorization = 'Bearer ' + self.access_token + "111"
        response = self.client.post('http://127.0.0.1:5000/api/logout', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 422)

    def testUser_Logout_TokenRevoked(self):
        """
        Тест выхода пользователя с токеном уже вышедшего пользователя
        """
        authorization = 'Bearer ' + self.access_token
        response = self.client.post('http://127.0.0.1:5000/api/logout', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        response = self.client.post('http://127.0.0.1:5000/api/logout', headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
