def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestTubeCrawler))
    return suite
