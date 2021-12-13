from database import get_connection

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
        cursor.execute("SELECT * FROM organisations")
        return cursor.fetchall()

    def find(self, name):
        """Finds an organisation by name

        Args:
            name: Name of the organisation
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM organisations WHERE name = ?", (name,))
        return cursor.fetchone()

    def check_join_key(self, name, join_key):
        """Finds an organisation by name

        If key is correct, return true. Else returns false

        Args:
            name: Name of the organisation
            join_key: Join key of the organisation
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT join_key FROM organisations WHERE name = ?", (name,))
        db_key = cursor.fetchone()[0]
        if db_key == join_key:
            return True
        else:
            return False

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
            print("Name or join key is too short (min 3)")
            return False

        if self.find(name) is not None:
            print("Organisation with that name already exists")
            return False
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO organisations (name, join_key) VALUES (?, ?)", (name, join_key))
        self.connection.commit()
        user_service.join_org(name, join_key)
        
