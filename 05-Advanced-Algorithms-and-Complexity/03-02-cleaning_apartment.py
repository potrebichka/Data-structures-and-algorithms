# python2
import itertools
n, m = map(int, raw_input().split())
edges = [ list(map(int, raw_input().split())) for i in range(m) ]

clauses = []
digits = range(1, n+1)

def varnum(i, j):
    assert(i in digits and j in digits)
    return n*(i) + j-n


def exactly_one_of(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

#all vertices is on the pass and only once
for i in digits:
    exactly_one_of([varnum(i,j) for j in digits])

#only one vertex at each position on the path
for j in digits:
    exactly_one_of([varnum(i,j) for i in digits])

#matrix for vertices:
matrix = []
for i1 in digits:
    for i2 in digits:
        if ([i1, i2] not in edges and [i2, i1] not in edges) and i1 != i2:
            matrix.append((i1, i2))
        
#connectivity
for (i1, i2) in matrix:
    for j in range(1, n):
        clauses.append([-varnum(i1, j), -varnum(i2, j+1)])
    
# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print len(clauses), n*n
    for clause in clauses:
        for var in clause:
            print var,
        print 0

printEquisatisfiableSatFormula()