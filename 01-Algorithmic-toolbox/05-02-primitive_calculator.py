#python2
# You are given a primitive calculator that can perform the following three operations with the current number
#x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a positive integer n, find the
#minimum number of operations needed to obtain the number n starting from the number 1.

def dynamic_sequence(n):
    sequence_operations, MinNum, sequence = [], [], [] 
    MinNum.append(0)
    MinNum.append(0)
    if n == 1:
        return 0, [1]
    sequence_operations.append(0)
    sequence_operations.append(0)
    for i in range(2, n+1):
        MinNum.append(10**9)
        sequence_operations.append(0)
    for i in range(2,n+1):
        NumOp1, NumOp2, NumOp3, NumOp = 10**9, 10**9, 10**9, 10**9
        if i % 3 == 0:
            NumOp1 = MinNum[i/3]+1
        if i % 2 == 0:
            NumOp2 = MinNum[i/2]+1
        NumOp3 = MinNum[i-1] +1
        NumOp = min(NumOp1, NumOp2, NumOp3)
        if NumOp < MinNum[i]:
            MinNum[i] = NumOp
        if NumOp == NumOp1:
            sequence_operations[i] = 1
        elif NumOp == NumOp2:
            sequence_operations[i] = 2
        elif NumOp == NumOp3:
            sequence_operations[i] = 3
    k = n
    while True:
        sequence.append(k)
        if k == 1:
            break
        if sequence_operations[k] == 1:
            k = k / 3
        elif sequence_operations[k] == 2:
            k = k /2
        elif sequence_operations[k] == 3:
            k = k - 1
    return MinNum[n], reversed(sequence)

n = int(raw_input())
Num, sequence = dynamic_sequence(n)
print Num 
for x in sequence:
    print x,