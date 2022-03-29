import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Running time is {t2 - t1}")
    return wrapper
