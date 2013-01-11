PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employees (key INTEGER PRIMARY KEY, id TEXT, name TEXT, title TEXT);
CREATE TABLE comments (key INTEGER PRIMARY KEY, category_id NUMERIC, comment TEXT);
CREATE TABLE categories (key INTEGER PRIMARY KEY, text TEXT);
CREATE TABLE feedback (date NUMERIC, key INTEGER PRIMARY KEY, provider_key NUMERIC, target_key NUMERIC, comment_key NUMERIC);
COMMIT;
