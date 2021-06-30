import unittest

from flask_testing import TestCase

from pandlol.constant import URL_SERVER
from pandlol import app


class TestAPIChampions(TestCase):
    def create_app(self):
        app.config.from_object("pandlol.default_config.TestingConfig")
        return app

    def testAPI_Champions_OK(self):
        response = self.client.get(f"{URL_SERVER}/api/champions?patch=11.10&queue=420,440&page=2,2")
        self.assertEqual(response.status_code, 200)

    def testAPI_Champions_WrongPage(self):
        response = self.client.get(f"{URL_SERVER}/api/champions?patch=11.10&queue=420,440&page=22")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json, dict(status="INTERNAL ERROR", error="wrong page param"))

    def testAPI_Champions_WrongOrder(self):
        response = self.client.get(f"{URL_SERVER}/api/champions?patch=11.10&queue=420,440&order=22")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json, dict(status="INTERNAL ERROR", error="wrong order param"))


if __name__ == '__main__':
    unittest.main()
