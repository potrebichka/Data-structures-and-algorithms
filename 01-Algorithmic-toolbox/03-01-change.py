#python3
#The goal in this problem is to find the minimum number of coins needed to change the input value
#(an integer) into coins with denominations 1, 5, and 10.

def get_change(m):
    #array of values of possible coins
    coins = [10, 5, 1]
    #result's list
    count = 0
    for i in len(0, len(coins)):
        if m == 0:
            return count
	    count += number/coins[i];
		m = m % coins[i];
    return count

#m = int(raw_input("Input the value of money to change in coins 1<=m<=10^3: "))
m = int(input())
print(get_change(m))