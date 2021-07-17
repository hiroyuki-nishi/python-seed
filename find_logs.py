# -*- coding: utf-8 -*-
from concurrent import futures
import time


def sample_func(index):
    print('index: %s started.' % index)
    sleep_seconds = random.randint(2, 4)
    time.sleep(sleep_seconds)
    print('index: %s ended.' % index)

def __mutliple():
    future_list = []
    with futures.ProcessPoolExecutor(max_workers=4) as executor:
        # with futures.ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(20):
            future = executor.submit(fn=sample_func, index=i)
            future_list.append(future)
        _ = futures.as_completed(fs=future_list)


# 並列処理
# [OK] TODO: 1. 日付ファイル一覧を読み込む
# [ ] TODO: 2. ファイルを順次処理で作成する（新規上書き）
# [ ] TODO: 3. 10並列で並列処理をしてファイルを作成+書き込む
# TODO: 3. 残りの日付があれば1から繰り返す

def read_dates(path="./dates.txt"):
    try:
        print("---------- STAR: read ----------")
        with open(path) as f:
            l = f.readlines()
            print(l)
        print("---------- END: read ----------")
    except Exception as e:
        print("ファイル読込み失敗")
        print(e)
        raise

read_dates()

print('completed.')
