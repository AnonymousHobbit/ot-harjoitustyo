from database import get_connection
from modules.org_service import OrgService

class UserService:
    """Class used to handle user activities

        Attributes:
            connection: connection returned from database.py
            org_service: OrgService class
            username: username of user
            password: password of user
    """
    def __init__(self, test=False):
        """Class used to handle user activities

        Args:
            connection: connection returned from database.py
            test: boolean used to determine if test database should be used
        """

        self.connection = get_connection(test)
        self.org_service = OrgService()
        self.username = ""
        self.password = ""

    def get_users(self):
        """Get all users"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM users
        """)

        return cursor.fetchall()

    def find(self, username):
        """Find user by username from database

        Args:
            username: username of user
        """

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM users WHERE username = ?
        """, (username,))

        return cursor.fetchone()

    def register(self, username, password):
        """Find user by username from database
        
        Returns false if username already exists
        Returns false if username or password is less than 3 characters

        Args:
            username: username of user
            password: password of user
        """

        if len(username) < 3 or len(password) < 3:
            print("Username or password is too short (min 3)")
            return False

        if self.find(username) is not None:
            print("Username already exists")
            return False

        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))

        self.username = username
        self.password = password
        self.connection.commit()
        return True

    def login(self, username, password):
        """Sets username and password if login is successful
        
        Returns false if username or password is incorrect

        Args:
            username: username of user
            password: password of user
        """

        user = self.find(username)
        if user is None:
            print("Username or password is incorrect")
            return False

        if user[2] != password:
            print("Username or password is incorrect")
            return False

        self.username = username
        self.password = password
        return True

    def get_id(self):
        """Returns id of user"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id FROM users WHERE username = ?
        """, (self.username,))

        return cursor.fetchone()[0]

    def get_name(self):
        """Returns name of user"""
        return self.username

    def join_org(self, name, key):
        """Join a new organisation
        
        Return false if join key is incorrect

        Args:
            name: name of organisation
            key: join key of organisation
        """
        if not self.org_service.check_join_key(name, key):
            print("Invalid join key")
            return False
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users SET org_name = ? WHERE username = ?
        """, (name, self.username))

        self.connection.commit()
        return True
        
    def get_org_name(self):
        """Return name of the organisation"""

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT org_name FROM users WHERE username = ?
        """, (self.username,))

        return cursor.fetchone()[0]

    def clear_table(self):
        """Delete all tasks from the database"""
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM users
        """)

        self.connection.commit()
        return True

user_service = UserService()