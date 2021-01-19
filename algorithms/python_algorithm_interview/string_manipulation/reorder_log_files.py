from functools import wraps
from typing import List
import time


input_log = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def timer(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do something before
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        # Do something after
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000
        print(f"Finished {func.__name__!r} in {run_time:.4f} ms")
        return value
    return wrapper_timer


@timer
def reorder_logs(logs: List[str]) -> List[str]:
    letter_logs, digit_logs = [], []

    # split logs into letters and digits
    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    # sort() method is for list; sorted() method for iterable
    # sort letter logs with lambda on multiple keys
    # letter log first, identifier second
    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letter_logs + digit_logs


print(reorder_logs(input_log))
