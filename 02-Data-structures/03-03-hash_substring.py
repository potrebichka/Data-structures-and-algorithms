#python2
# Task. In this problem your goal is to implement the Rabin-Karp's algorithm for searching the given pattern 
# in the given text

import random

def read_input():
    return (raw_input().rstrip(), raw_input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def get_occurrences(pattern, text):
    p = 1000000007 # big prime number
    x = random.randrange(1, p)
    result = []
    pHash = PolyHash(pattern, p, x)
    H = PrecomputeHashes(text, len(pattern), p, x)
    for i in range (0, len(text) - len(pattern)+1):
        if not pHash == H[i]:
            continue
        if text[i: i + len(pattern)] ==  pattern:
            result.append(i)
    return result

# string hashing
def PolyHash(S, p, x):
    hash = 0 
    for i in range( len(S) - 1, -1, -1):
        hash = (hash * x + ord(S[i])) % p
    return hash

def PrecomputeHashes(T, len_P, p, x):
    H = []
    for i in range(0, len(T) - len_P+1):
        H.append(None)
    S = T[len(T) - len_P: len(T)]
    H[len(T) - len_P] = PolyHash(S, p, x)
    y = 1
    for i in range(1, len_P+1):
        y = (y * x) % p
    for i in range (len(T) - len_P-1, -1, -1):
        H[i] =  (x*H[i+1] + ord(T[i]) - y*ord(T[i+len_P])) % p
    return H

print_occurrences(get_occurrences(*read_input()))