import os
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

# create a pool of connections that is not thread safe
DATABASE_PROMPT = "Enter the DATABASE_URI or leave empty to use .env: "

database_uri = input(DATABASE_PROMPT)
if not database_uri:
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]

# pool with 1 connection that will go to max of ten
# minconn are created when the pool is created
# if not enough pools, will create more until max is reached
"""
    create a connection with:
        connection = pool.getconn()
    put connection back in the pool with
        pool.putconn(connection)
"""
pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_uri)


# create a context manager that gets a connection from the pool
#   and puts it back when finished
@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)