from concurrent import futures
import time


def sample_func(index):
    print('index: %s started.' % index)
    sleep_seconds = random.randint(2, 4)
    time.sleep(sleep_seconds)
    print('index: %s ended.' % index)


# 並列処理
# TODO: 1. 日付ファイル一覧を読み込む
# TODO: 2. 10並列で並列処理をしてファイルを作成+書き込む
# TODO: 3. 残りの日付があれば1から繰り返す
# ----------------------------------
# DynamoDB
# TODO: 1. BatchGetItemを作成

future_list = []
with futures.ProcessPoolExecutor(max_workers=4) as executor:
# with futures.ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(20):
        future = executor.submit(fn=sample_func, index=i)
        future_list.append(future)
    _ = futures.as_completed(fs=future_list)

print('completed.')