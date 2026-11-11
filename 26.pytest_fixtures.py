## Run test_pytest_1.py for this file

import pytest
import sqlite3

@pytest.fixture
def temp_db():
    # Setup: Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES ('Alice')")
    yield conn
    # Teardown: Close the connection
    conn.close()

def test_query_user(temp_db):
    cursor = temp_db.cursor()
    cursor.execute("SELECT name FROM users WHERE id=1")
    user = cursor.fetchone()
    assert user[0] == "Alice"

'''
Q: What is the purpose of the `@pytest.fixture` decorator in the provided code?
A: The `@pytest.fixture` decorator is used to define a fixture in pytest, which is a reusable piece
 of code that can be used to set up and tear down resources needed for tests. In the provided code, 
 the `temp_db` fixture creates an in-memory SQLite database, sets up a table and inserts a user, and 
 then yields the database connection for use in the test. After the test is done, the fixture ensures 
 that the database connection is closed, providing a clean state for subsequent tests. This helps in 
 maintaining test isolation and reusability of setup code.
'''
