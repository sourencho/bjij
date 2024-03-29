"""
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.

Code Challenge: Solve the Frequent Words with Mismatches Problem.

"""
from collections import Counter
from itertools import takewhile
import operator

letters = {'A', 'C', 'G', 'T'}

def Neighbors(pattern, d):
    if len(pattern) == 0:
        return [pattern]
    if d == 0:
        return [pattern]

    mutations = []
    first_l = pattern[:1]
    mutations += [first_l + n for n in Neighbors(pattern[1:], d)]
    for l in letters - set(first_l):
        mutations += [l + n for n in Neighbors(pattern[1:], d-1)]

    return mutations

# Write your FrequentWordsWithMismatches() function here, along with any subroutines you need.
# Your function should return a list.
def FrequentWordsWithMismatches(data, k, d):
    freq = Counter()

    for i in range(len(data) - k + 1):
        k_mer = data[i:i+k]
        for n in Neighbors(k_mer, d):
            freq[n] += 1

    items = freq.most_common()
    max_ = items[0][1]
    top_items = list(takewhile(lambda x: x[1]==max_,  items))
    top_words = sorted([i[0] for i in top_items])
    return top_words
