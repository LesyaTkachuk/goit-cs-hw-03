import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 5
NUMBER_TASKS = 15


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []  # fake users array
    fake_statuses = [("new",), ("in progress",), ("completed",)]  # fake statuses array
    fake_tasks = []  # fake tsks array

    fake_data = faker.Faker()

    # fake users creation
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    # fake tasks creation
    for _ in range(number_tasks):
        fake_tasks.append(
            (fake_data.text(max_nb_chars=20), fake_data.sentence(nb_words=10))
        )

    return fake_users, fake_statuses, fake_tasks


def prepare_data(users, statuses, tasks) -> tuple():
    prepared_tasks = []  # for tasks table

    for task in tasks:
        """fill tasks array with task title, description, status_id as random integer from 1-3, and user_id as random integer in range of users number"""
        prepared_tasks.append(
            (task[0], task[1], randint(1, len(statuses)), randint(1, NUMBER_USERS))
        )

    return users, statuses, prepared_tasks


def insert_data_to_db(users, statuses, tasks) -> None:
    # create connection with our database
    with sqlite3.connect("tasks.db") as con:

        cur = con.cursor()

        # query for users table filling with prepared fake data
        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""

        # execute several scripts with the halp of executemany() method to insert data into the table
        cur.executemany(sql_to_users, users)

        # query for statuses table filling with prepared fake data
        sql_to_statuses = """INSERT INTO statuses(name)
                               VALUES (?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_statuses, statuses)

        # query for tasks table filling with prepared fake data
        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_tasks, tasks)

        # fix data in database
        con.commit()


if __name__ == "__main__":
    # get fake and formatted data
    users, statuses, tasks = prepare_data(
        *generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    )

    # insert generated fake data into database
    insert_data_to_db(users, statuses, tasks)
