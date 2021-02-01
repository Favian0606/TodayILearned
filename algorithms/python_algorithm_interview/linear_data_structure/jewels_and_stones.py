from decorators import timer

jewels_one = 'aA'
stones_one = 'aAAbbbb'

jewels_two = 'z'
stones_two = 'ZZ'


# solution 1
@timer
def find_num_of_jewels(jewels: str, stones: str) -> int:
    freqs = {}
    count = 0

    for stone in stones:
        if stone in freqs:
            freqs[stone] += 1
        else:
            freqs[stone] = 1

    for jewel in jewels:
        if jewel in freqs:
            count += freqs[jewel]

    return count


print(find_num_of_jewels(jewels_one, stones_one))
print(find_num_of_jewels(jewels_two, stones_two))


from collections import defaultdict


# solution 2
@timer
def find_num_of_jewels(jewels: str, stones: str) -> int:
    freqs = defaultdict(int)
    count = 0

    for stone in stones:
        freqs[stone] += 1

    for jewel in jewels:
        if jewel in freqs:
            count += freqs[jewel]

    return count


print(find_num_of_jewels(jewels_one, stones_one))
print(find_num_of_jewels(jewels_two, stones_two))


from collections import Counter


# solution 3
@timer
def find_num_of_jewels(jewels: str, stones: str) -> int:
    freqs = Counter(stones)
    count = 0

    for jewel in jewels:
        count += freqs[jewel]

    return count


print(find_num_of_jewels(jewels_one, stones_one))
print(find_num_of_jewels(jewels_two, stones_two))


# solution 3
@timer
def find_num_of_jewels(jewels: str, stones: str) -> int:
    return sum(stone in jewels for stone in stones)


print(find_num_of_jewels(jewels_one, stones_one))
print(find_num_of_jewels(jewels_two, stones_two))
