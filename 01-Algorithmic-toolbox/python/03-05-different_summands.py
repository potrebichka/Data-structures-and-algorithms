#python2
#import sys

#You are organizing a funny competition for children. As a prize fund you have n
#candies. You would like to use these candies for top k places in a competition
#with a natural restriction that a higher place gets a larger number of candies.
#To make as many children happy as possible, you are going to find the largest
#value of k for which it is possible.


def optimal_summands(n):
    summands = []
    #write your code here
    k = n
    l = 1
    while True:
        if k <= 2*l:
            summands.append (l)
            break
        else:
            k = k - l
            l += 1
    summands.append( list())
    acc = 0
    for i in range(1, l+1):
        if i == l:
            summands[1].append(n-acc)
        else:
            summands[1].append (i)
            acc += i
    return summands

#if __name__ == '__main__':
#    input = sys.stdin.read()
#    n = int(input)
n = int(raw_input())
#n = int(raw_input("Enter number n of candies: "))
summands = optimal_summands(n)
for x in summands:
#     print(x, end=' ')
      print x