def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

#Euclidean algorithm is efficient way of computing great common divisor
def EuclidGCD(a, b):
    if b == 0:
        return a
    a_prime = (a % b)
    return EuclidGCD(b, a_prime)
	
input = raw_input()
a, b = map(int, input.split())
print(EuclidGCD(a, b))
