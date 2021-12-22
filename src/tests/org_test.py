import unittest
from modules.user_service import UserService
from modules.org_service import OrgService, OrganisationExistsError, ShortNameError
from models.user import User


class OrgServiceTest(unittest.TestCase):
    def setUp(self):
        self.user = User("admin", "admin")
        self.user_service = UserService(True)
        self.org_service = OrgService(True)

    def test_org_create(self):
        self.user_service.clear_table()
        self.org_service.clear_table()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)
        org = self.org_service.find("test_org")
        self.assertEqual(org[1], "test_org")

    def test_org_create_fail(self):
        # If organisation already exists
        with self.assertRaises(OrganisationExistsError):
            self.org_service.create_new(
                "test_org", "test_key", self.user_service)

        # If name or join key is less than 3 characters
        with self.assertRaises(ShortNameError):
            self.org_service.create_new(
                "te", "te", self.user_service)

    def test_check_join_key(self):
        self.user_service.clear_table()
        self.org_service.clear_table()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)
        org = self.org_service.find("test_org")
        self.assertEqual(org[1], "test_org")

        # Check if key is valid
        self.assertEqual(
            self.org_service.check_join_key("test_org", "test_key"),
            True
        )

        # Check if key is invalid
        self.assertEqual(
            self.org_service.check_join_key("test_org", "test_key2"),
            False
        )

        # Fail if organisation does not exist
        with self.assertRaises(OrganisationExistsError):
            self.org_service.check_join_key("test_org2", "test_key")

    def test_create_task(self):
        self.user_service.clear_table()
        self.org_service.clear_table()
        self.org_service.clear_tasks()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)
        org = self.org_service.find("test_org")
        self.assertEqual(org[1], "test_org")

        # Create a new task
        self.org_service.create_task("test_task", "test_org")
        tasks = self.org_service.get_all_tasks("test_org")
        self.assertEqual(len(tasks), 1)

        self.org_service.create_task("all done", "test_org")
        tasks = self.org_service.get_all_tasks("test_org")
        self.assertEqual(len(tasks), 2)

    def test_delete_task(self):
        self.user_service.clear_table()
        self.org_service.clear_table()
        self.org_service.clear_tasks()

        # Create a test user
        self.user_service.register(self.user.username, self.user.password)

        # Create a new organisation
        self.org_service.create_new("test_org", "test_key", self.user_service)
        org = self.org_service.find("test_org")
        self.assertEqual(org[1], "test_org")

        # Create a new task
        self.org_service.create_task("test_task", "test_org")
        tasks = self.org_service.get_all_tasks("test_org")
        self.assertEqual(len(tasks), 1)

        self.org_service.delete_task(tasks[0][0])
        tasks = self.org_service.get_all_tasks("test_org")
        self.assertEqual(len(tasks), 0)
