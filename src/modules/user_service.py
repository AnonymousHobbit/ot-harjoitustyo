from database import get_connection
from modules.org_service import OrgService
from models.user import User


class UsernameExistsError(Exception):
    pass


class ShortCredentialsError(Exception):
    pass


class IncorrectCredentialsError(Exception):
    pass


class InvalidJoinKey(Exception):
    pass


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
        self.org_service = OrgService(test)
        self.user = None

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
            raise ShortCredentialsError(
                "Username or password must be at least 3 characters")

        if self.find(username) is not None:
            raise UsernameExistsError("Username already exists")

        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))

        self.user = User(username, password)
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
            raise IncorrectCredentialsError("Incorrect username or password")

        if user[2] != password:
            raise IncorrectCredentialsError("Incorrect username or password")

        self.user = User(username, password)
        return True

    def get_id(self):
        """Returns id of user"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id FROM users WHERE username = ?
        """, (self.user.username,))

        return cursor.fetchone()[0]

    def get_name(self):
        """Returns name of user"""
        return self.user.username

    def join_org(self, name, key):
        """Join a new organisation

        Return false if join key is incorrect

        Args:
            name: name of organisation
            key: join key of organisation
        """
        if not self.org_service.check_join_key(name, key):
            raise InvalidJoinKey("Invalid join key")

        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users SET org_name = ? WHERE username = ?
        """, (name, self.user.username))

        self.connection.commit()
        return True

    def leave_org(self):
        """Leave organisation"""
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users SET org_name = NULL WHERE username = ?
        """, (self.user.username,))

        self.connection.commit()
        return True

    def get_org_name(self):
        """Return name of the organisation"""

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT org_name FROM users WHERE username = ?
        """, (self.user.username,))

        return cursor.fetchone()[0]

    def clear_table(self):
        """Delete all tasks from the database"""
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM users
        """)
        self.user = None
        self.connection.commit()
        return True


user_service = UserService()
