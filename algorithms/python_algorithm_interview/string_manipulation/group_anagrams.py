from decorators import timer
from typing import List
from collections import defaultdict

input_str_list_one = ["eat", "tea", "tan", "ate", "nat", "bat"]
input_str_list_two = [""]
input_str_list_three = ["a"]


@timer
def find_group_anagrams(strs: List[str]) -> List[List[str]]:
    # if string items are anagram, sorted result of them should be the same
    # we have to group them thus sorted result is used as a key
    anagram_group = defaultdict(list)

    for word in strs:
        # using sorted() with string list returns chars list
        # anagram group has the same key with sorted string
        anagram_group[''.join(sorted(word))].append(word)
    # https://bluese05.tistory.com/67
    # dict values() method returns <class 'dict_values'>
    # view objects: provides a dynamic view on the dictionary's entries, which means that when dictionary changes,
    # the view reflects these changes
    return list(anagram_group.values())


print(find_group_anagrams(input_str_list_one))
print(find_group_anagrams(input_str_list_two))
print(find_group_anagrams(input_str_list_three))