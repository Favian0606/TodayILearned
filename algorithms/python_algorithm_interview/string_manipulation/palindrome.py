from functools import wraps
from time import time

input_text_example_one = 'A man, a plan, a canal: Panama'
input_text_example_two = 'race a car'


# decorator for measuring time
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it


# solution 1
@measure
def is_palindrome(input_string: str) -> bool:
    strs = []
    for char in input_string:
        # check if char is alphabet or number
        if char.isalnum():
            strs.append(char.lower())

    # for debug
    # print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():  # pop(0) takes O(n) time
            return False

    return True


print(is_palindrome(input_text_example_one))
print(is_palindrome(input_text_example_two))


# solution 2
from collections import deque


@measure
def is_palindrome(input_string: str) -> bool:
    strs: deque = deque()
    for char in input_string:
        # check if char is alphabet or number
        if char.isalnum():
            strs.append(char.lower())

    # for debug
    # print(strs)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # pop(0) takes O(n) time
            return False

    return True


print(is_palindrome(input_text_example_one))
print(is_palindrome(input_text_example_two))

# solution 3
import re


@measure
def is_palindrome(input_string: str) -> bool:
    s = input_string.lower()
    # filtering for only alphanumeric on lower case
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


print(is_palindrome(input_text_example_one))
print(is_palindrome(input_text_example_two))
