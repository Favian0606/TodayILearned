from decorators import timer
from typing import List

nums_input = [1, 2, 3, 4]


# solution 1
@timer
def product_except_self(nums: List[int]) -> List[int]:
    """Product of sliding each side productions (cumulative from pivot)"""
    out = []
    product_pivot = 1
    # left side productions
    for i in range(0, len(nums)):
        out.append(product_pivot)
        product_pivot = product_pivot * nums[i]

    product_pivot = 1  # initialization for right
    # right side productions on left side result for net result
    # range(len(nums) - 1, 0 - 1, -1): from last index to fist by step -1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * product_pivot
        product_pivot = product_pivot * nums[i]
    return out


print(product_except_self(nums_input))

