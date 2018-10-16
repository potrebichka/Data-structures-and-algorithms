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
    characters = {'$':0, 'A':1, 'C':2, 'G':3, 'T':4}
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
        mid = cur + L
        midPrev = (prev + L) % n
        if class_[cur] != class_[prev] or class_[mid] != class_[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass

if __name__ == '__main__':
    text = raw_input().strip()
    print(" ".join(map(str, build_suffix_array(text))))