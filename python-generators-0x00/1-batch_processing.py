#!/usr/bin/env python3
from decimal import Decimal
from seed import connect_to_prodev
from contextlib import closing

def stream_users_in_batches(batch_size):
    """ fetches rows in batches """
    with closing(connect_to_prodev()) as cnx:
        with closing(cnx.cursor(dictionary=True)) as cur:
            cur.execute("SELECT * FROM user_data WHERE age > 25")
            while True:
                batch = cur.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
def batch_processing(batch_size):
    """ processes each batch to filter users over the age of 25 """
    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if isinstance(row["age"], Decimal):
                row["age"] = int(row["age"])
                print(row)
