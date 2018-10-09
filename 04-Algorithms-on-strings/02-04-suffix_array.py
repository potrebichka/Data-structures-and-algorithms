# python2
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    result = []
    text_array = []
    current_text = text
    # Implement this function yourself
    for i in range(len(text)):
        text_array.append((current_text, i))
        current_text = current_text[1:]
    text_array.sort()
    for j in range(len(text_array)):
        result.append(text_array[j][1])
    return result


if __name__ == '__main__':
    text = raw_input()
    print(" ".join(map(str, build_suffix_array(text))))