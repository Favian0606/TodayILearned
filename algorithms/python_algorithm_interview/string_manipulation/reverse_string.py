from functools import wraps
import time

input_sequence_one = ["h", "e", "l", "l", "o"]
input_sequence_two = ["H", "a", "n", "n", "a", "h"]


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


from typing import List


# solution 1
@timer
def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s)-1  # double pointer for indexing
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


reverse_string(input_sequence_one)
reverse_string(input_sequence_two)

print(input_sequence_one)
print(input_sequence_two)

input_sequence_one = ["h", "e", "l", "l", "o"]
input_sequence_two = ["H", "a", "n", "n", "a", "h"]


# solution 2
@timer
def reverse_string(s: List[str]) -> None:
    s.reverse()  # in-place


reverse_string(input_sequence_one)
reverse_string(input_sequence_two)

print(input_sequence_one)
print(input_sequence_two)
