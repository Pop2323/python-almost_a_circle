import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_width(self):
        r = Rectangle(5, 10)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_height(self):
        r = Rectangle(5, 10)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_x(self):
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

    def test_y(self):
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 1, 2, 3)
        expected_output = "[Rectangle] (3) 1/2 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_update_args(self):
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(7, 8, 9, 10, 11)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)

    def test_update_kwargs(self):
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()