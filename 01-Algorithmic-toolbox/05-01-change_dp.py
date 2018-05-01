# Uses python2

def get_change(money):
    #write your code here
    coins = [1, 3, 4]
    MinNumCoins = list()
    MinNumCoins.append(0)
    for m in range(1, money+1):
        MinNumCoins.append(10 ** 9)
        for i in range(0, len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m-coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

m = int(raw_input());
print(get_change(m))