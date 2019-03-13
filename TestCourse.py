import unittest

import Course


class TestCourse(unittest.TestCase):


    def testSomething(self):
        self.assertEqual(2, 2)

    def testDBID(self):
        c = Course()
        c.__setDataBaseID__(4080)
        self.assertEqual(c.__getDataBaseID__(), 4080)
    def test_get_class_number(self):
        c = Course()
        c.classNumber = 235
        self.assertEqual((235,c.getClassNumber))
    def test_set_class_number(self):
        c = Course()
        c.setClassNumber(55)
        self.assertEqual(55, c.classNumber)
    def test_get_time(self):
        c = Course()
        c.time = "14:20"
        self.assertEqual("14:20",c.get_time)
    def test_set_time(self):
        c = Course()
        c.set_time(15:00)
        self.assertEqual("15:00",c.time)
    def test_get_databaseID(self):
        c = Course()
        c.databaseID = 2134
        self.assertEqual(2134, c.getDataBaseID())
    def test_set_databaseID(self):
        c = Course()
        c.setDataBaseID(666)
        self.assertEqual(666,c.databaseID)
    def test_set_location(self):
        c = Course()
        c.set_location("EMS 156")
        self.assertEqual("EMS 156", c.location)
    def test_get_location(self):
        c = Course()
        c.location= "EMS 180"
        self.assertEqual("EMS 180", c.get_location)
    def test






if __name__ == '__main__':
    unittest.main()
