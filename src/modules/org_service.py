from database import get_connection


class OrganisationExistsError(Exception):
    pass


class ShortNameError(Exception):
    pass


class OrgService:
    """Class used to handle the organisation

    Attributes:
        connection: connection returned from database.py
    """

    def __init__(self, test=False):
        """Class used to handle the organisation

        Args:
            connection: connection returned from database.py
            test: boolean used to determine if test database should be used
        """

        self.connection = get_connection(test)

    def get_all(self):
        """Returns all organisations"""

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM organisations
        """)
        return cursor.fetchall()

    def get_all_tasks(self, name):
        """Returns all tasks for an organisation

        Args:
            name: Name of the organisation
        """

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM organisation_tasks WHERE organisation_name = ?
        """, (name,))
        return cursor.fetchall()

    def create_task(self, title, org_name):
        """Create new task

        Args:
            title: Title of the task
            org_name: organisation name
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO organisation_tasks (title, status, organisation_name)
            VALUES (?, ?, ?)
        """, (title, False, org_name))
        self.connection.commit()
        return True

    def find(self, name):
        """Finds an organisation by name

        Args:
            name: Name of the organisation
        """

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM organisations WHERE name = ?
        """, (name,))
        return cursor.fetchone()

    def check_join_key(self, name, join_key):
        """Finds an organisation by name

        If key is correct, return true. Else returns false

        Args:
            name: Name of the organisation
            join_key: Join key of the organisation
        """
        if not self.find(name):
            raise OrganisationExistsError("Organisation does not exist")

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT join_key FROM organisations WHERE name = ?
        """, (name,))
        db_key = cursor.fetchone()[0]
        if db_key == join_key:
            return True
        return False

    def delete_task(self, task_id):
        """Deletes a task

        Args:
            task_id: ID of the task
        """

        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM organisation_tasks WHERE id = ?
        """, (task_id,))
        self.connection.commit()
        return True

    def create_new(self, name, join_key, user_service):
        """Creates a new organisation

        Returns false if organisation already exists
        Returns false if join key or name is less than 3 characters

        Args:
            name: Name of the organisation
            join_key: Join key of the organisation
            user_service: User service object
        """

        name = name.lower()
        if len(name) < 3 or len(join_key) < 3:
            raise ShortNameError(
                "Name and join key must be at least 3 characters")

        if self.find(name) is not None:
            raise OrganisationExistsError("Organisation already exists")

        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO organisations (name, join_key) VALUES (?, ?)
        """, (name, join_key))
        self.connection.commit()
        self.check_join_key(name, join_key)
        user_service.join_org(name, join_key)
        return True

    def clear_table(self):
        """Clears the organisation table"""

        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM organisations
        """)
        self.connection.commit()
        return True

    def clear_tasks(self):
        """Clears the organisation tasks table"""

        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM organisation_tasks
        """)
        self.connection.commit()
        return True
