# -*- coding: utf-8 -*-
import sqlite3
import datetime
import os

dbFileName = 'learn-word.db'
dbPath = os.environ['HOME'] + '/' + dbFileName


def create_db():
    con = sqlite3.connect(dbPath)
    c = con.cursor()
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
    result = c.fetchone()
    c.close()
    con.close()
    return result
