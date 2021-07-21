import unittest
import json

from pandlol.constant import URL_SERVER
from pandlol.tests.test_base import BaseCase
from pandlol.models.user import UserModel


class TestUserRegistrationCase(BaseCase):
    """
    /signup
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
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")

    def testUser_Register_EmailEmpty(self):
        self.payload["email"] = ""
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 100)

    def testUser_Register_EmailWrongFormat(self):
        self.payload["email"] = "kate"
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 101)

    def testUser_Register_EmailExists(self):
        user = UserModel(
            email=self.payload["email"],
            password=self.payload["password"]
        )
        user.save()

        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 102)

    def testUser_Register_PasswordEmpty(self):
        self.payload["password"] = ""
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 103)

    def testUser_Register_PasswordNotEqualConfirm(self):
        self.payload["confirm_password"] = "222222"
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["confirm_password"]["code"], 104)

    def testUser_Register_PasswordShort(self):
        self.payload["password"] = "1"
        self.payload["confirm_password"] = "1"
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 106)

    def testUser_Register_ConfirmPasswordEmpty(self):
        self.payload["confirm_password"] = ""
        response = self.client.post(
            f"{URL_SERVER}/api/signup",
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.payload)
        )
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["confirm_password"]["code"], 107)


class TestUserLoginCase(BaseCase):
    """
    /login
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel(
            email="test1@test.com",
            password="111111")
        user.save()

    def testUser_Login_Successful(self):

        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")
        self.assertIn("access_token", json_data["user"].keys())
        self.assertIn("refresh_token", json_data["user"].keys())

    def testUser_Login_EmailEmpty(self):
        self.payload["email"] = ""
        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 100)

    def testUser_Login_EmailWrongFormat(self):
        self.payload["email"] = "1"
        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 101)

    def testUser_Login_EmailNotExists(self):
        self.payload["email"] = "test2@test.com"
        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 108)

    def testUser_Login_PasswordEmpty(self):
        self.payload["password"] = ""
        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 103)

    def testUser_Login_PasswordWrong(self):
        self.payload["password"] = "222222"
        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 105)


class TestUserRefreshTokenCase(BaseCase):
    """
    /refresh
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel(
            email="test1@test.com",
            password="111111"
        )
        user.save()

        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.access_token = json_data["user"]["access_token"]
        self.refresh_token = json_data["user"]["refresh_token"]

    def testUser_Refresh_Successful(self):
        authorization = 'Bearer ' + self.refresh_token
        response = self.client.post(f"{URL_SERVER}/api/refresh",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")
        self.assertIn("access_token", json_data["user"].keys())

    def testUser_Refresh_TokenWrong(self):
        authorization = 'Bearer ' + self.refresh_token + "111"
        response = self.client.post(f"{URL_SERVER}/api/refresh",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 422)


class TestUserLogoutCase(BaseCase):
    """
    /logout
    """
    def setUp(self):
        super().setUp()
        email = "test1@test.com"
        password = "111111"
        self.payload = {
            "email": email,
            "password": password
        }
        user = UserModel(
            email="test1@test.com",
            password="111111"
        )
        user.save()

        response = self.client.post(f"{URL_SERVER}/api/login",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.access_token = json_data["user"]["access_token"]

    def testUser_Logout_Successful(self):
        authorization = 'Bearer ' + self.access_token
        response = self.client.post(f"{URL_SERVER}/api/logout",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")

    def testUser_Logout_TokenWrong(self):
        authorization = 'Bearer ' + self.access_token + "111"
        response = self.client.post(f"{URL_SERVER}/api/logout",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 422)

    def testUser_Logout_TokenRevoked(self):
        authorization = 'Bearer ' + self.access_token
        response = self.client.post(f"{URL_SERVER}/api/logout",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        response = self.client.post(f"{URL_SERVER}/api/logout",
                                    headers={"Authorization": authorization},
                                    data=json.dumps(self.payload))
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
