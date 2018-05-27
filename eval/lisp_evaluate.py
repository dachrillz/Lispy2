import sys
sys.path.append('../parser')
sys.path.append('../environment')
import lisp_parser
import lisp_environment
    
def evaluate(input_, env):
    '''
    Iterate through abstract syntax tree and evalute the leaves.
    '''
    value_of_parsed_result = input_[1]

    if type(value_of_parsed_result) == list:
        arguments = []

        for item in value_of_parsed_result:
            if item[0] == 'sym':
                #here we do lookups and call appropriate methods from the environment
                if item[1] == 'def!':
                    symbol_to_be_bound = value_of_parsed_result[1][1]
                    to_be_evaluated = value_of_parsed_result[2:][0]
                    env[symbol_to_be_bound] = evaluate(to_be_evaluated,env)
                else:
                    try:
                        bound_function = env[item[1]]
                    except:
                        bound_function = ".*\'%s\' not found.*" %str(item[1])
                        break

            elif item[0] == 'int':
                arguments.append(item[1])
            elif item[0] == 'list':
                arguments.append(evaluate(item,env))

        if callable(bound_function): #use this for error handling for now...
            result = bound_function(arguments)
        else:
            result = bound_function

    elif input_[1] == '()':
        return '()'

    elif input_[0] == 'int':
        return input_[1]

    elif input_[0] == 'sym':
        try:
            result = env[input_[1]]
        except:
            result = ".*\'%s\' not found.*" %str(input_[1])   

    return result




if __name__ == '__main__':
    parser_instance = lisp_parser.get_parser()
    #to_be_parsed = input("Type something to evalute >> ")
    to_be_parsed = '(+ (+ 1 2) 3)'
    #to_be_parsed = '(+ 2 3)'
    to_be_parsed = "(/ (- (+ 515 (* -87 311)) 296) 27)"
    to_be_parsed = "(def! x 3)"
    to_be_parsed = "(def! x (+ 3 2))"
    #to_be_parsed = "(- (+ 515 (* 87 311)) 296)"
    #to_be_parsed = '(* 87 311)'
    #to_be_parsed = '(- (+ 515 (* 87 311) 296) 1)'
    try:
        temp = to_be_parsed
        to_be_parsed = int(to_be_parsed)
    except:
        to_be_parsed = temp

    parsed_result = parser_instance.parse(to_be_parsed)

    env = lisp_environment.get_environment()

    result = evaluate(parsed_result, env)
    print(result)

    to_be_parsed = 'x'
    parsed_result = parser_instance.parse(to_be_parsed)

    result = evaluate(parsed_result,env)

    print(result)