import pytest
from database_utils import MySQLDatabase

@pytest.fixture(scope="module")
def db_connection():
    db = MySQLDatabase(
        host="localhost",
        username="your_username",
        password="your_password",
        database="your_database"
    )
    db.connect()
    yield db
    db.disconnect()

def test_verify_user_password(db_connection):
    username = "test_user"
    password = "test_password"
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    result = db_connection.execute_query(query)

    assert len(result) == 1, "Username and password are not correct"
