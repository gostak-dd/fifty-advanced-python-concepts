import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    """Context manager for managing a database connection."""
    conn = sqlite3.connect(db_name)
    try:
        print("Database connection opened")
        yield conn
    finally:
        conn.close()
        print("Database connection closed")

# Usage
with database_connection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Alice"))
    conn.commit()
    print("Data inserted successfully")

'''
Q: How does the context manager `database_connection` work in this code snippet?
A: The context manager `database_connection` is defined using the `@contextmanager` decorator 
from the `contextlib` module. It manages a database connection to an SQLite database specified 
by the `db_name` parameter. 
When the context manager is entered (using the `with` statement), it opens a connection to the
database and yields the connection object to the block of code inside the `with` statement.
The code inside the `with` block can then use the connection to perform database operations, such as
creating tables and inserting data.

When the block of code inside the `with` statement is exited, either normally or due to an exception,
the `finally` block is executed, which closes the database connection and prints a message indicating
that the connection has been closed. This ensures that the database connection is properly managed and
cleaned up.

Q: what happens if you remove 'contextmanager' decorator from the code snippet?
A: If you remove the `@contextmanager` decorator from the `database_connection` function, it will no 
longer be recognized as a context manager. As a result, when you try to 
use it with the `with` statement, you will encounter a `TypeError` because the 
function will not return an object that implements the context management protocol 
(i.e., it won't have `__enter__` and `__exit__` methods).
    
'''
