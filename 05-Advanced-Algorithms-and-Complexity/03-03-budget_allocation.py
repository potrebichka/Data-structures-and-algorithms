# python2
#import pycosat

n, m = list(map(int, raw_input().split()))
A = []
for i in range(n):
    A += [list(map(int, raw_input().split()))]
b = list(map(int, raw_input().split()))

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.

clauses = []
#digits = range(0, m)

#def varnum(i):
#    assert(i in digits)
#    return i

values_3 = [[0,0,0], [0,0,1],[0,1,0],[1,0,0],[0,1,1],[1,0,1],[1,1,0],[1,1,1]]
values_2 = [[0,0],[1,0],[0,1],[1,1]]
values_1 = [0,1]

for j,a in enumerate(A):
    not_zero_coef = []
    for i in range(len(a)):
        if a[i] != 0:
            not_zero_coef.append(i)
    assert(len(not_zero_coef) <= 3)
    
    if len(not_zero_coef) == 3:
        #calculate truth table
        for k in values_3:
            expression = 0
            expression += k[0]*a[not_zero_coef[0]]
            expression += k[1]*a[not_zero_coef[1]]
            expression += k[2]*a[not_zero_coef[2]]
            if expression > b[j]:
                current_clause = []
                for l in range(len(k)):
                    if k[l] == 0:
                        current_clause.append(not_zero_coef[l]+1)
                    else:
                        current_clause.append(-(not_zero_coef[l]+1))
                clauses.append(current_clause)
    elif len(not_zero_coef) == 2:
        for k in values_2:
            expression = 0
            expression += k[0]*a[not_zero_coef[0]]
            expression += k[1]*a[not_zero_coef[1]]
            if expression > b[j]:
                current_clause = []
                for l in range(len(k)):
                    if k[l] == 0:
                        current_clause.append(not_zero_coef[l]+1)
                    else:
                        current_clause.append(-(not_zero_coef[l]+1))
                clauses.append(current_clause)
    elif len(not_zero_coef) == 1:
        for k in values_1:
            expression = 0
            expression += k*a[not_zero_coef[0]]
            if expression > b[j]:
                current_clause = []
                if k == 0:
                    current_clause.append(not_zero_coef[0]+1)
                else:
                    current_clause.append(-(not_zero_coef[0]+1))
                clauses.append(current_clause)
    
#print clauses
def printEquisatisfiableSatFormula():
    if clauses != []:
        print len(clauses), m
        for clause in clauses:
            for var in clause:
                print var,
            print 0
    else:
        print("3 2")
        print("1 2 0")
        print("-1 -2 0")
        print("1 -2 0")
   

#answer = pycosat.solve(clauses)
#print answer        
        
printEquisatisfiableSatFormula()
