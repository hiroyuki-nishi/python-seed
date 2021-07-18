# -*- coding: utf-8 -*-
import traceback
import datetime

from core import logger
from core.util import __parallel_process_execute, __sample_sleep
from core.file import write_file, create_dirs


class Params:
    path: str
    error_path: str

    def __init__(self, path, error_path):
        self.path = path
        self.error_path = error_path


# [ ] ★ TODO: 失敗しやすいところなのでテストコードを実装する ★
def __write_log(date: str, params: Params):
    """
    n 台数分の繰返し処理
    (例) 1000台なら、1000回ループする
    """
    try:
        print(date)
        # [ ] TODO: 1. ログを検索(BatchGetItem)
        # [ ] TODO: 2 ファイルに追記
        # [ ] TODO: 2-1 実行タイミン
        __sample_sleep()
        write_file(file_path=f"{params.path}/{date}.json", data="PIYOPIYO", mode="a")
        # [ ] TODO: 3 続きがあるなら1を繰り返す(lastEvaluatedKey?)
    except Exception as e:
        # [ ] TODO: 一時的なスロットルや失敗でもリトライしたい
        # [ ] TODO: 指定した失敗回数を超えたら 対象日付のクエリ?(日付？)をerrorファイルに書き出す
        logger.error(description=f"__write_log. ファイル書込み失敗. date: {date}", cause=traceback.format_exc())
        write_file(file_path=f"{params.error_path}/{date}.json", data="ERROR", mode="a")


def __create_dirs(params: Params):
    try:
        create_dirs(params.path)
        create_dirs(params.error_path)
    except Exception as e:
        # [ ] TODO: リトライしたい?
        logger.error(description=f"__create_dirs. params: {params}", cause=traceback.print_exc())


def __write_logs(date_str_list, clients=""):
    """
    n (日数分) の並列数
    (例) max_workersが4なら4並列
    [date_str_list] = [1, 2, ... 31]なら
    処理1. [1,2,3,4]
    処理2. [5,6,7,8]
    ....
    全て処理されるまで並列で動作する
    """
    try:
        print("---------- STAR: write_files ----------")
        now = datetime.datetime.now()
        params = Params(
            path=f"./out/{now}/dist",
            error_path=f"./out/{now}/error"
        )
        __create_dirs(params=params)
        # [ ] TODO: クエリ用にclientsの情報を型として渡す?(path, error_path, clients情報など)
        __parallel_process_execute(func=__write_log, data=date_str_list, option=params, max_workers=4)
        print("---------- END: write_files ----------")
    except Exception as e:
        # [ ] TODO: リトライしたい?
        logger.error(description=f"__write_logs.", cause=traceback.print_exc())


# [ ] TODO
def __find_clients():
    try:
        print("???")
    except Exception as e:
        print("???")
        print(e)


def read_file(path="./dates.txt"):
    try:
        with open(path) as f:
            return f.read().splitlines()
    except Exception as e:
        print("ファイル読込み失敗")
        print(e)
        raise


def export_logs():
    r = read_file()
    clients = __find_clients()
    __write_logs(date_str_list=r)
    print('completed.')


export_logs()
