import unittest


class TestExportLogs(unittest.TestCase):
    def test_write_file_ファイル書き込みに失敗すること(self):
        print("AAA")


if __name__ == "__main__":
    unittest.main()
