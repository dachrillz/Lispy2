
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEBANG BOOLEAN CLASS DIVIDE DOT ELSE EQUAL EXTENDS FALSE GREATER IF INT LBRACE LBRACKET LESS LPAREN MAIN MINUS NEW NUMBER PLUS PUBLIC RBRACE RBRACKET RETURN RPAREN SEMI STATIC STRING THIS TIMES TRUE VOID WHILE idstatement : id EQUAL expressionstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression expression : LPAREN expression RPARENexpression : NUMBERexpression : id'
    
_lr_action_items = {'NUMBER':([0,1,8,9,10,11,12,],[3,3,3,3,3,3,3,]),'PLUS':([3,4,5,6,7,13,14,15,16,17,18,],[-8,8,-9,8,-9,-7,-3,-6,-4,-5,8,]),'MINUS':([3,4,5,6,7,13,14,15,16,17,18,],[-8,10,-9,10,-9,-7,-3,-6,-4,-5,10,]),'id':([0,1,8,9,10,11,12,],[5,7,7,7,7,7,7,]),'RPAREN':([3,6,7,13,14,15,16,17,],[-8,13,-9,-7,-3,-6,-4,-5,]),'DIVIDE':([3,4,5,6,7,13,14,15,16,17,18,],[-8,9,-9,9,-9,-7,9,-6,9,-5,9,]),'$end':([2,3,4,5,7,13,14,15,16,17,18,],[0,-8,-2,-9,-9,-7,-3,-6,-4,-5,-1,]),'TIMES':([3,4,5,6,7,13,14,15,16,17,18,],[-8,11,-9,11,-9,-7,11,-6,11,-5,11,]),'LPAREN':([0,1,8,9,10,11,12,],[1,1,1,1,1,1,1,]),'EQUAL':([5,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,8,9,10,11,12,],[4,6,14,15,16,17,18,]),'statement':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> id EQUAL expression','statement',3,'p_statement_assign','parser.py',18),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',22),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',27),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',28),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',29),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',30),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',38),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',42),
  ('expression -> id','expression',1,'p_expression_name','parser.py',47),
]
