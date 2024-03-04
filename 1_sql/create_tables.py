import sqlite3


def create_tables():
    # read script file
    with open("tasks.sql", "r") as f:
        sql = f.read()

    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()

        # execute script with tables creation
        cur.executescript(sql)

if __name__=="__main__":
    create_tables()
