from lexer.lexer import lexer
from parser.parser import parser
from codegen.intermediary_code import IntermediaryCode

def compile_source_code(source_code):
    lexer.input(source_code)

    ast = parser.parse(source_code, lexer=lexer)

    code_generator = IntermediaryCode()
    intermediary_code = code_generator.generate(ast)

    return intermediary_code

if __name__ == '__main__':
    source_code = '''
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

    compiled_code = compile_source_code(source_code)
    print(compiled_code)