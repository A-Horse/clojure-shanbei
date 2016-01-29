import sqlite3
import datetime
import os

dbFileName = 'learnword.db'
dbPath = os.environ['HOME'] + '/' + dbFileName

con = sqlite3.connect(dbPath)
c = con.cursor()


def create_db():
    c.execute('''
    CREATE TABLE IF NOT EXISTS word (
    word TEXT PRIMARY KEY,
    shanbay_id INTEGER,
    definition TEXT NOT NULL,
    learn_time INTEGER DEFAULT 0,
    status INTEGER DEFAULT 0,
    add_date DATETIME NOT NULL,
    last_learn_date DATETIME,
    audio TEXT,
    pronunciations TEXT);''')
    con.commit()


def delete_table(table):
    c.execute('DROP TABLE IF EXISTS ' + table + ';')


def delete_db():
    delete_table('word')
    con.commit()


def count_table_row(table):
    c.execute('SELECT count(rowId) from word;')
    return c.fetchone()[0]


def insert_word(word, definition, **kwargs):
    t = (word, definition, kwargs['shanbay_id'], kwargs['audio'],
         kwargs['pronunciations'], datetime.datetime.now())
    c.execute('''INSERT INTO word
    (word, definition, shanbay_id, audio, pronunciations, add_date)
    VALUES (?, ?, ?, ?, ?, ?);''', t)
    con.commit()


def query_word(word):
    c.execute('SELECT * from word where word = ?;', [word])
    return c.fetchone()


def close_db():
    con.close()


def close_cursor():
    c.close()


def get_word_where_state(status, limit=1):
    c.execute('SELECT * from word where status = ? ORDER BY RANDOM() LIMIT ?;', [status, limit])
    return c.fetchone()
