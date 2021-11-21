from database import get_connection

class User:
    def __init__(self, test=False):
        self.connection = get_connection(test)

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
            msg = "Username or password is too short (min 3)"
            return msg

        if self.find(username) is not None:
            msg = "Username already exists"
            return msg

        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))

        self.connection.commit()
        return True
        

    def login(self, username, password):
        user = self.find(username)
        if user is None:
            msg = "Username or password is incorrect"
            return msg

        if user[2] != password:
            msg = "Username or password is incorrect"
            return msg

        return True
    
    def clear_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM users
        """)

        self.connection.commit()
        return True