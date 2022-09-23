import sqlite3
from sqlite3 import Error

def create_connection(path: str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'Error {e} occurred')
    
    return connection

def execute_query(connection: sqlite3.Connection, query: str) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'Error {e} occurred')