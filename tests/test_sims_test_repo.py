"""
Example unit tests for sims_test_repo package
"""
import unittest
import desc.sims_test_repo

class sims_test_repoTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'

    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.sims_test_repo.sims_test_repo(self.message)
        self.assertEqual(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.sims_test_repo.sims_test_repo)
        foo = desc.sims_test_repo.sims_test_repo(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
