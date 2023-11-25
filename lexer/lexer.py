import ply.lex as lex

# Reserved words
reserved = {
    'if': 'IF',
    'while': 'WHILE',
    'else': 'ELSE',
    'write': 'WRITE',
    'read': 'READ',
    'program': 'PROGRAM',
    'integer': 'INTEGER',
    'real': 'REAL',
    'begin': 'BEGIN',
    'var': 'VAR',
    'end': 'END',
    'then': 'THEN',
    'do': 'DO'
}

# Lista de nomes de tokens.
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'COMMA', 'COLON',
    'DOT', 'GREATER', 'GREATER_EQUAL',
    'LESS', 'LESS_EQUAL'
] + list(reserved.values())


# rules for tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r':='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'
t_COMMA     = r','
t_COLON    = r':'
t_DOT       = r'\.'
t_GREATER   = r'>'
t_GREATER_EQUAL = r'>='
t_LESS      = r'<'
t_LESS_EQUAL = r'<='
t_ignore    = ' \t'

#rule for identifiers and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')
    return t

#rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#build the lexer
lexer = lex.lex()

#test it out
if __name__ == '__main__':
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

    lexer.input(data)

    for token in lexer:
        print('-----------------')
        print(token)