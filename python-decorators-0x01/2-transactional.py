import functools

with_db_connection = __import__("1-with_db_connection.py").with_db_connection


def transactional(func):
    # manages database transactions by automatically committing or rolling back changes

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cnx = args[0]
        try:
            result = func(*args, **kwargs)
            cnx.commit()
            return result
        except Exception as e:
            print(e)
            cnx.rollback()

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    #### Update user's email with automatic transaction handling


update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
