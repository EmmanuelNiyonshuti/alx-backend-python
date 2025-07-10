import sqlite3
import functools

from contextlib import closing


def with_db_connection(func):
    """opens a database connection, passes it to the function and closes it afterword"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with closing(sqlite3.connect("users.db")) as cnx:
            result = func(cnx, *args, **kwargs)
            return result

    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
    #### Fetch user by ID with automatic connection handling


user = get_user_by_id(user_id=1)
print(user)
