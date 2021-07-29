import unittest

from core.file import write_file, create_dirs


class TestFile(unittest.TestCase):
    def test_write_file_ファイル書き込みに失敗すること(self):
        with self.assertRaises(Exception):
            write_file("a", None)

    def test_create_dir_ディレクトリ作成に失敗すること(self):
        with self.assertRaises(Exception):
            create_dirs("a", None)


if __name__ == "__main__":
    unittest.main()