from decorators import timer
from typing import List

nums_one = [-1, 0, 1, 2, -1, -4]
nums_two = []
nums_three = [0]


# solution 1
@timer
def three_sum(nums: List[int]) -> List[List[int]]:
    """Brute-force using three pointers checks if sum of them are zero"""
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # skip when facing same combination (prev = current)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)- 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


# solution 2
@timer
def three_sum(nums: List[int]) -> List[List[int]]:
    """Two pointers left and right, index i is base left(i+1) and right(len)"""
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # skip when facing same combination (prev = current)
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0; append found answer and skipping
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


print(three_sum(nums_one))
print(three_sum(nums_two))
print(three_sum(nums_three))