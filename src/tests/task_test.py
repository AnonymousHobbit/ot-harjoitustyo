import unittest
from modules.task_service import TaskService
from modules.user_service import UserService


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.task = {"title": "tester", "status": False}
        self.task2 = {"title": "tester2", "status": False}
        self.task_service = TaskService(True)
        # Create a test user nro. 1
        self.user = UserService(True)
        self.user.clear_table()
        self.user.register("test", "test")

        # Create a test user nro. 2
        self.user_test = UserService(True)
        self.user_test.register("admin", "admin")

    def test_get_tasks(self):
        self.task_service.clear_db()  # Clear database before testing

        self.task_service.get_all()  # Get all tasks
        self.assertEqual(self.task_service.get_all(), [])

        # Create a task
        self.task_service.create_new(self.task["title"], self.task["status"])
        self.assertEqual(len(self.task_service.get_all()), 1)

    def test_get_tasks_by_username(self):
        self.task_service.clear_db()

        # Create a task for both users
        self.task_service.create_new(self.task["title"], self.user.get_id())
        self.task_service.create_new(
            self.task["title"], self.user_test.get_id())

        # Get all tasks by first user's name
        tasks = self.task_service.get_by_userid(self.user.get_id())
        self.assertEqual(len(tasks), 1)

        # Get all tasks by second user's name
        tasks = self.task_service.get_by_userid(self.user_test.get_id())
        self.assertEqual(len(tasks), 1)

    def test_task_creation(self):
        self.task_service.clear_db()

        created_task = self.task_service.create_new(
            self.task["title"], self.task["status"])
        # Test if create_new() returns True
        self.assertEqual(created_task, True)

        tasks_list = self.task_service.get_all()[0]

        # Test if task is in the list and has correct values
        self.assertEqual(tasks_list[1], "tester")
        self.assertEqual(tasks_list[2], "0")

    def test_task_deletion(self):
        self.task_service.clear_db()

        # Create a task
        self.task_service.create_new(self.task["title"], self.user.get_id())

        # Get task id
        task_to_delete = self.task_service.get_by_userid(self.user.get_id())
        task_id = task_to_delete[0][0]

        # Delete the task
        self.task_service.delete(task_id)

        # Test if task is not in the list
        self.assertEqual(self.task_service.get_by_userid(
            self.user.get_id()), [])
