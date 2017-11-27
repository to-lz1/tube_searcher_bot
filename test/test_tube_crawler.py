import unittest
from src.tube_crawler import TubeCrawler

class TestTubeCrawler(unittest.TestCase):

    def test_select_movies(self):
        t = TubeCrawler()
        result = t._TubeCrawler__select_movies({ "hogehoge", \
            "http://test/watch?v=aaaa", \
            "http://test/watch?v=bbbb&list=1", \
            "http://test/watch?v=cccc&index=1", \
            "http://test/watch?v=dddd&list=1&index=1", \
            "http://test/watch?v=eeee&index=1&list=1"
        }, 10)
        print(result)
        self.assertEqual(len(result), 5)
        self.assertTrue("aaaa" in result)
        self.assertTrue("bbbb" in result)
        self.assertTrue("cccc" in result)
        self.assertTrue("dddd" in result)
        self.assertTrue("eeee" in result)


if __name__ == '__main__':
    unittest.main()
