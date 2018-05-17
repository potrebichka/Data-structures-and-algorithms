#python2
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check_brackets(text):
    opening_brackets_stack = []
      
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            # add new opening brack to the stack
            new_bracket = Bracket(next, i)
            opening_brackets_stack.append(new_bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            # check if stack is empty, then we find the answer
            if len(opening_brackets_stack) == 0:
                return i+1
            # last element in list
            top = opening_brackets_stack.pop()
            # matching the last element and next element. If not - we have an answer
            if not top.Match(next):
                return i+1
    # Printing answer, write your code here
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        return opening_brackets_stack[0].position+1
    
text = raw_input()
print check_brackets(text)
