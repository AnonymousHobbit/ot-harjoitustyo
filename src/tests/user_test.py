import unittest
from modules.user_service import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.testing_user = {"username": "test", "password": "test"}
        self.testing_user_fail = {"username": "ez", "password": "ez"}

    def test_user_register_success(self):
        user = User(True)
        user.clear_table()
        registration = user.register(
            self.testing_user["username"], self.testing_user["password"])
        self.assertEqual(registration, True)
        self.assertEqual(user.find(self.testing_user["username"])[
                         1], self.testing_user["password"])

    def test_user_register_fail(self):
        user = User(True)
        user.clear_table()

        user.register(self.testing_user["username"],
                      self.testing_user["password"])

        registration = user.register(
            self.testing_user_fail["username"], self.testing_user_fail["password"])
        self.assertEqual(registration, False)

        registration = user.register(
            self.testing_user["username"], self.testing_user["password"])
        self.assertEqual(registration, False)

    def test_user_login_success(self):
        user = User(True)
        user.clear_table()
        user.register(self.testing_user["username"],
                      self.testing_user["password"])
        login = user.login(
            self.testing_user["username"], self.testing_user["password"])
        self.assertEqual(login, True)

    def test_user_login_fail(self):
        user = User(True)
        user.clear_table()

        user.register(self.testing_user["username"],
                      self.testing_user["password"])
        login = user.login(
            self.testing_user["username"], self.testing_user_fail["password"])
        self.assertEqual(login, False)

        login = user.login(
            self.testing_user_fail["username"], self.testing_user["username"])
        self.assertEqual(login, False)

    def test_get_users(self):
        user = User(True)
        user.clear_table()
        user.register(self.testing_user["username"],
                      self.testing_user["password"])
        users = user.get_users()
        self.assertEqual(len(users), 1)
