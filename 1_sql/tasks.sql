-- Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY, -- SQLite id INTEGER PRIMARY KEY AUTOINCREMENT
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Table: statuses
DROP TABLE IF EXISTS statuses;
CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    user_id INTEGER REFERENCES users(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    status_id INTEGER REFERENCES statuses(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);