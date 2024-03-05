/* select all tasks for the given user by id */
SELECT * from tasks WHERE user_id = 3;

/* select all tasks iby status id */
SELECT * FROM tasks WHERE status_id = 2;

/* select tasks by status 'new' */
SELECT * from tasks WHERE status_id = (SELECT id FROM statuses WHERE name = 'new');

/* update status by status_id */
UPDATE tasks SET status_id = 2  WHERE id = 3; 

/* update status by status name */
UPDATE tasks SET status_id = (SELECT id FROM statuses WHERE name = 'completed')  WHERE id = 4; 

/* select all users without tasks */
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

/* add new task to user by id */
INSERT INTO tasks(title, description, status_id, user_id) VALUES('Perform homework', 'Perform homework #3 in Data Science and Deutsch homework', 1, 4);

/* select all unfinished tasks */
SELECT * from tasks WHERE status_id IN (1, 2);
SELECT * from tasks WHERE status_id != 3;

/* delete task by id */
DELETE FROM tasks WHERE id = 16;

/* find users with email template */
SELECT * from users WHERE email LIKE '%.net%';

/* update user name */
UPDATE users SET fullname = 'Oleksandra Tkachuk', email = 'olex@example.com' WHERE id = 1;

/* select number of tasks for each status */
SELECT COUNT(status_id) as total_tasks, status_id  FROM tasks GROUP BY status_id; 

/* select tasks for users with some email template */
SELECT t.title, t.description, u.fullname AS owner, u.email FROM tasks as t  JOIN users as u ON u.id = t.user_id  WHERE u.email LIKE '%@example.com'; 

/* select tasks without description */
SELECT * FROM tasks WHERE description = NULL; 

/* select users and tasks in progress */
SELECT u.fullname as owner, t.id, t.title, t.description, t.status_id  FROM tasks as t INNER JOIN users as u ON u.id = t.user_id WHERE t.status_id = 2 ORDER BY u.fullname;

/* select users and number of their tasks */
SELECT u.fullname as owner, COUNT(t.user_id) as total_tasks FROM tasks as t LEFT JOIN users as u ON t.user_id = u.id GROUP BY u.fullname  ;





