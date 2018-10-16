# python2
import sys

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = SortCharacters(text)
    class_ = ComputeCharClasses(text, order)
    L = 1
    while L < len(text):
        order = SortDoubled(text, L, order, class_)
        class_ = UpdateClasses(order, class_, L)
        L = 2 * L
    return order

def SortCharacters(S):
    order = [None] * len(S)
    characters = {'A':0, 'C':1, 'G':2, 'T':3}
    count = [0]* len(characters)
    char = 0
    for i in range(0, len(S)):
        count[characters[S[i]]] += 1
    for j in range(1, len(count)):
        count[j] += count[j-1]
    for i in range(len(S)-1, -1, -1):
        c = S[i]
        count[characters[c]] -= 1
        order[count[characters[c]]] = i
    return order

def ComputeCharClasses(S, order):
    class_ = [None]*len(S)
    class_[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            class_[order[i]] = class_[order[i-1]]+1
        else:
            class_[order[i]] = class_[order[i-1]]
    return class_

def SortDoubled(S, L, order, class_):
    count = [0] * len(S)
    newOrder = [None] * len(S)
    for i in range(0, len(S)):
        count[class_[i]] += 1
    for j in range(1, len(S)):
        count[j] += count[j-1]
    for i in range(len(S)-1, -1, -1):
        start = (order[i] - L + len(S))% len(S)
        cl = class_[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
    return newOrder

def UpdateClasses(newOrder, class_, L):
    n = len(newOrder)
    newClass = [None] * n
    newClass[newOrder[0]] = 0
    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = (cur + L) % n
        midPrev = (prev + L) % n
        if class_[cur] != class_[prev] or class_[mid] != class_[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass


def compare(pattern, text, suffix_index):
    
    for i in range(len(pattern)):
        try:
            if pattern[i] > text[suffix_index + i]:
                return 1
            elif pattern[i] < text[suffix_index + i]:
                return -1
        except:
            return 0
    return 0

def find_occurrences(text, patterns):
    occs = set()

    # write your code here
    suffix_array = build_suffix_array(text)
    for pattern in patterns:
        min_index = 0
        max_index = len(text)
        while min_index < max_index:
            mid_index = (min_index + max_index)/2
            flag = compare(pattern, text, suffix_array[mid_index])
            if flag == 1:
                min_index = mid_index +1 
            else:
                max_index = mid_index
        start = min_index
        max_index = len(text)
        while min_index < max_index:
            mid_index = (min_index + max_index)/2
            flag = compare(pattern, text, suffix_array[mid_index])
            if flag == -1:
                max_index = mid_index
            else:
                min_index = mid_index + 1
        end = max_index
        if start >= end:
            continue
        else:
            for pos in range(start, end):
                if pattern == text[suffix_array[pos]:suffix_array[pos]+len(pattern)]:
                    occs.add(suffix_array[pos])
    return occs



text = raw_input().strip()
pattern_count = int(raw_input().strip())
                  
patterns = raw_input().strip().split()
occs = find_occurrences(text, patterns)
print(" ".join(map(str, occs)))