
import unittest


"""
aws es create-elasticsearch-domain --domain-name mylogs-2 --elasticsearch-version 7.10 --elasticsearch-cluster-config '{ "InstanceType": "m3.xlarge.elasticsearch", "InstanceCount": 4, "DedicatedMasterEnabled": true, "ZoneAwarenessEnabled": true, "DedicatedMasterType": "m3.xlarge.elasticsearch", "DedicatedMasterCount": 3}' --endpoint=http://localhost:4566
"""


class TestFile(unittest.TestCase):
    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        print("setUp")

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        print("tearDown")

    def test_write_file_ファイル書き込みに失敗すること(self):
        print("AAA")


if __name__ == "__main__":
    unittest.main()
