#python2
# To force the given implementation of the quick sort algorithm to efficiently process sequences with
#few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
#partition procedure should partition the array into three parts: < x part, = x part, and > x part.
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j1 = l
    j2 = l
	# check if element less or equal pivot
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j1 += 1
            j2 += 1
            a[i], a[j1] = a[j1], a[i]
        elif a[i] == x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
    a[l], a[j1] = a[j1], a[l]
    return j1, j2


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
	# choose a pivot element
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    
    #use partition3
    m1, m2 = partition3(a, l, r)
	# sort less and greater parts
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);



input = raw_input().split()
n = int(input[0])
a = raw_input().split()
for i in range(0, len(a)):
    a[i] = int(a[i])
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print x, 