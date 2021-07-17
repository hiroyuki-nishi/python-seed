# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import sys

"""
指定された年月日のテキストファイルを出力するpythonファイルです。

(実行例)
python dates.py 2021 11 30

結果
date.txtには以下の内容が書き込まれます。

2021-11-01
2021-11-02
...
2021-11-30
"""

print(sys.argv[0])
year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])


def __create_dates():
    try:
        print("---------- STAR: create ----------")
        date_list = [datetime(year, month, 1) + timedelta(days=i) for i in range(day)]
        date_str_list = [d.strftime("%Y-%m-%d") for d in date_list]
        print(date_str_list)
        print("---------- END: create ----------")
        return "\n".join(date_str_list)
    except Exception as e:
        print("日付作成失敗")
        print(e)
        raise


def write_file(list):
    try:
        print("---------- STAR: write ----------")
        with open('./dates.txt', 'w') as f:
            print(type(f))
            f.write(list)
        print("---------- END: write ----------")
    except Exception as e:
        print("ファイル書込み失敗")
        print(e)
        raise

write_file(__create_dates())


