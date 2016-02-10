# -*- coding: utf-8 -*-
import learnword.query as query
import learnword.db as db
import learnword.strategy as strategy

import time

LEARNING_WORD_THRESHOLD = 10
MAX_LEARNING_STATUS = 3

current_learning_status = 0


def add_word(word):
    definition, shanbay_id, audio, pronunciations \
        = query.query_shanbei_word(word)
    db.insert_word(word, definition, shanbay_id=shanbay_id, audio=audio,
                   pronunciations=pronunciations)


def get_learning_word(status=0):
    learning_word_number = db.count_table_row('learning_word')
    if learning_word_number < LEARNING_WORD_THRESHOLD:
        strategy.export_to_learning_words(LEARNING_WORD_THRESHOLD
                                          - learning_word_number)
    word = db.get_leaning_word(1, status)
    wordInfo = db.query_word(word[0])
    return wordInfo


def check_db_create():
    if not db.check_db_exist():
        db.init()


def reset_learning_word_status():
    today = time.strftime("%Y-%m-%d")
    if strategy.check_new_day():
        db.insert_to_date_trace(today)
        db.reset_learning_word_status()


def learning_word_up(word):
    word = db.query_learning_word(word)
    if word[1] == MAX_LEARNING_STATUS:
        db.delete_learning_word(word)
        return 0
    else:
        db.change_learning_word_status(word[0], word[1] + 1)
        return word[1] + 1


def get_current_status():
    return current_learning_status


def sync_current_status():
    global current_learning_status
    current_learning_status = db.get_lowest_learning_word_status()

check_db_create()
