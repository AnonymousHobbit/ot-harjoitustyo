import unittest
from modules.user import User
import init_db

class UserTest(unittest.TestCase):
    def setUp(self):
        self.testing_user = {"username":"test", "password":"test"}
    
