import unittest
from modules.task_service import Task


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.task = {"title": "tester",
                     "description": "This is a test task", "status": False}

    def test_get_tasks(self):
        task = Task()
        task.clear_db()  # Clear database before testing

        task.get_all()  # Get all tasks
        self.assertEqual(task.get_all(), [])

        # Create a task
        task.create_new(self.task["title"],
                        self.task["description"], self.task["status"])
        self.assertEqual(len(task.get_all()), 1)

    def test_task_creation(self):
        task = Task()
        task.clear_db()  # Clear database before testing

        created_task = task.create_new(
            self.task["title"], self.task["description"], self.task["status"])
        # Test if create_new() returns True
        self.assertEqual(created_task, True)

        tasks_list = task.get_all()[0]

        # Test if task is in the list and has correct values
        self.assertEqual(tasks_list[1], "tester")
        self.assertEqual(tasks_list[2], "This is a test task")
        self.assertEqual(tasks_list[3], "0")
