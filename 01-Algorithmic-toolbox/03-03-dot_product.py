#python3

import sys
#import numpy as np
def max_dot_product(a, b):
    #write your code here
	res = 0
	i = 0
	n = len(a)
	a = a.sort()
	b = b.sort()
	for i in range(0, len(a)):
	    res += a * b
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
	
print(max_dot_product(a, b))   
