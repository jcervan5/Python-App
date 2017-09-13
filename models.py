import sqlite3


def drop_table():
    with sqlite3.connect('whiskey.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS whiskey;""")
    return True


def create_db():
    with sqlite3.connect('whiskey.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE whiskey(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            abv INTEGER NOT NULL,
            price INTEGER NOT NULL
        );
        """
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
