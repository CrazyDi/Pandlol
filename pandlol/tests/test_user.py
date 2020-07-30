import unittest
import json

from pandlol.tests.test_base import BaseCase


class TestUserCase(BaseCase):
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

    def testUser_Register_EmptyEmail(self):
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

    def testUser_Register_WrongEmailFormat(self):
        """
        Тест регистрации с пустым полем email
        """
        self.payload["email"] = "kate"
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["email"]["code"], 101)

    def testUser_Register_EmptyPassword(self):
        """
        Тест регистрации с пустым полем email
        """
        self.payload["password"] = ""
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.payload))
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "ERROR")
        self.assertEqual(json_data["errors"]["password"]["code"], 103)


if __name__ == '__main__':
    unittest.main()
