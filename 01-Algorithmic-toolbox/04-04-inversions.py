#python2
#import sys
#An inversion of a sequence a0, a1 ... an-1 is a pair of indices 0 <= i < j < n such
#that ai > aj . The number of inversions of a sequence in some sense measures how
#close the sequence is to being sorted. For example, a sorted (in non-descending
#order) sequence contains no inversions at all, while in a sequence sorted in descending
#order any two elements constitute an inversion (for a total of n*(n-1)/2
#inversions).

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
	# array of length 1 is sorted
    if right - left <= 1:
        return a, 0
	# find the middle of array
    ave = (left + right) // 2
	# divide array into two parts and call recursively each part 
    B, number1 = get_number_of_inversions(a[0:ave-left], 0, ave-left)
    C, number2 = get_number_of_inversions(a[ave-left:right-left], ave-left, right-left)
	# merge two parts
    sorted_array, number_of_inversions = Merge(B, C)
	# whole number of inversions is the sum of inversions of parts
    number_of_inversions += number1+number2
    return sorted_array, number_of_inversions

def Merge(B, C):
    # merge two sorted arrays
    D = []
    j = 0
	# while there are elements in both arrays
    while (not (B == [])) and (not (C == [])):
	    # choose first elements of arrays
        b = B[0]
        c = C[0]
		# if element of first array B is less than element from second array C
		# add this element to new array D and remove from B
        if b <= c:
            D.append(b)
            B.remove(b)
		# otherwise append element from second array C to new array D.
		# number of inversions will increase on length of first array B 
        else:
            D.append(c)
            C.remove(c)
            j+=len(B)
	# Add remainder of array B or C to new array D. They are greater than other numbers.
    D.extend(B)
    D.extend(C)
    return D, j

#if __name__ == '__main__':
n = int(raw_input().split()[0])
a = raw_input().split()
for i in range(0, n):
    a[i] = int(a[i]) 
b = n * [0]
print(get_number_of_inversions(a, 0, len(a)))[1]