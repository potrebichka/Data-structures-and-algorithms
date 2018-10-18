# python2
from sys import stdin
 
EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(raw_input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, raw_input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
        if pivot_element.column >= len(a[0]):
            return 'No solution', used_columns
    while used_rows[pivot_element.row] or a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.row += 1
        if pivot_element.row >= len(a):
            used_columns[pivot_element.column] = True
            return SelectPivotElement(a, used_rows, used_columns) 
    return pivot_element, used_columns

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    coeff = a[pivot_element.row][pivot_element.column]*1.0
    if coeff != 1:
        for i in range(len(a[pivot_element.row])):
            a[pivot_element.row][i] /= coeff
        b[pivot_element.row] /= coeff
    for i in range(len(a)):
        if i != pivot_element.row and a[i][pivot_element.column] != 0:
            coeff2 = a[i][pivot_element.column]
            for j in range(len(a[i])):
                a[i][j] -= coeff2*a[pivot_element.row][j]     
            b[i] -= coeff2*b[pivot_element.row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        (pivot_element, used_columns) = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element == 'No solution':
            return None
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b
 
def solve_diet_problem(n, m, A, b, c):  
    # Write your code here
    # add m inequalities for each ingredient to matrix A and B
    for i in range(m):
        temp = []
        for j in range(m):
            if i == j:
                temp.append(-1)
            else:
                temp.append(0)
        if temp not in A:
            A.append(temp)
            b.append(0)
    # making subsets of inequalities
    temp = []
    for i in range(m):
        temp.append(1)
    A.append(temp)
    b.append(10**9)
    k = m
    i = 1
    subset = set()
    while i <= k:
        subset_temp = set()
        # for start add subsets consisting only one inequality
        if i == 1:
            for j in range(len(A)):
                temp = (j,)
                subset_temp.add(temp)
        elif i == k:
            for j in range(len(A)):
                for element in subset:
                    temp = set(element)
                    temp.add(j)
                    temp = tuple(temp)
                    if len(temp) == k:
                        subset_temp.add(temp)
            subset = subset_temp
            break
        else:
            for j in range(len(A)):
                for element in subset:
                    temp = set(element)
                    temp.add(j)
                    temp = tuple(temp)
                    subset_temp.add(temp)
        subset = subset.union(subset_temp)
        i += 1
    
    full_set = set()
    for i in range(len(A)):
        full_set.add(i)
    
    solutions = []
    for current_tuple in subset:
        A_prime = []
        B_prime = []
        for element in current_tuple:
            A_prime.append(list(A[element]))
            B_prime.append(b[element])
        equation = Equation(A_prime, B_prime)
        solution = SolveEquation(equation)
        if solution == None:
            continue
        remaining_subset = full_set.difference(set(current_tuple))
        
        flag = True
        for element in remaining_subset:
            temp = 0
            for i in range(len(A[element])):
                temp += A[element][i]*solution[i]
            flag = flag & (temp <= b[element])
        if flag:
            pleasure = 0
            for i in range(len(solution)):
                pleasure += solution[i]*c[i]
            solutions.append((pleasure, solution))
            
    if solutions == []:
        return [-1, [0]*m]
    answer = max(solutions)
    max_solution = answer
    for solut in solutions:
        if solut != max_solution and solut[0] == max_solution[0]:
            for i in range(len(max_solution[1])):
                if max_solution[1][i] > 10**7 and solut[1][i]< 10**7:
                    max_solution = solut
                    break
    if max_solution == []:
        max_solution = answer
    if max_solution[0] != None:
        if any(element >= 10**7 for element in max_solution[1]):
            return [1, 0]
        return [0, max_solution[1]]
    return [0]


# number of restictions and number of available dishes
n, m = list(map(int, raw_input().split()))
# coefficients of the linear inequalities
A = []
for i in range(n):
    A += [list(map(int, raw_input().split()))]
# the right part of inequalities
b = list(map(int, raw_input().split()))
# expression for pleasure
c = list(map(int, raw_input().split()))
'''
n, m = int(input_.split()[0]), int(input_.split()[1])
A = []
for i in range(n):
    A += [list(map(int, (input_.split()[m*i+2:m*i+2+m])))]
# the right part of inequalities
b = list(map(int, (input_.split()[m*(n-1)+2+m: m*(n-1)+2+m+n])))
# expression for pleasure
c = list(map(int, input_.split()[m*(n-1)+2+m+n:]))
'''
anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:  
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
    