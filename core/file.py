def write_file(file_path: str, data: any, mode="w"):
    try:
        print(f"---------- STAR: write {file_path} ----------")
        with open(file_path, mode) as f:
            f.write(data)
        print(f"---------- END: write {file_path} -----------")
    except Exception as e:
        # TODO: リトライしたい
        print("ファイル書込み失敗")
        print(e)
        raise

