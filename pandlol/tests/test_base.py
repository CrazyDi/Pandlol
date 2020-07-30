from flask_testing import TestCase

from pandlol import app, db


class BaseCase(TestCase):
    def create_app(self):
        app.config.from_object("pandlol.default_config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
