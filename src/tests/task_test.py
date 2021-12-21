import unittest
from modules.task_service import TaskService
from modules.user_service import UserService


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.task = {"title": "tester", "status": False}
        self.task2 = {"title": "tester2", "status": False}

        # Create a test user nro. 1
        self.user = UserService()
        self.user.clear_table()
        self.user.register("test", "test")

        # Create a test user nro. 2
        self.user_test = UserService()
        self.user_test.register("admin", "admin")

    def test_get_tasks(self):
        task = TaskService()
        task.clear_db()  # Clear database before testing

        task.get_all()  # Get all tasks
        self.assertEqual(task.get_all(), [])

        # Create a task
        task.create_new(self.task["title"], self.task["status"])
        self.assertEqual(len(task.get_all()), 1)

    def test_get_tasks_by_username(self):
        task = TaskService()
        task.clear_db()

        # Create a task for both users
        task.create_new(self.task["title"], self.user.get_id())
        task.create_new(
            self.task["title"], self.user_test.get_id())

        # Get all tasks by first user's name
        tasks = task.get_by_userid(self.user.get_id())
        self.assertEqual(len(tasks), 1)

        # Get all tasks by second user's name
        tasks = task.get_by_userid(self.user_test.get_id())
        self.assertEqual(len(tasks), 1)

    def test_task_creation(self):
        task = TaskService()
        task.clear_db()

        created_task = task.create_new(
            self.task["title"], self.task["status"])
        # Test if create_new() returns True
        self.assertEqual(created_task, True)

        tasks_list = task.get_all()[0]

        # Test if task is in the list and has correct values
        self.assertEqual(tasks_list[1], "tester")
        self.assertEqual(tasks_list[2], "0")

    def test_task_deletion(self):
        task = TaskService()
        task.clear_db()

        # Create a task
        task.create_new(self.task["title"], self.user.get_id())

        # Get task id
        task_to_delete = task.get_by_userid(self.user.get_id())
        task_id = task_to_delete[0][0]

        # Delete the task
        task.delete(task_id)

        # Test if task is not in the list
        self.assertEqual(task.get_by_userid(self.user.get_id()), [])
