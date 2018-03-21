#python3
def fibonacci_partial_sum_naive(from_, to):
#finding the last digit of a partial sum of Fibonacci numbers: Fm + Fm+1 + ... + Fn.
    if to <= 1:
        return to

    previous = 0
    current  = 1


    if k_to >= k_from:
        for _ in range(k_from - 1):
            previous, current = current, (previous + current)
        sum = current

        for _ in range(k_to - k_from):
            previous, current = current, previous + current
            sum += current

    return sum % 10

# Using pisano period 
def fibonacci_partial_sum(from_, to):
#finding the last digit of a partial sum of Fibonacci numbers: Fm + Fm+1 + · · · + Fn.
    if to <= 1:
        return to

    previous = 0
    current  = 1
    # for modulo = 10
    pisano_number = 60
    # new variables
    k_from = from_ % pisano_number
    k_to = to % pisano_number
    if k_to >= k_from:
        F_from = 0
        F_from_2 = 0
        for _ in range(to+1):
            previous, current = current, (previous + current)%10
            if _ == from_ -2:
                F_from = current%10
            if _ == from_:
                F_from_2 = current%10
        return (current%10 - F_from_2 + F_from)

inp = input()
from_, to = map(int, inp.split())
print(fibonacci_partial_sum(from_, to))
