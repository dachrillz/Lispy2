#import lexer
import ply.yacc as yacc

from lexer import tokens


#Parsing rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


#dictionary of names
names = {}

def p_statement_assign(t):
    'statement : id EQUAL expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression '''
    if t[2]   == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]


#ClassDeclaration 	::= 	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"
def p_class_declaration(t):
    'class_declaration : CLASS id'
    #STOPPED HERE


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_name(t): 
    'expression : id' 
    try:
        t[0] = names[t[1]] 
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0 
        
def p_error(t):
    print("Syntax error at '%s'" % t.value)



parser_instance = yacc.yacc()


if __name__ == '__main__':
    
    sample_program = """
    class Factorial {
        public static void main(String[] a){
            System.out.println(new Fac().ComputeFac(10));
        }
    }

    class Fac {
        public int ComputeFac(int num){
            in num_aux;
            if (num < 1)
                num_aux = 1;
            else
                num_aux = num * (this.ComputeFac(num-1));
            return num_aux;
        }
    }
    """

    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break

        if not s: continue

        if s == 'sample':
            s = sample_program

        result = parser_instance.parse(s)


