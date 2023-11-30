
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BEGIN COLON COMMA DIVIDE DO DOT ELSE END GREATER GREATER_EQUAL IDENTIFIER IF INTEGER LESS LESS_EQUAL LPAREN MINUS NUMBER PLUS PROGRAM READ REAL RPAREN SEMICOLON THEN TIMES VAR WHILE WRITEprogram : PROGRAM IDENTIFIER SEMICOLON declaration_list compound_statement DOTdeclaration_list : declaration_list declaration \n                        | emptydeclaration : VAR variable_list COLON type SEMICOLONvariable_list : variable_list COMMA IDENTIFIER\n                     | IDENTIFIERtype : INTEGER\n          | REALcompound_statement : BEGIN statement_list ENDstatement_list : statement_list SEMICOLON statement\n                    | statementstatement : assignment_statement\n                | if_statement\n                | while_statement\n                | read_statement\n                | write_statement assignment_statement : IDENTIFIER ASSIGN expressionif_statement : IF expression THEN statement\n                    | IF expression THEN statement ELSE statementwhile_statement : WHILE expression DO statementread_statement : READ IDENTIFIERwrite_statement : WRITE expressionrelational_expression : expression GREATER expression\n                             | expression LESS expression\n                             | expression GREATER_EQUAL expression\n                             | expression LESS_EQUAL expressionexpression : relational_expression\n                  | expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : NUMBER\n              | IDENTIFIERempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,11,],[0,-1,]),'IDENTIFIER':([2,9,10,20,21,22,23,27,28,39,42,43,44,45,46,47,48,49,50,51,67,],[3,19,25,34,34,36,34,19,34,55,19,34,34,34,34,34,34,34,34,19,19,]),'SEMICOLON':([3,12,13,14,15,16,17,18,30,31,32,33,34,36,37,40,41,52,53,54,56,57,58,59,60,61,62,63,64,65,68,],[4,27,-11,-12,-13,-14,-15,-16,-27,-30,-33,-34,-35,-21,-22,-10,-17,66,-7,-8,-18,-28,-29,-23,-24,-25,-26,-31,-32,-20,-19,]),'BEGIN':([4,5,6,8,66,],[-36,9,-3,-2,-4,]),'VAR':([4,5,6,8,66,],[-36,10,-3,-2,-4,]),'DOT':([7,26,],[11,-9,]),'IF':([9,27,42,51,67,],[20,20,20,20,20,]),'WHILE':([9,27,42,51,67,],[21,21,21,21,21,]),'READ':([9,27,42,51,67,],[22,22,22,22,22,]),'WRITE':([9,27,42,51,67,],[23,23,23,23,23,]),'END':([12,13,14,15,16,17,18,30,31,32,33,34,36,37,40,41,56,57,58,59,60,61,62,63,64,65,68,],[26,-11,-12,-13,-14,-15,-16,-27,-30,-33,-34,-35,-21,-22,-10,-17,-18,-28,-29,-23,-24,-25,-26,-31,-32,-20,-19,]),'ELSE':([14,15,16,17,18,30,31,32,33,34,36,37,41,56,57,58,59,60,61,62,63,64,65,68,],[-12,-13,-14,-15,-16,-27,-30,-33,-34,-35,-21,-22,-17,67,-28,-29,-23,-24,-25,-26,-31,-32,-20,-19,]),'ASSIGN':([19,],[28,]),'NUMBER':([20,21,23,28,43,44,45,46,47,48,49,50,],[33,33,33,33,33,33,33,33,33,33,33,33,]),'COLON':([24,25,55,],[38,-6,-5,]),'COMMA':([24,25,55,],[39,-6,-5,]),'THEN':([29,30,31,32,33,34,57,58,59,60,61,62,63,64,],[42,-27,-30,-33,-34,-35,-28,-29,-23,-24,-25,-26,-31,-32,]),'PLUS':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[43,-27,-30,-33,-34,-35,43,43,43,-28,-29,43,43,43,43,-31,-32,]),'MINUS':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[44,-27,-30,-33,-34,-35,44,44,44,-28,-29,44,44,44,44,-31,-32,]),'GREATER':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[45,-27,-30,-33,-34,-35,45,45,45,-28,-29,45,45,45,45,-31,-32,]),'LESS':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[46,-27,-30,-33,-34,-35,46,46,46,-28,-29,46,46,46,46,-31,-32,]),'GREATER_EQUAL':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[47,-27,-30,-33,-34,-35,47,47,47,-28,-29,47,47,47,47,-31,-32,]),'LESS_EQUAL':([29,30,31,32,33,34,35,37,41,57,58,59,60,61,62,63,64,],[48,-27,-30,-33,-34,-35,48,48,48,-28,-29,48,48,48,48,-31,-32,]),'DO':([30,31,32,33,34,35,57,58,59,60,61,62,63,64,],[-27,-30,-33,-34,-35,51,-28,-29,-23,-24,-25,-26,-31,-32,]),'TIMES':([31,32,33,34,57,58,63,64,],[49,-33,-34,-35,49,49,-31,-32,]),'DIVIDE':([31,32,33,34,57,58,63,64,],[50,-33,-34,-35,50,50,-31,-32,]),'INTEGER':([38,],[53,]),'REAL':([38,],[54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([4,],[5,]),'empty':([4,],[6,]),'compound_statement':([5,],[7,]),'declaration':([5,],[8,]),'statement_list':([9,],[12,]),'statement':([9,27,42,51,67,],[13,40,56,65,68,]),'assignment_statement':([9,27,42,51,67,],[14,14,14,14,14,]),'if_statement':([9,27,42,51,67,],[15,15,15,15,15,]),'while_statement':([9,27,42,51,67,],[16,16,16,16,16,]),'read_statement':([9,27,42,51,67,],[17,17,17,17,17,]),'write_statement':([9,27,42,51,67,],[18,18,18,18,18,]),'variable_list':([10,],[24,]),'expression':([20,21,23,28,45,46,47,48,],[29,35,37,41,59,60,61,62,]),'relational_expression':([20,21,23,28,45,46,47,48,],[30,30,30,30,30,30,30,30,]),'term':([20,21,23,28,43,44,45,46,47,48,],[31,31,31,31,57,58,31,31,31,31,]),'factor':([20,21,23,28,43,44,45,46,47,48,49,50,],[32,32,32,32,32,32,32,32,32,32,63,64,]),'type':([38,],[52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENTIFIER SEMICOLON declaration_list compound_statement DOT','program',6,'p_program','parser.py',15),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',20),
  ('declaration_list -> empty','declaration_list',1,'p_declaration_list','parser.py',21),
  ('declaration -> VAR variable_list COLON type SEMICOLON','declaration',5,'p_declaration','parser.py',29),
  ('variable_list -> variable_list COMMA IDENTIFIER','variable_list',3,'p_variable_list','parser.py',37),
  ('variable_list -> IDENTIFIER','variable_list',1,'p_variable_list','parser.py',38),
  ('type -> INTEGER','type',1,'p_type','parser.py',46),
  ('type -> REAL','type',1,'p_type','parser.py',47),
  ('compound_statement -> BEGIN statement_list END','compound_statement',3,'p_compound_statement','parser.py',52),
  ('statement_list -> statement_list SEMICOLON statement','statement_list',3,'p_statement_list','parser.py',59),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',60),
  ('statement -> assignment_statement','statement',1,'p_statement','parser.py',68),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',69),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',70),
  ('statement -> read_statement','statement',1,'p_statement','parser.py',71),
  ('statement -> write_statement','statement',1,'p_statement','parser.py',72),
  ('assignment_statement -> IDENTIFIER ASSIGN expression','assignment_statement',3,'p_assignment_statement','parser.py',77),
  ('if_statement -> IF expression THEN statement','if_statement',4,'p_if_statement','parser.py',105),
  ('if_statement -> IF expression THEN statement ELSE statement','if_statement',6,'p_if_statement','parser.py',106),
  ('while_statement -> WHILE expression DO statement','while_statement',4,'p_while_statement','parser.py',114),
  ('read_statement -> READ IDENTIFIER','read_statement',2,'p_read_statement','parser.py',119),
  ('write_statement -> WRITE expression','write_statement',2,'p_write_statement','parser.py',124),
  ('relational_expression -> expression GREATER expression','relational_expression',3,'p_relational_expression','parser.py',129),
  ('relational_expression -> expression LESS expression','relational_expression',3,'p_relational_expression','parser.py',130),
  ('relational_expression -> expression GREATER_EQUAL expression','relational_expression',3,'p_relational_expression','parser.py',131),
  ('relational_expression -> expression LESS_EQUAL expression','relational_expression',3,'p_relational_expression','parser.py',132),
  ('expression -> relational_expression','expression',1,'p_expression','parser.py',138),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser.py',139),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser.py',140),
  ('expression -> term','expression',1,'p_expression','parser.py',141),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',149),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',150),
  ('term -> factor','term',1,'p_term','parser.py',151),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',160),
  ('factor -> IDENTIFIER','factor',1,'p_factor','parser.py',161),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',170),
]
