import unittest
import pep8
from models.rectangle import Rectangle

"""
This modual contains class TestBase:
"""


class TestRectangle(unittest.TestCase):

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        def testpep8(self):
        """ pep8 test """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/base.py'])
        print(r.total_errors, "total errors")
        self.assertEqual(r.total_errors, 0, "found code errors and warnings. ")

if __name__ == '__main__':
    unittest.main()
