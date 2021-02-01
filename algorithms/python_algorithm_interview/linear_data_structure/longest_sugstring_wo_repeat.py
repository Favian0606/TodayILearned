from decorators import timer

input_one = 'abcabcbb'
input_two = 'bbbbb'
input_three = 'pwwkew'
input_four = ''


# solution 1
@timer
def get_longest_substr_len(input_str: str) -> int:
    """Using sliding window"""
    used = {}
    start = max_length = 0
    # 1. check current character is used in this sub-string pointed by sliding window
    # 2. if current character is not used, determines if update is needed
    # between current max_length and new sliding window size
    # 3. if current character is used before, update left pointer of sliding window by (index of used char) + 1
    for index, char in enumerate(input_str):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:  # update length of longest sub-string
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length


print(get_longest_substr_len(input_one))
print(get_longest_substr_len(input_two))
print(get_longest_substr_len(input_three))
print(get_longest_substr_len(input_four))

