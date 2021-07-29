import os
from enum import Enum


class Mode(Enum):
    OVER_WRITE = "w"
    ADD_WRITE = "a"


def write_file(file_path: str, data: any, mode=Mode.OVER_WRITE):
    try:
        print(f"---------- STAR: write {file_path} ----------")
        with open(file_path, mode) as f:
            f.write(data)
        print(f"---------- END: write {file_path} -----------")
    except Exception as e:
        print("ファイル書込み失敗")
        return e


def create_dirs(path: str):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception as e:
        print("ディレクトリ作成失敗")
        return e


def read_file(path: str):
    try:
        with open(path) as f:
            return f.read().splitlines()
    except Exception as e:
        print("ファイル読込み失敗")
        return e
