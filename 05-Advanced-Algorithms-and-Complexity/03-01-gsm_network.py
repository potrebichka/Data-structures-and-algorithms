### python2
import itertools, os
#import pycosat
#from subprocess import DEVNULL, STDOUT, check_call, call

n, m = map(int, raw_input().split())
edges = [ list(map(int, raw_input().split())) for i in range(m) ]
#print edges

clauses = []
digits_vertices = range(1, n+1)
digits_colors = range(1, 4)

def varnum(i, j):
    assert(i in digits_vertices and j in digits_colors)
    return 3*(i) + 1*j-3


def exactly_one_of_3(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 3):
        clauses.append([-pair[0], -pair[1]])
        clauses.append([-pair[1], -pair[2]])
        clauses.append([-pair[0], -pair[2]])
        
def exactly_one_of_2(literals):
    clauses.append([-l for l in literals])
    

# cell [i] contains exactly one color
for (i) in digits_vertices:
    exactly_one_of_3([varnum(i, j) for j in digits_colors])

# edges has different color
for (i1, i2) in edges:
    for j in digits_colors:
        exactly_one_of_2([varnum(i1,j), varnum(i2,j)])

#print clauses
#answer = pycosat.solve(clauses)
#print answer
# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print len(clauses), n*3
    for clause in clauses:
        for var in clause:
            print var,
        print 0

printEquisatisfiableSatFormula()