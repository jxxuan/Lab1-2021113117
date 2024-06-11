import unittest
import main

class testcsp(unittest.TestCase):
    def test_1(self):
        result = main.randomWalk(main.process_text(), "may")
        self.assertEqual(result, "may you be blessed with happiness health prosperty")

    def test_2(self):
        result = main.randomWalk(main.process_text(),)
        self.assertEqual(result, "")

    def test_3(self):
        result = main.randomWalk(main.process_text(), "one")
        self.assertEqual(result, "one two three one")


if __name__ == '__main__':
    unittest.main()
