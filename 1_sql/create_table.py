import logging
from psycopg2 import DatabaseError

from connect import create_connect


def create_table(conn, sql_stmt: str):
    c = conn.cursor()
    try:
        c.execute(sql_stmt)
        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    try:
        with open("1_sql/tasks.sql", "r") as f:
            sql_stmt = f.read()
        with create_connect() as conn:
            create_table(conn, sql_stmt)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
