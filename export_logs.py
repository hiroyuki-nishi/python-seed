# -*- coding: utf-8 -*-
import traceback
import datetime

from core import logger
from core.util import __parallel_process_execute, __sample_sleep
from core.file import write_file, create_dirs, read_file
from infrastructure.dynamodb import find_client_ids


class Params:
    path: str
    error_path: str
    client_ids: any # TODO

    def __init__(self, path, error_path, client_ids):
        self.path = path
        self.error_path = error_path
        self.client_ids = client_ids


# [ ] ★ TODO: 失敗しやすいところなのでテストコードを実装する ★
def __write_log(date: str, params: Params, max_workers=50):
    """
    n 台数分の繰返し処理
    (例)
    1. 1000台なら、1000回ループする
    2. 50並列で動作させる
    """
    try:
        print(date)
        # [ ] TODO: 1. ログを検索(BatchGetItem)
        # [ ] TODO: 2 ファイルに追記
        # [ ] TODO: 2-1 実行タイミン
        __sample_sleep()
        # __parallel_process_execute(func=find_logs, data=query, option=params, max_workers=max_workers)
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


def __write_logs(date_str_list, client_ids):
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
            error_path=f"./out/{now}/error",
            client_ids=client_ids
        )
        __create_dirs(params=params)
        __parallel_process_execute(func=__write_log, data=date_str_list, option=params, max_workers=4)
        print("---------- END: write_files ----------")
    except Exception as e:
        # [ ] TODO: リトライしたい?
        logger.error(description=f"__write_logs.", cause=traceback.print_exc())


def export_logs():
    r = read_file(file_path="./dates.txt")
    client_ids = find_client_ids()
    __write_logs(date_str_list=r, client_ids=client_ids)
    print('completed.')


export_logs()
