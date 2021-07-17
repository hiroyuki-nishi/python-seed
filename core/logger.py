import datetime


def error(description: str, cause: str):
    print(f"ERROR: {description}. cause: {cause}, time_stamp: {datetime.datetime.now()}")
