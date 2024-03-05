import logging
from psycopg2 import DatabaseError

from connect import create_connect
from create_table import create_table
from seed import (
    generate_fake_data,
    prepare_data,
    insert_data_to_db,
    NUMBER_TASKS,
    NUMBER_USERS,
)


def main():
    users, statuses, tasks = prepare_data(
        *generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    )

    try:
        with open("1_sql/tasks.sql", "r") as f:
            sql_stmt = f.read()
        with create_connect() as conn:
            create_table(conn, sql_stmt)

            # insert generated fake data into database
            insert_data_to_db(conn, users, statuses, tasks)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")


if __name__ == "__main__":
    main()
