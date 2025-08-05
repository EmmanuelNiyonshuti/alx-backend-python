import sys

sys.path.append("../python-generators-0x00/")  # from previous proj, to  reuse db conn.

from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from seed import connect_to_prodev


class ExecuteQuery:
    def __init__(self, conn: MySQLConnection, query: str, param: int):
        self.conn = conn
        self.query = query
        self.param = param

    def __enter__(self) -> list[tuple]:
        self.cur: MySQLCursor = self.conn.cursor()
        self.cur.execute(self.query, (self.param,))
        return self.cur.fetchall()

    def __exit__(self, type, value, traceback):
        self.conn.close()


# with ExecuteQuery(connect_to_prodev(), 'SELECT * FROM user_data WHERE age > %s', 25) as res: user_data table in ALX_prodev db and %s in mysql
#     print(res)
with ExecuteQuery(
    connect_to_prodev(), "SELECT * FROM user_data WHERE age > ?", 25
) as res:
    print(res)
