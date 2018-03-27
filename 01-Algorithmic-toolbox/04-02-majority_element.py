#python2
#import sys

#Majority rule is a decision rule that selects the alternative which has a majority,
#that is, more than half the votes.
#Given a sequence of elements a1, a2, a3...an you would like to check whether
#it contains an element that appears more than n/2 times. A naive way to do
#this is the following.

# naive algorithm - O(n^2)
def get_majority_element(a, left, right):
    for i in range(0, n):
        currentElement = a[i]
        count = 0
        for j in range(0,n):
            if a[j] == currentElement:
                count += 1
        if count > n/2:
            return a[i]
    return -1

# O(nlog(n)) divide-conquer algorithm
def majority(a, left, right):
    if left >= right:
        return -1
    if left + 1 == right:
        return a[left]
    
    m1 = majority(a, left, (right-left)/2+left)
    m2 = majority(a, (right-left)/2+left, right)
    count = 0
    for i in range (left, right):
        if a[i] == m1:
            count+=1
    if count > (right-left)/2:
        return m1
    count = 0
    for i in range (left, right):
        if a[i] == m2:
            count+=1
    if count > (right-left)/2:
        return m2
    return -1

#if __name__ == '__main__':
#    input = sys.stdin.read()
input = raw_input().split()
n = int(input[0])
a = raw_input().split()
for i in range (0, len(a)):
    a[i] = int(a[i])
if majority(a, 0, n) != -1:
    print(1)
else:
    print(0)