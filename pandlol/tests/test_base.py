from flask_testing import TestCase

from pandlol import app

from mongoengine import connect, disconnect


class BaseCase(TestCase):
    def create_app(self):
        app.config.from_object("pandlol.default_config.TestingConfig")
        return app

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongomock://localhost')

    def tearDown(self):
        disconnect()
