import sys

sys.path.append(
    "../python-generators-0x00/"
)  # from previous proj, to  reuse db conn.

from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor


from seed import connect_to_prodev


class DatabaseConnection:
    def __init__(self, conn: MySQLConnection):
        self.conn = conn

    def __enter__(self) -> MySQLConnection:
        return self.conn

    def __exit__(self, type, value, traceback) -> None:
        self.conn.close()


with DatabaseConnection(connect_to_prodev()) as conn:
    cur: MySQLCursor = conn.cursor()
    # cur.execute('SELECT * FROM user_data;') # table in ALX_prodev db
    cur.execute("SELECT * FROM users;")
    for row in cur.fetchall():
        print(row)
