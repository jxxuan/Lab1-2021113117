import unittest
import main
import show

class testcsp(unittest.TestCase):
    def test_1(self):
        result = show.calcShortestPath(main.process_text(), "out", "and")
        self.assertEqual(result, "out→new→life→and")

    def test_2(self):
        result = result = show.calcShortestPath(main.process_text(), "", "")
        self.assertEqual(result, "请输入word1！")

    def test_3(self):
        result = result = show.calcShortestPath(main.process_text(), "out", "")
        self.assertEqual(result, "请输入word2！")

    def test_4(self):
        result = result = show.calcShortestPath(main.process_text(), "oUt", "AND")
        self.assertEqual(result, "out→new→life→and")

    def test_5(self):
        result = result = show.calcShortestPath(main.process_text(), "out4", "and+7")
        self.assertEqual(result, "无效的输入！")

    def test_6(self):
        result = result = show.calcShortestPath(main.process_text(), "apple", "banana")
        self.assertEqual(result, "不存在的结点！")

    def test_7(self):
        result = result = show.calcShortestPath(main.process_text(), "out", "out")
        self.assertEqual(result, "out")


if __name__ == '__main__':
    unittest.main()
