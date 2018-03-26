# python2
# import sys

# O(log n)
def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while left <= right:
        mid = left +(right-left)/2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# O(n)
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

## python3
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
data = raw_input().split()
n = int(data[0])
a = list()
for ai in data[1 : n + 1]:
    a.append(int(ai))
data2 = raw_input().split()
k = int(data2[0])
b = []
for bi in data2[1:k+1]:
    b.append(int(bi))
for x in b:
        print binary_search(a, x),