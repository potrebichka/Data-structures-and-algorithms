#python2
#In this problem, your goal is to find the closest pair of points among the given n
#points. This is a basic primitive in computational geometry having applications in,
#for example, graphics, computer vision, traffic-control systems.

import math

def distance(P, a, b):
    return math.sqrt((P[a][0] - P[b][0]) ** 2 + (P[a][1] - P[b][1]) ** 2)

def minimum_distance(P):
    #write your code here
    n = len(P)
	# if there are two elements => return distance between two points
    if n == 2:
        return distance(P, 0, 1)
    elif n < 2:
        return -1
	# if there are three elements => calculate distances between three points
	# and return the minimum
    elif n == 3:
        d1 = distance(P, 0, 1)
        d2 = distance(P, 0, 2)
        d3 = distance(P, 1, 2)
        return min(d1, d2, d3)
    
	# divide array into two parts and call recursively each part and choose the minimum
    mid = n // 2
    midPoint = P[mid]
    
    d_left = minimum_distance(P[0:mid])
    d_right = minimum_distance(P[mid:n])
    d = min(d_left,d_right)
    
	# find point that has difference between X-coordinate with midpoint less than current
	# minimum distance and add them to strip array
    strip = []
    for i in range(0, n):
        if abs(P[i][0] - midPoint[0]) < d:
            strip.append(P[i])
	# choose the minimum 
    return min(d, stripClosest(strip, len(strip), d))

def stripClosest(strip, n, d):
    minimum = d
	# sort by Y coordinate
    strip_sorted = MergeSort_y(strip) 
            
	# find the minimum distance between points in strip
    for i in range(0, n-1):
        j = i + 1
        if strip_sorted[j][1] - strip_sorted[i][1]) < minimum:
            dist = distance(strip_sorted, j, i)
            if dist < minimum:
                minimum = dist
    return minimum

def MergeSort_y(P):
    n = len(P)
    if n <= 1:
        return P
    m = n/2
    B = MergeSort_y(P[0:m])
    C = MergeSort_y(P[m:n])
    A = Merge_y(B, C)
    return A
        
def Merge_y(B, C):
    p = len(B)
    q = len(C)
    D = []
    while (not (B == [])) and (not (C == [])):
        b = B[0]
        c = C[0]
        if b[1] <= c[1]:
            D.append(b)
            B.remove(b)
        else:
            D.append(c)
            C.remove(c)
    D.extend(B)
    D.extend(C)
    return D

def MergeSort_x(P):
    n = len(P)
	# if only one element in array => it is sorted
    if n <= 1:
        return P
	#divide array into two parts and sort parts recursively 
    m = n/2
    B = MergeSort_x(P[0:m])
    C = MergeSort_x(P[m:n])
	# merge two sorted parts
    A = Merge_x(B, C)
    return A
        
def Merge_x(B, C):
    p = len(B)
    q = len(C)
    D = []
	# while there are elements in any sorted array
    while (not (B == [])) and (not (C == [])):
	    # choose first elements in arrays
		# add greater element to new array
        b = B[0]
        c = C[0]
        if b[0] <= c[0]:
            D.append(b)
            B.remove(b)
        else:
            D.append(c)
            C.remove(c)
	# add remainder in B or C to new array. they are greater anyway.
    D.extend(B)
    D.extend(C)
    return D
    

n = int(raw_input().split()[0])
x, y = [], []
P = list()
for i in range (0, n):
    data = raw_input().split()
    x.append(int(data[0]))
    y.append(int(data[1]))
    P.append([x[i], y[i]])

# sort by X coordinate
P_sorted = MergeSort_x(P)    
    
print("{0:.4f}".format(minimum_distance(P_sorted)))