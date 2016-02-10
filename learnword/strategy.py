# -*- coding: utf-8 -*-
import learnword.db as db
import time


def export_to_learning_words(n):
    words = db.get_word_where_status(0, n)
    for word in words:
        db.add_learning_word(word[0])
        db.change_word_status(word[0], 1)
    return words


# def get_leaning_word(n):
#     pass


def check_new_day():
    # global is_new_day
    today = time.strftime("%Y-%m-%d")
    last_day = db.get_last_date()
    if today == last_day:
        # is_new_day = False
        return False
    else:
        return True
