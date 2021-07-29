import os
from enum import Enum

from core.exception import exception_handler


class Mode(Enum):
    OVER_WRITE = "w"
    ADD_WRITE = "a"


@exception_handler("ファイル書込み失敗")
def write_file(file_path: str, data: any, mode=Mode.OVER_WRITE.value):
    print(f"---------- STAR: write {file_path} ----------")
    with open(file_path, mode) as f:
        f.write(data)
    print(f"---------- END: write {file_path} -----------")


@exception_handler("ファイル読込み失敗")
def read_file(file_path: str):
    print(f"---------- STAR: read {file_path} ----------")
    with open(file_path) as f:
        return f.read().splitlines()


@exception_handler("ディレクトリ作成失敗")
def create_dirs(path: str):
    print(f"---------- STAR: create_dirs {path} ----------")
    if not os.path.exists(path):
        os.makedirs(path)


