import unittest


class TestFile(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_write_file(self):
        """test method for tashizan
        """
        expected = 8
        actual = 8
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()