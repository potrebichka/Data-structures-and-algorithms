#python2
#In this problem, your goal is to compute the length of a longest common subsequence of three sequences.
#Given three sequences A = (a1, a2, . . . , an), B = (b1, b2, . . . , bm), and C = (c1, c2, . . . , cl), find the
#length of their longest common subsequence, i.e., the largest non-negative integer p such that there
#exist indices 1 <= i1 < i2 < ... < ip <= n, 1 <= j1 < j2 < ... < jp <= m, 1 <= k1 < k2 < ... < kp <= l such
#that ai1 = bj1 = ck1, ... , aip = bjp = ckp

global ab
ab = list()

def lcs3(a, b, c):
    #write your code here
    AB = two_seq(a, b)
    ab = OutputAlignment(AB, len(a), len(b))
    ABC = two_seq(ab, c)
    return ABC[len(ab)][len(c)]

def two_seq(a, b):
    #write your code here
    n = len(a)
    m = len(b)
    D = [[0 for x in range(m+1)] for y in range(n+1)] 

    for j in range(1, m+1):
        for i in range(1, n+1):
            D[i][0] = 0
            D[0][j] = 0
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = D[i][j-1]
            deletion = D[i - 1][j]
            match = D[i-1][j-1]+1
            mismatch = D[i-1][j-1]
            if a[i-1] == b[j-1]:
                D[i][j] = max(insertion, deletion, match)
            else:
                D[i][j] = max(insertion, deletion, mismatch)  
    return D

def OutputAlignment(D, i, j):
    global ab
    if i == 0 and j == 0:
        return
    if i > 0 and D[i][j] == D[i - 1][j]:
        OutputAlignment(D, i-1, j)
    elif j > 0 and D[i][j] == D[i][j-1]:
        OutputAlignment(D, i, j-1)
    else:
        OutputAlignment(D, i-1, j-1)
        ab.append(a[i-1])
    return ab
        

n = int(raw_input())
a_n = raw_input().split()
a = list(map(int, a_n))


m = int(raw_input())
b_m = raw_input().split()
b = list(map(int, b_m))

l = int(raw_input())
c_l = raw_input().split()
c = list(map(int, c_l))

print(lcs3(a, b, c))
