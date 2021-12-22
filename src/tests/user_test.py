import unittest
from modules.user_service import UserService, UsernameExistsError, ShortCredentialsError, IncorrectCredentialsError, InvalidJoinKeyError
from modules.org_service import OrgService
from models.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("user", "passwd")
        self.fail_user = User("ez", "ez")
        self.user_service = UserService(True)
        self.org_service = OrgService(True)

    def test_user_register_success(self):
        self.user_service.clear_table()  # Clear database before testing

        # Register a test user
        self.user_service.register(
            self.user.username, self.user.password)
        # Find the added user
        user = self.user_service.find(self.user.username)

        self.assertEqual(user[
                         1], self.user.username)

    def test_user_register_fail(self):
        self.user_service.clear_table()  # Clear database before testing

        # Register a test user
        self.user_service.register(
            self.user.username, self.user.password
        )

        # Test if register fails if username or password is too short
        with self.assertRaises(ShortCredentialsError):
            self.user_service.register(
                self.fail_user.username, self.fail_user.password
            )

        # Test if register fails if username already exists
        with self.assertRaises(UsernameExistsError):
            self.user_service.register(
                self.user.username, self.user.password
            )

    def test_user_login_success(self):
        self.user_service.clear_table()  # Clear database before testing
        self.user_service.register(self.user.username,
                                   self.user.password)
        login = self.user_service.login(
            self.user.username, self.user.password)
        self.assertEqual(login, True)

    def test_user_login_fail(self):
        self.user_service.clear_table()  # Clear database before testing

        self.user_service.register(self.user.username,
                                   self.user.password)

        # Test if login fails when passwords dont match
        with self.assertRaises(IncorrectCredentialsError):
            self.user_service.login(
                self.user.username, self.fail_user.password
            )

        # Test if login fails when usernames dont match
        with self.assertRaises(IncorrectCredentialsError):
            self.user_service.login(
                self.fail_user.username, self.user.password
            )

    def test_get_users(self):
        self.user_service.clear_table()  # Clear database before testing

        # Register
        self.user_service.register(self.user.username,
                                   self.user.password)

        # Check if user is added to the database
        users = self.user_service.get_users()
        self.assertEqual(len(users), 1)

    def test_user_join_org(self):
        self.user_service.clear_table()
        self.org_service.clear_table()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)

        # Join the organisation
        self.user_service.join_org("test_org", "test_key")
        org_name = self.user_service.get_org_name()
        self.assertEqual(org_name, "test_org")

        # Error if key is invalid
        with self.assertRaises(InvalidJoinKeyError):
            self.user_service.join_org("test_org", "test_key_invalid")

    def test_user_leave_org(self):
        self.user_service.clear_table()
        self.org_service.clear_table()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)

        # Join the organisation
        self.user_service.join_org("test_org", "test_key")
        org_name = self.user_service.get_org_name()
        self.assertEqual(org_name, "test_org")

        # Leave the organisation
        self.user_service.leave_org()
        org_name = self.user_service.get_org_name()
        self.assertEqual(org_name, None)
