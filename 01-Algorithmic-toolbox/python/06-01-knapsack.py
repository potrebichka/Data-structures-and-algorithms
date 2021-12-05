#python2
# This problem is about implementing an algorithm for the knapsack without repetitions problem
# In this problem, you are given a set of bars of gold and your goal is to take as much gold as possible
# into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence
# you cannot take a fraction of a bar).

def optimal_weight_greedy(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight_pd(W, w):
    n = len(w)
    value = [[0 for x in range(n)] for y in range(W+1)] 

    for i in range(0, n):
        for weight in range(0,W+1):
            value[weight][i] = value[weight][i-1]
            if w[i] <= weight:
                val = value[weight-w[i]][i-1] + w[i]
                if value[weight][i] < val:
                    value[weight][i] = val
    return value[W][n-1]
# The first line of the input contains the capacity W of a knapsack and the number n of bars
# of gold. The next line contains n integers w0, w1 .... wn-1 defining the weights of the bars of gold.

input = raw_input().split()
W, n = map(int, input)
input2 = raw_input().split()
w = map(int, input2)
print(optimal_weight_pd(W, w))
