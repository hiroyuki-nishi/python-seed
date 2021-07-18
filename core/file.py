import os


# [ ] TODO modeはenumにしたい
def write_file(file_path: str, data: any, mode="w"):
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
