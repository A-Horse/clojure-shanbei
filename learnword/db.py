# -*- coding: utf-8 -*-
import sqlite3
import datetime
import os
import os.path


dbFileName = 'learn-word.db'
dbPath = os.environ['HOME'] + '/' + dbFileName

MAX_LEARNING_STATUS = 3


def check_db_exist():
    return os.path.isfile(dbPath)


def init():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    with open('schema.sql', mode='r') as f:
        c.executescript(f.read())
    con.commit()
    c.close()
    con.close()


def delete_table(table):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('DROP TABLE IF EXISTS  ' + table + ';')
    c.close()
    con.close()


def delete_db():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    delete_table('word')
    con.commit()
    c.close()
    con.close()


def count_table_row(table):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT count(rowId) from word;')
    result = c.fetchone()[0]
    c.close()
    con.close()
    return result


def insert_word(word, definition, **kwargs):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    t = (word, definition, kwargs['shanbay_id'], kwargs['audio'],
         kwargs['pronunciations'], datetime.datetime.now())
    c.execute('INSERT INTO word ('
              + 'word, definition, shanbay_id, audio, '
              + 'pronunciations, add_date' + ')'
              + ' VALUES (?, ?, ?, ?, ?, ?);', t)
    con.commit()
    c.close()
    con.close()


def change_word_status(word, status):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('update word set status = ? where word = ?;',
              [status, word])
    con.commit()
    c.close()
    con.close()


def query_word(word):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT * from word where word = ?;', [word])
    result = c.fetchone()
    c.close()
    con.close()
    return result


def get_word_where_status(status, limit):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT * from word where status = ? ORDER BY random() limit ?;',
              (status, limit))
    result = c.fetchall()
    c.close()
    con.close()
    return result


def query_leaning_word(word):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT * from learning_word where word = ?;', [word])
    result = c.fetchone()
    c.close()
    con.close()
    return result


def get_leaning_word(n):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT * from learning_word ORDER BY random() LIMIT ?;', [n])
    result = c.fetchone()
    c.close()
    con.close()
    return result


def change_learning_word_status(word, status):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('update learning_word set status = ? where word = ?;',
              [status, word])
    con.commit()
    c.close()
    con.close()


def delete_learning_word(word):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('DELETE FROM learning_word where word = ?;', [word])
    con.commit()
    c.close()
    con.close()


def add_learning_word(word):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('INSERT INTO learning_word (word) VALUES (?);', [word])
    con.commit()
    c.close()
    con.close()


def get_all_learning_words():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute('SELECT * from learning_word;')
    result = c.fetchall()
    c.close()
    con.close()
    return result


def insert_to_date_trace(date_str):
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute(
        'INSERT INTO learning_date_trace (learning_date) VALUES (?);',
        [date_str])
    con.commit()
    c.close()
    con.close()


def get_last_date():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute(
        'SELECT * from learning_date_trace ' +
        'ORDER BY learning_date asc limit 1;'
    )
    result = c.fetchone()
    c.close()
    con.close()
    return result


def reset_learning_word_status():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
    c.execute(
        'UPDATE learning_word set status = 0;',
    )
    con.commit()
    c.close()
    con.close()
