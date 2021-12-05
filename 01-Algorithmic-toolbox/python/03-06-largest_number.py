#python2

#As the last question of a successful interview, your boss gives you a few pieces of paper
#with numbers on it and asks you to compose a largest number from these numbers. The
#resulting number is going to be your salary, so you are very much interested in maximizing
#this number. How can you do this?
#Your goal in this problem is to tweak the above algorithm so that it works not only for single-digit
#numbers, but for arbitrary positive integers

#import sys

def IsGreaterOrEqual(digit, maxDigit):

    if digit // 100 > 0:
        if maxDigit // 100 > 0:
            if digit //100 < maxDigit//100:
                return False
            elif digit // 100 == maxDigit//100:
                IsGreaterOrEqual(digit % 100, maxDigit % 100)
            else:
                return True
        elif maxDigit // 10 > 0:
            if digit // 100 < maxDigit //10:
                return False
            elif digit // 100 == maxDigit // 10:
                IsGreaterOrEqual(digit % 100, maxDigit % 10)
            else:
                return True
        else:
            if digit //100 < maxDigit:
                return False
            elif digit // 100 == maxDigit:
                IsGreaterOrEqual(digit % 100, maxDigit)
            else:
                return True
    elif maxDigit // 100 > 0:
        return not IsGreaterOrEqual(maxDigit, digit)
                   
    if digit // 10 > 0:
        if maxDigit // 10 > 0:
            IsGreaterOrEqual(digit, maxDigit//10)
        else:
            if digit // 10 < maxDigit:
                return False
            elif digit // 10 == maxDigit:
                if digit % 10 >= maxDigit:
                    return True
                else:
                    return False
            else:
                return True
    elif maxDigit // 10 > 0:
        return not IsGreaterOrEqual(maxDigit, digit)
                    
    if digit >= maxDigit:
        return True
    else:
        return False

def largest_number(a):
    #write your code here
    res = ''
    while len(a) != 0:
        maxDigit = 0
        for digit in a:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res = res + str(maxDigit)
        a.remove(maxDigit)   
    return res
	
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = input.split()
#    a = data[1:]

n = int(raw_input())
a = list()
a = raw_input().split()
for i in range(0, n):
    a[i] = int(a[i])
print (largest_number(a))
    
