drop table if exists word;
CREATE TABLE IF NOT EXISTS word (
word TEXT PRIMARY KEY,
shanbay_id INTEGER,
definition TEXT NOT NULL,
learn_time INTEGER DEFAULT 0,
status INTEGER DEFAULT 0,
add_date DATETIME NOT NULL,
last_learn_date DATETIME,
audio TEXT,
pronunciations TEXT);

DROP TABLE IF EXISTS learning_word;
CREATE TABLE IF NO EXISTS learning_word (
word TEXT PRIMARY KEY,
status INTEGER
);
