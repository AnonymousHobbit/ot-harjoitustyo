from database import get_connection

def clear_db(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    connection.commit()
    print("[+] Table 'users' dropped")

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


def main(testing=False):
    if not testing:
        connection = get_connection()
        print("\n[*] Initializing main database")
        clear_db(connection)
        create_users(connection)

    connection = get_connection(True)
    print("\n[*] Initializing test database")
    clear_db(connection)
    create_users(connection)



    print("\n[*] Finished initializing database")


if __name__ == "__main__":
    main()