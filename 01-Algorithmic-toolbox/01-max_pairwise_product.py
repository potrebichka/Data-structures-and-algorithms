# Uses python3
n = int(input("Enter n "))
a = [int(x) for x in input("Enter numbers ").split()]
assert(len(a) == n)

result = 0
# Find the first and second maximum number in array
max_index1 = -1
max_index2 = -1
for i in range(0, n):
    if (max_index1 == -1 ) or (a[i] > a[max_index1]):
	    max_index1 = i
    if (i != max_index1) and ((max_index2 == -1) or (a[i] > a[max_index2])):
	    max_index2 = i		

# the result is the multiplication of these numbers
result = a[max_index1]*a[max_index2]

print(result)
