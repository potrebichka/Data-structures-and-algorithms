# Uses python3
n = int(input("Enter n "))
a = [int(x) for x in input("Enter numbers ").split()]
assert(len(a) == n)

result = 0
# Find the first and second maximum number in array
if n <= 1:
    print(result)
else:
    max1 = a[0] if a[0] > a[1] else a[1]
    max2 = a[1] if a[0] > a[1] else a[0]
    for i in range(2, n):
        if 	a[i] > max1:
            max1, max2 = a[i], max1
        elif a[i] > max2 and a[i] <= max1:
            max2 = a[i]

# the result is the multiplication of these numbers
result = max1*max2

print(result)
