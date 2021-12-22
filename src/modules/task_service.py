from database import get_connection


class TaskService:
    """Class used to handle tasks

    Attributes:
        connection: connection returned from database.py
    """

    def __init__(self, test=False):
        """Class used to handle tasks

        Args:
            connection: connection returned from database.py
            test: boolean used to determine if test database should be used
        """

        self.connection = get_connection(test)

    def get_all(self):
        """Returns all tasks"""

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM tasks
        """)
        return cursor.fetchall()

    def get_by_userid(self, user_id):
        """Get all tasks by user id

        Args:
            user_id: Id of the user
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM tasks
            WHERE user_id = ?
        """, (user_id,))
        return cursor.fetchall()

    def create_new(self, title, user_id):
        """Create new task

        Args:
            title: Title of the task
            user_id: Id of the user
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO tasks (title, status, user_id)
            VALUES (?, ?, ?)
        """, (title, False, user_id))
        self.connection.commit()
        return True

    def delete(self, task_id):
        """Delete task

        Args:
            task_id: Id of the task
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))
        self.connection.commit()
        return True

    def clear_db(self):
        """Delete all tasks from the database"""

        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM tasks
        """)
        self.connection.commit()
        return True


task_service = TaskService()
