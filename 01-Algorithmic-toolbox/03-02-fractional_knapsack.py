#python3
# A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
#of items assuming that any fraction of a loot item can be put into his bag.


# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    W = capacity
    n = len(weights)
    v_w = list()
    
    # calculate ratio of values to weights
    for i in range(0,n):
        v_w.append(values[i]/weights[i])
        
    #arrange sorted lists of weights and values
    for _ in range(0, n):
        i = v_w.index(max(v_w))

        if W == 0:
		    return value
        a = min(weights[i], W)
		value = value + a * values[i]/weights[i]
		W = W - a
		v_w.pop(i)
		weights.pop(i)
		values.pop(i)
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

# Input Format. The first line of the input contains the number n of items and the capacity W of a knapsack.
#The next n lines define the values and weights of the items. The i-th line contains integers vi and wi - the value
#value and the weight of i-th item, respectively.
#Constraints. 1 <= n <= 103, 0 <= W <= 2 * 10^6 ; 0 <= vi <= 2 * 10^6, 0 < wi <= 2 * 10^6
# for all 1 <= i <= n. All the numbers are integers.

'''
n, capacity = raw_input("Enter number n of items and capasity W of a knapsack: ").split()
i=0
n, capacity = int(n), int(capacity)
values = list()
weights = list()
while i < n:
    input = raw_input("Enter the values and weights of the items(one combination on each line: ")
    values.append(float(input.split()[0]))
    weights.append(int(input.split()[1]))
    i += 1

opt_value = get_optimal_value(capacity, weights, values)
print("{:.4f}".format(opt_value))'''