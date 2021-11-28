from database import get_connection

class Task:
    def __init__(self, test=False):
        self.connection = get_connection(test)

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM tasks
        """)
        return cursor.fetchall()

    def get_by_name(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM tasks
            WHERE user_id = ?
        """, (user_id,))
        return cursor.fetchall()

    def create_new(self, title, description, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO tasks (title, description, status, user_id)
            VALUES (?, ?, ?, ?)
        """, (title, description, False, user_id))
        self.connection.commit()
        return True

    def clear_db(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM tasks
        """)
        self.connection.commit()
        return True
