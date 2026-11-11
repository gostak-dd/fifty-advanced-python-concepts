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
