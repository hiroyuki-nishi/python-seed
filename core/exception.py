from functools import wraps


class MyException(Exception):
    def __init__(self, arg=""):
        self.arg = arg


class SystemException(MyException):
    def __str__(self):
        return (
            f"[{self.arg}]..."
        )


def exception_handler(message: str):
    """
    リトライするデコレータを返す
    :param message: Exceptionになった場合に表示するメッセージ
    :return: デコレータ
    """

    def _handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(message)
                raise SystemException(e)
        return wrapper
    return _handler
