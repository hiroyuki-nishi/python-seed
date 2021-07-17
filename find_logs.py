# -*- coding: utf-8 -*-
import random
import time

from core.util import __parallel_execute
from core.file import write_file


# [ ] TODO 削除する
def __sample_sleep():
    sleep_seconds = random.randint(1, 3)
    time.sleep(sleep_seconds)


def __write_log(date: str):
    try:
        print(date)
        # [ ] TODO: 1. ログを検索(BatchGetItem)
        # [ ] TODO: 2 ファイルに追記
        # [ ] TODO: 2-1 実行タイミン
        __sample_sleep()
        write_file(file_path=f"./out/{date}.json", data="PIYOPIYO")
        # [ ] TODO: 3 続きがあるなら1を繰り返す(lastEvaluatedKey?)
    except Exception as e:
        # [ ] TODO: 一時的なスロットルや失敗でもリトライしたい
        # [ ] TODO: 指定した失敗回数を超えたら 対象日付のクエリ?(日付？)をerrorファイルに書き出す
        print("ファイル書込み失敗")
        print(e)
        raise


# [x] TODO: 3. 並列処理をしてファイルを作成+書き込む
def __write_logs(date_str_list, clients):
    try:
        print("---------- STAR: write_files ----------")
        # [ ] TODO: クエリ用にclientsの情報を型として渡す?
        __parallel_execute(func=__write_log, data=date_str_list, max_workers=4)
        print("---------- END: write_files ----------")
    except Exception as e:
        # [ ] TODO: リトライしたい
        print("ファイル書込み失敗")
        print(e)
        raise


# [ ] TODO
def __find_clients():
    try:
        print("???")
    except Exception as e:
        print("???")
        print(e)
        raise


def read_file(path="./dates.txt"):
    try:
        with open(path) as f:
            return f.read().splitlines()
    except Exception as e:
        print("ファイル読込み失敗")
        print(e)
        raise


r = read_file()
print(r)
clients = __find_clients()
__write_logs(date_str_list=r)
print('completed.')
