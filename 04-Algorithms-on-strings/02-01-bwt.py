# python2
import sys

def BWT(text):
    rotations = []
    rotation_text = text
    for i in range(len(text)):
        rotations.append(rotation_text)
        rotation_text = rotation_text[-1] + rotation_text[:-1]
    rotations.sort()
    result = ""
    for rotation_text in rotations:
        result += rotation_text[-1]
    return result

if __name__ == '__main__':
    text = raw_input()
    print(BWT(text))