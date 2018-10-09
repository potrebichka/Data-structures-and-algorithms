# python2
import sys

def InverseBWT(bwt):
    # write your code here
    # convert string into list
    bwt = list(bwt)
    # add counters
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for i in range(len(bwt)):
        if bwt[i] == 'A':
            count_A += 1
            bwt[i] = bwt[i] + str(count_A).zfill(6)
        elif bwt[i] == 'C':
            count_C += 1
            bwt[i] = bwt[i] + str(count_C).zfill(6)
        elif bwt[i] == 'G':
            count_G += 1
            bwt[i] = bwt[i] + str(count_G).zfill(6)
        elif bwt[i] == 'T':
            count_T += 1
            bwt[i] = bwt[i] + str(count_T).zfill(6)
    # sort list
    bwt_sorted = list(bwt)
    bwt_sorted.sort()

    # form a dictionary
    
    bwt_dict = {}
    for i in range(len(bwt)):
        bwt_dict[bwt[i]] = bwt_sorted[i]
    result = ''
    result2 = ''
    symbol = '$'
    for i in range(len(bwt)):
        symbol = bwt_dict[symbol]
        result += symbol[0]
    return result


if __name__ == '__main__':
    bwt = raw_input()
    print(InverseBWT(bwt))