# -*- coding: utf-8 -*-
import learnword.query as query
import learnword.db as db


def add_word(word):
    definition, shanbay_id, audio, pronunciations \
        = query.query_shanbei_word(word)
    db.insert_word(word, definition, shanbay_id=shanbay_id, audio=audio,
                   pronunciations=pronunciations)
