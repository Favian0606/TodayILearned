from decorators import timer
from typing import List

input_nums_one = [1, 1, 1, 2, 2, 3]
input_most_one = 2

input_nums_two = [1]
input_most_two = 1


from collections import Counter
import heapq


# solution 1
@timer
def get_top_k_frequent_elems(nums: List[int], k: int) -> List[int]:
    # 1. get frequencies from nums (have to retain mapping info of frequency and element)
    # 2. create min(max) queue based on frequency to pull tok k elements

    freqs = Counter(nums)
    freq_heap = []
    # heapq is min queue
    for f in freqs:
        heapq.heappush(freq_heap, (-freqs[f], f))  # heappush tuple item (inverse frequency, value)

    # pull out k items from min heap
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freq_heap)[1])

    return topk


print(get_top_k_frequent_elems(input_nums_one, input_most_one))
print(get_top_k_frequent_elems(input_nums_two, input_most_two))


# solution 2
@timer
def get_top_k_frequent_elems(nums: List[int], k: int) -> List[int]:
    return list(list(zip(*Counter(nums).most_common(k)))[0])


print(get_top_k_frequent_elems(input_nums_one, input_most_one))
print(get_top_k_frequent_elems(input_nums_two, input_most_two))
