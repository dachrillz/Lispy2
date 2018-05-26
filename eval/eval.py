
import sys
sys.path.append('../parser')
import lisp_parser
from collections import deque

class simple_stack():
    def __init__(self):
        self.stack = deque()


    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.popleft()

    def __repr__(self):
        return ("repr of stack: " + str(self.stack))


parser_instance = lisp_parser.get_parser()
    
stack_instance = simple_stack()

def evaluate(input_):
    '''
    Iterate through abstract syntax tree and evalute the leaves.
    '''

    value_of_parsed_result = input_[1]
    if type(value_of_parsed_result) == list:
        if len(value_of_parsed_result) > 1:
            for item in reversed(value_of_parsed_result):
                if item[0] == 'sym':
                    #here we do lookups and call appropriate methods from the environment
                    stack_instance.push(item[1])
                elif item[0] == 'int':
                    stack_instance.push(item[1])
                elif item[0] == 'list':
                    evaluate(item)

    return parsed_result




if __name__ == '__main__':
    #to_be_parsed = input("Type something to evalute >> ")
    to_be_parsed = '(+ (+ 1 2) 3)'
    try:
        temp = to_be_parsed
        to_be_parsed = int(to_be_parsed)
    except:
        to_be_parsed = temp

    parsed_result = parser_instance.parse(to_be_parsed)

    evaluate(parsed_result)

    print(stack_instance)
