# -*- coding: utf-8 -*-
import unittest
import learnword.query as query
import learnword.db as db


class TestDB(unittest.TestCase):
    def setUp(self):
        # db.delete_db()
        db.create_db()

    # def tearDown(self):
    #     db.delete_db()

    def test01_add_word(self):
        definition, shanbay_id, audio, pronunciations \
            = query.query_shanbei_word('word')
        db.insert_word('word', definition, shanbay_id=shanbay_id, audio=audio,
                       pronunciations=pronunciations)
        row_n = db.count_table_row('word')
        self.assertEqual(row_n, 1)
        word_row = db.query_word('word')
        self.assertEqual(word_row[0], u'word')

    def test02_get_word_where_state(self):
        word_row = db.get_word_where_state(0, 1)
        print word_row


if __name__ == '__main__':
    unittest.main()
