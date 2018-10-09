# python2
import sys

letters = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}

def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
        * starts - for each character C in bwt, starts[C] is the first position 
            of this character in the sorted array of 
            all characters of the text.
        * occ_count_before - for each character C in bwt and each position P in bwt,
            occ_count_before[C][P] is the number of occurrences of character C in bwt
            from position 0 to position P inclusive.
     """
    # Implement this function yourself
    bwt = list(bwt)
    bwt_sorted = list(bwt)
    bwt_sorted.sort()
    starts = {}
    # first occurence of symbol in first column
    for i in range(len(bwt_sorted)):
        if bwt_sorted[i] in starts:
            continue
        else:
            starts[bwt_sorted[i]] = i
    occ_count_before = [[0 for x in range(len(bwt)+1)] for y in range(5)] 
    count_0 = 0
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for j in range(len(bwt)):
        if bwt[j] == '$':
            count_0 += 1
            occ_count_before[0][j+1] = count_0
        else:
            occ_count_before[0][j+1] = count_0
        if bwt[j] == 'A':
            count_A += 1
            occ_count_before[1][j+1] = count_A
        else:
            occ_count_before[1][j+1] = count_A
        if bwt[j] == 'C':
            count_C += 1
            occ_count_before[2][j+1] = count_C
        else:
            occ_count_before[2][j+1] = count_C
        if bwt[j] == 'G':
            count_G += 1
            occ_count_before[3][j+1] = count_G
        else:
            occ_count_before[3][j+1] = count_G
        if bwt[j] == 'T':
            count_T += 1
            occ_count_before[4][j+1] = count_T
        else:
            occ_count_before[4][j+1] = count_T
    return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    # Implement this function yourself
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if occ_counts_before[letters[symbol]][top] != occ_counts_before[letters[symbol]][bottom+1]:
                top = starts[symbol] + occ_counts_before[letters[symbol]][top]
                bottom = starts[symbol] + occ_counts_before[letters[symbol]][bottom+1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
     
     


if __name__ == '__main__':
    bwt = raw_input()
    pattern_count = int(raw_input())
    patterns = raw_input().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
