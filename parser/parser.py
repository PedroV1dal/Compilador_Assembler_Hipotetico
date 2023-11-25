import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lexer.lexer import tokens
from semantic.semantic import SemanticAnalyzer
from codegen.intermediary_code import IntermediaryCode
import ply.yacc as yacc

semantic_analyzer = SemanticAnalyzer()

#program structure
def p_program(p):
    'program : PROGRAM IDENTIFIER SEMICOLON declaration_list compound_statement DOT'
    p[0] = ('program', p[2], p[4], p[5])

# Declaration list
def p_declaration_list(p):
    '''declaration_list : declaration_list declaration 
                        | empty'''
    if len(p) == 3:
        p[0] = p[1] + (p[2],)
    else:
        p[0] = ()

# Declaration
def p_declaration(p):
    'declaration : VAR variable_list COLON type SEMICOLON'
    var_list = p[2]
    var_type = p[4]
    for var in var_list:
        semantic_analyzer.declare_var(var, var_type)
    p[0] = ('declaration', var_list, var_type)

def p_variable_list(p):
    '''variable_list : variable_list COMMA IDENTIFIER
                     | IDENTIFIER'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

#type
def p_type(p):
  '''type : INTEGER
          | REAL'''
  p[0] = p[1]

#compound statement
def p_compound_statement(p):
  'compound_statement : BEGIN statement_list END'
  p[0] = ('compound', p[2])

#statement list
def p_statement_list(p):
  '''statement_list : statement_list SEMICOLON statement
                    | statement'''
  if len(p) == 4:
    p[0] = p[1] + (p[2],)
  else:
    p[0] = (p[1],)

#statement
def p_statement(p):
  '''statement : assignment_statement
                | if_statement
                | while_statement
                | read_statement
                | write_statement '''
  p[0] = p[1]

#assignment statement
def p_assignment_statement(p):
    'assignment_statement : IDENTIFIER ASSIGN expression'
    var_name = p[1]
    var_type = semantic_analyzer.use_var(var_name)
    expr_type = get_expr_type(p[3])
    semantic_analyzer.check_type(var_type, expr_type, 'assignment')

    p[0] = ('assign', var_name, p[3])

def get_expr_type(expr):
    if isinstance(expr, tuple) and expr[0] == 'binop':
        left_type = get_expr_type(expr[1])
        right_type = get_expr_type(expr[3])
        if left_type != right_type:
            raise Exception(f"Type mismatch in expression: left is {left_type}, right is {right_type}")
        return left_type
    elif isinstance(expr, tuple) and expr[0] == 'number':
        return 'integer'
    elif isinstance(expr, tuple) and expr[0] == 'identifier':
        return semantic_analyzer.use_var(expr[1])
    elif isinstance(expr, int):
        return 'integer'
    else:
        raise Exception(f"Invalid expression type: {expr}")


#if statement
def p_if_statement(p):
    'if_statement : IF expression THEN statement'
    p[0] = ('if', p[2], p[4])

#while statement
def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    p[0] = ('while', p[2], p[4])

#read statement
def p_read_statement(p):
    'read_statement : READ IDENTIFIER'
    p[0] = ('read', p[2])

#write statement
def p_write_statement(p):
    'write_statement : WRITE expression'
    p[0] = ('write', p[2])

#expression
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        p[0] = ('binop', p[1], p[2], p[3])
    else:
        p[0] = p[1]

#term
def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binop', p[1], p[2], p[3])
    else:
        p[0] = p[1]

#factor

def p_factor(p):
    '''factor : NUMBER
              | IDENTIFIER'''
    p[0] = p[1]

#empty

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test it out
data = '''
    program testProgram;
    var x, y: integer;
    var z: integer;

    begin
        x := 10;
        y := 20;
        z := x + y - 5 * 3 / 2;

        if x > y then
            z := z + 1;
        else
            z := z - 1;

        while z <= 100 do
            begin
                read(x);
                z := z + x;
            end;

        write(z);
    end.
'''

result = parser.parse(data)
