import unittest
import json

from pandlol.tests.test_base import BaseCase


class TestUserCase(BaseCase):
    def test_user_register_successful(self):
        email = "test1@test.com"
        password = "111111"
        payload = json.dumps({
            "email": email,
            "password": password,
            "confirm_password": password
        })
        response = self.client.post('http://127.0.0.1:5000/api/signup', headers={"Content-Type": "application/json"}, data=payload)
        json_data = response.get_json()
        self.assert200(response)
        self.assertEqual(json_data["status"], "OK")


if __name__ == '__main__':
    unittest.main()
