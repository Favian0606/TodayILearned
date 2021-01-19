from decorators import timer
from typing import List
from collections import Counter, defaultdict

import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


@timer
def find_most_common_word(paragraph: str, banned: List[str]) -> str:
    # data cleansing
    # remove non-word, not case sensitive
    # substitute now word character(\w) with whitespace
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]

    # count word frequency
    # counts = defaultdict(int)
    # for word in words:
    #     counts[word] += 1

    # mc_word = max(counts, key=counts.get)

    word_counts = Counter(words)
    # most_common returns a list of the n most common elements; each element is tuple (elem, count)
    return word_counts.most_common(1)[0][0]  


print(find_most_common_word(paragraph, banned))
