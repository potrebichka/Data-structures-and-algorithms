#python2
# The edit distance between two strings is the minimum number of insertions, deletions, and mismatches in
#an alignment of two strings.

def edit_distance(s, t):
    #write your code here
    n = len(s)
    m = len(t) 
    #distance matrix for different lengths of s and t	
    D = [[0 for x in range(m+1)] for y in range(n+1)] 
    
	#initialize first row and first column equal length of string (length of s or t is 0)
    for j in range(1, m+1):
        for i in range(1, n+1):
            D[i][0] = i
            D[0][j] = j
	#compute distances for different lengths of s and t
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = D[i][j-1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[n][m]

#Each of the two lines of the input contains a string consisting of lower case latin letters.
#The length of both strings is at least 1 and at most 100.	

s = list(raw_input())
t = list(raw_input())
print(edit_distance(s, t))
