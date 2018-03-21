# Uses python3

def calc_fib(n):
    F = list()
    F.append(0)
    F.append(1)
    for i in range(2, n+1):
	    F.append(F[i-1]+F[i-2])
    return F[n]

n = int(input())
print(calc_fib(n))
