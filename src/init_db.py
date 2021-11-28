import os
from database import get_connection


def clear_db(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS tasks")
    cursor.execute("DROP TABLE IF EXISTS users")
    connection.commit()
    print("[+] Table 'users', 'tasks' dropped")


def create_users(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connection.commit()
    print("[+] Table 'users' created")


def create_task(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    connection.commit()
    print("[+] Table 'tasks' created")


def main(testing=False):
    if not os.path.exists("src/databases/"):
        os.mkdir("src/databases")

    if not testing:
        connection = get_connection()
        print("\n[*] Initializing main database")
        clear_db(connection)
        create_users(connection)
        create_task(connection)

    connection = get_connection(True)
    print("\n[*] Initializing test database")
    clear_db(connection)
    create_users(connection)
    create_task(connection)

    print("\n[*] Finished initializing databases")


if __name__ == "__main__":
    main()
