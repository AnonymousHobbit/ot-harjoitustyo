from database import get_connection


class User:
    def __init__(self, test=False):
        self.connection = get_connection(test)
        self.username = ""
        self.password = ""

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM users
        """)

        return cursor.fetchall()

    def find(self, username):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM users WHERE username = ?
        """, (username,))

        return cursor.fetchone()

    def register(self, username, password):
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
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id FROM users WHERE username = ?
        """, (self.username,))

        return cursor.fetchone()[0]

    def clear_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM users
        """)

        self.connection.commit()
        return True
