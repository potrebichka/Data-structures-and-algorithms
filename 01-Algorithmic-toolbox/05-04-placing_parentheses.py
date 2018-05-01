#python2
# Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
# operations using additional parentheses.

global m, M

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(d, op):
    #write your code here
    return 0

def MinAndMax(i, j):
    minimum = 10 ** 9
    maximum = - 10** 9
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k-1])
        b = evalt(M[i][k], m[k+1][j], op[k-1])
        c = evalt(m[i][k], M[k+1][j], op[k-1])
        d = evalt(m[i][k], m[k+1][j], op[k-1])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def Parentheses(d, op):
    global m, M
    n = len(d)
    m = [[0 for x in range(n+1)] for y in range(n+1)] 
    M = [[0 for x in range(n+1)] for y in range(n+1)] 
    for i in range(1, n+1):
        m[i][i] = d[i-1]
        M[i][i] = d[i-1]
    for s in range(1, n):
        for i in range(1, n-s+1):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j)
    return M[1][n]

#The only line of the input contains a string s of length 2n + 1 for some n, with symbols
#s0, s1, . . . , s2n. Each symbol at an even position of s is a digit (that is, an integer from 0 to 9) while
#each symbol at an odd position is one of three operations from {+,-,*}.
# 1 <= n <= 14 (hence the string contains at most 29 symbols).

input = list(raw_input())
n = len(input)
# arrays for digits and for operators
d, op = [], []
for i in range(0, n):
    if i % 2 == 0:
        d.append(int(input[i]))
    else:
        op.append(input[i])

print(Parentheses(d, op))

