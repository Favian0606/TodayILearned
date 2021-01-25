from decorators import timer
from typing import List

import sys

prices_one = [7, 1, 5, 3, 6, 4]
prices_two = [7, 6, 4, 3, 1]


# solution 1
@timer
def maximize_profit(prices: List[int]) -> int:
    """Brute-force calculate every possible trades"""
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


print(maximize_profit(prices_one))
print(maximize_profit(prices_two))


# solution 2
@timer
def maximize_profit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # update min and max values
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(maximize_profit(prices_one))
print(maximize_profit(prices_two))
