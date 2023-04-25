import sqlite3


connection = sqlite3.connect("data.db")
# return cursor rows as dictionaries instead of the default tuple
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content, entry_date):
    with connection:
        # don't use format strings as they are open to SQL injection
        connection.execute(
            "INSERT INTO entries VALUES (?,?);",
            (entry_content, entry_date)
        )


def get_entries():
    # don't need with because we're not changing the db
    # loads results into a cursor
    cursor = connection.execute("SELECT * FROM entries;")
    # returns a tuple, not a dictionary
    return cursor
