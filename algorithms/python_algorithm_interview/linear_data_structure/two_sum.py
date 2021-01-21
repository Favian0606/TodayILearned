from decorators import timer
from typing import List

nums_one = [2, 7, 11, 15]
target_one = 9

nums_two = [3, 2, 4]
target_two = 6

nums_three = [3, 3]
target_three = 6


# solution 1
@timer
def get_two_sum(nums: List[int], target: int) -> List[int]:
    """Brute-force: calculate possible pairs from the first until they add up to target"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(get_two_sum(nums_one, target_one))
print(get_two_sum(nums_two, target_two))
print(get_two_sum(nums_three, target_three))


# solution 2
@timer
def get_two_sum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]


print(get_two_sum(nums_one, target_one))
print(get_two_sum(nums_two, target_two))
print(get_two_sum(nums_three, target_three))


# solution 3
@timer
def get_two_sum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # key: num value: index
    for i, n in enumerate(nums):
        nums_map[n] = i

    # find key(num) complement difference (target - n)
    for i, num in enumerate(nums):
        if (target - num) in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


print(get_two_sum(nums_one, target_one))
print(get_two_sum(nums_two, target_two))
print(get_two_sum(nums_three, target_three))


# solution 4
@timer
def get_two_sum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if (target - num) in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


print(get_two_sum(nums_one, target_one))
print(get_two_sum(nums_two, target_two))
print(get_two_sum(nums_three, target_three))


# solution 5
@timer
def get_two_sum(nums: List[int], target: int) -> List[int]:
    """Using two-pointer; sort is needed but if we do that, we cannot find original index"""
    left, right = 0, len(nums) - 1
    while not left == right:
        # if sum is under target; move left pointer to the right
        if nums[left] + nums[right] < target:
            left += 1
        # if sum is over target; move right pointer to the left
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
