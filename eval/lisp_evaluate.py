
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

    def is_not_empty(self):
        return len(self.stack) != 0



parser_instance = lisp_parser.get_parser()
    
stack_instance = simple_stack()

def evaluate(input_, env):
    '''
    Iterate through abstract syntax tree and evalute the leaves.
    '''
    value_of_parsed_result = input_[1]

    if type(value_of_parsed_result) == list:
        if len(value_of_parsed_result) > 1:
            
            arguments = []

            for item in value_of_parsed_result:
                if item[0] == 'sym':
                    #here we do lookups and call appropriate methods from the environment
                    try:
                        bound_function = env[item[1]] #@TODO: should probably do some error handling as well
                        stack_instance.push(bound_function)
                    except:
                        bound_function = ".*\'abc\' not found.*"
                        break
                elif item[0] == 'int':
                    stack_instance.push(item[1])
                    arguments.append(item[1])
                elif item[0] == 'list':
                    stack_instance.push('|')
                    arguments.append(evaluate(item,env))
                    stack_instance.push('|')

            if callable(bound_function): #use this for error handling for now...
                result = bound_function(arguments)
            else:
                result = bound_function

    elif input_[1] == '()':
        return '()'

    elif input_[0] == 'int':
        return input_[1]
    

    return result




if __name__ == '__main__':
    #to_be_parsed = input("Type something to evalute >> ")
    to_be_parsed = '(+ (+ 1 2) 3)'
    #to_be_parsed = '(+ 2 3)'
    to_be_parsed = "(/ (- (+ 515 (* -87 311)) 296) 27)"
    #to_be_parsed = "(- (+ 515 (* 87 311)) 296)"
    #to_be_parsed = '(* 87 311)'
    #to_be_parsed = '(- (+ 515 (* 87 311) 296) 1)'
    try:
        temp = to_be_parsed
        to_be_parsed = int(to_be_parsed)
    except:
        to_be_parsed = temp

    #parsed_result = parser_instance.parse(to_be_parsed)

    def simple_addition(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = 0
        for item in arg:
            result += item
        return result


    def simple_subtraction(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = arg[0]
        for i in range(1, len(arg)):
            result -= arg[i]
        return result


    
    def simple_multiplication(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = 1
        for item in arg:
            result *= item
        return result


    
    def simple_division(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = arg[0]
        for i in range(1, len(arg)):
            result /= arg[i]
        return result


    env = {'+' : simple_addition, '-': simple_subtraction, '*': simple_multiplication,'/': simple_division}

    result = evaluate(parsed_result, env)

    print(result)

'''
    while stack_instance.is_not_empty():
        res = stack_instance.pop()
        if res == '|':
            
            print(res)'''