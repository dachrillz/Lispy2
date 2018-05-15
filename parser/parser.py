#import lexer
import ply.yacc as yacc

from lexer import tokens



'''
GRAMMAR OF THE LISP!

Program	the start of input, an Operator, one or more Expression, and the end of input.
Expression	: Number | '(' Operator Expression+ ')'.
Operator :	'+' | '-' | '*' | '/'
Number : -?[0-9]+
'''

#Parsing rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


#dictionary of names
names = {}



def p_expr(t):
    '''expression : LPAREN PLUS explist RPAREN
                  | LPAREN MINUS explist RPAREN
                  | LPAREN TIMES explist RPAREN
                  | LPAREN DIVIDE explist RPAREN 
                  '''
    AST_local = []
    t[0] = t[:]


def p_expr_list(t):
    ''' explist : expression
                | explist expression
    '''
    if len(t) < 3:
        t[0] = ('list', [t[1]])
    else:
        t[1][1].append(t[2])
        t[0] = t[1]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]
        
def p_error(t):
    print("Syntax error at '%s'" % t)



parser_instance = yacc.yacc()


if __name__ == '__main__':

    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break

        if not s: continue

        result = parser_instance.parse(s)

        print(result)



