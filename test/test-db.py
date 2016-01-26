# -*- coding: utf-8 -*-
import unittest
import learnword.query as query
import learnword.db as db


class TestDB(unittest.TestCase):
    def setUp(self):
        db.delete_db()
        db.create_db()

    def test_add_word(self):
        definition, shanbay_id, audio, pronunciations \
            = query.query_shanbei_word('word')
        db.insert_word('word', definition, shanbay_id=shanbay_id, audio=audio,
                       pronunciations=pronunciations)
        row_n = db.count_table_row('word')
        self.assertEqual(row_n, 1)
        word_row = db.query_word('word')
        self.assertEqual(word_row[0], u'word')

if __name__ == '__main__':
    unittest.main()
