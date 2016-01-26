# -*- coding: utf-8 -*-
import unittest
import learnword.query as query


class TestQueryShanbay(unittest.TestCase):

    def test_query_word(self):
        definition, shanbay_id, audio, pronunciations \
            = query.query_shanbei_word('word')
        self.assertEqual(shanbay_id, 312)

if __name__ == '__main__':
    unittest.main()
