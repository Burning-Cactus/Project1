import unittest

import Course


class TestCourse(unittest.TestCase):
    c = Course()

    def testSomething(self):
        self.assertEqual(2, 2)

    def testDBID(self):
        c.__setDataBaseID__(4080)
        self.assertEqual(c.__getDataBaseID__(), 4080)

if __name__ == '__main__':
    unittest.main()
