import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_str(self):
        b = Base(3)
        expected_output = "[Base] (3)"
        self.assertEqual(str(b), expected_output)

if __name__ == '__main__':
    unittest.main()