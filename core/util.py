# -*- coding: utf-8 -*-
from concurrent import futures
import concurrent.futures
import random
import time


def __parallel_execute(func: any, data: any, max_workers=4):
    try:
        with futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            """
            1. 配列生成
            2. 1要素毎に別プロセスで処理
            """
            executors = [executor.submit(func, d) for d in data]
            for future in concurrent.futures.as_completed(executors):
                print(f"COMPLETE: executor. { future.result() }")
            executor.shutdown()
    except Exception as e:
        print(e)
        raise


def __sample_sleep():
    sleep_seconds = random.randint(1, 3)
    print(sleep_seconds)
    if sleep_seconds >= 2:
        return 1/0
    time.sleep(sleep_seconds)




