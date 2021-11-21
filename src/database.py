import sqlite3
from config import DATABASE_PATH, TESTING_DATABASE_PATH

def get_connection(test=False):
    con = sqlite3.connect(DATABASE_PATH if not test else TESTING_DATABASE_PATH)
    return con
