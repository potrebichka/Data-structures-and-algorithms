# python2

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
    while used_rows[pivot_element.row] or a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.row += 1
        if pivot_element.row >= len(a):
            used_columns.append(pivot_element_column)
            return (self.SelectPivotElement(a, used_rows, used_columns), used_columns)
        
    return pivot_element, used_columns

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    coeff = a[pivot_element.row][pivot_element.column]
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
        pivot_element, used_columns = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)