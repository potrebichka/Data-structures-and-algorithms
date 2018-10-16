# python2
import sys


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    # Implement this function yourself
    string = pattern + '$' + text
    # compute prefix function
    s = compute_prefix_function(string)
    result = []
    for i in range(len(pattern) + 1, len(s)):
        if s[i] == len(pattern):
            result.append(i - 2* len(pattern))
    return result

def compute_prefix_function(text):
    # array of integers of length of pattern
    s = [None] * len(text)
    # initialise start position
    s[0] = 0
    border = 0
    # go through text
    for i in range(1, len(text)):
        # decrease border if symbols don't match
        while border > 0 and text[i] != text[border]:
            border = s[border-1]
        # if match --> increase border
        if text[i] == text[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border
    return s
    

if __name__ == '__main__':
    pattern = raw_input().strip()
    text = raw_input().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
