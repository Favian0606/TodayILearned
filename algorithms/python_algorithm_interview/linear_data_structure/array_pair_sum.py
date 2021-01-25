from decorators import timer
from typing import List

nums_one = [1, 4, 3, 2]
nums_two = [6, 2, 6, 5, 1, 2]


# solution 1
@timer
def get_array_pair_sum(nums: List[int]) -> int:
    maximized_sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:  # list is sorted; just check min num of each pair to maximize sum
            maximized_sum += min(pair)
            pair = []  # clear pair check list for the next one

    return maximized_sum


print(get_array_pair_sum(nums_one))
print(get_array_pair_sum(nums_two))


# solution 2
@timer
def get_array_pair_sum(nums: List[int]) -> int:
    maximized_sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # sum only even number index from sorted list
        if i % 2 == 0:
            maximized_sum += n

    return maximized_sum


print(get_array_pair_sum(nums_one))
print(get_array_pair_sum(nums_two))


# solution 3
@timer
def get_array_pair_sum(nums: List[int]) -> int:
    """slicing improves performance"""
    return sum(sorted(nums)[::2])


print(get_array_pair_sum(nums_one))
print(get_array_pair_sum(nums_two))
