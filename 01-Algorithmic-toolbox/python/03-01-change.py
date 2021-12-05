#python3
#The goal in this problem is to find the minimum number of coins needed to change the input value
#(an integer) into coins with denominations 1, 5, and 10.

def get_change(m):
    #array of values of possible coins
    coins = [10, 5, 1]
    #result's list
    count = 0

    while m > 0:
        for coin in coins:
            count += number//coin;
            m = m % coin;
    return count

#m = int(raw_input("Input the value of money to change in coins 1<=m<=10^3: "))
m = int(input())
print(get_change(m))