import os
from database import get_connection


def clear_db(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS tasks")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS organisation_tasks")
    cursor.execute("DROP TABLE IF EXISTS organisations")
    connection.commit()
    print("[+] Table 'users', 'tasks', 'organisations', 'organisation_tasks' dropped")


def create_users(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            org_name TEXT,
            FOREIGN KEY(org_name) REFERENCES organisation(name)
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
            status TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    connection.commit()
    print("[+] Table 'tasks' created")


def create_org(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS organisations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            join_key TEXT NOT NULL
        )
    """)
    connection.commit()
    print("[+] Table 'organisations' created")


def create_org_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS organisation_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            organisation_name TEXT NOT NULL,
            FOREIGN KEY(organisation_name) REFERENCES organisation(name)
        )
    """)
    connection.commit()
    print("[+] Table 'organisation_tasks' created")


def creation(connection):
    clear_db(connection)
    create_users(connection)
    create_task(connection)
    create_org(connection)
    create_org_tasks(connection)


def main(testing=False):
    if not os.path.exists("src/databases/"):
        os.mkdir("src/databases")

    if not testing:
        connection = get_connection()
        print("\n[*] Initializing main database")
        creation(connection)

    connection = get_connection(True)
    print("\n[*] Initializing test database")
    creation(connection)

    print("\n[*] Finished initializing databases")


if __name__ == "__main__":
    main()
