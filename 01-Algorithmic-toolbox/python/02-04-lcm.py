def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

#Find the greatest common divisor
def GCD(a, b):
    if b == 0:
        return a
    a_prime = (a % b)
    return GCD(b, a_prime)

# Find the least common multiple using formula with GCD	
def lcm(a,b):
    return a * b / GCD(a,b)	
	
input = raw_input()
a, b = map(int, input.split())
print(lcm(a, b))
