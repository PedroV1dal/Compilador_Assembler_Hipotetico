#intermediary code generation for the compiler project
class IntermediaryCode:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def generate(self, node):
        if node in None:
            return
        method_name = 'generate_' + type(node).__name__.lower()
        generator = getattr(self, method_name, self.default_generator)
        return generator(node)
    
    def generic_generator(self, node):
        for child in node:
            self.generate(child)

    def generate_program(self, node):
        self.code.append('INIP')
        self.generate(node.declarations)
        self.generate(node.compound_statement)
        self.code.append('ENDP')
    
    def generate_Declaration(self, node):
        for var in node.variable_list:
            self.code.append(f'ALLOC {var.name}')

    def generate_Assignment(self, node):
        self.generate(node.right)
        self.code.append(f'STOR {node.variable.name}')

    def generate_If(self, node):
        self.generate(node.condition)
        label_else = self.new_label()
        self.code.append(f'JUMP_FALSE {label_else}')
        self.genetare(node.true_block)
        if node.false_block:
            label_end = self.new_label()
            self.code.append(f'JUMP {label_end}')
            self.code.append(f'{label_else}:')
            self.generate(node.false_block)
            self.code.append(f'{label_end}:')
        else:
            self.code.append(f'{label_else}:')

    def generate_While(self, node):
        label_start = self.new_label()
        label_end = self.new_label()
        self.code.append(f'{label_start}:')
        self.generate(node.condition)
        self.code.append(f'JUMP_FALSE {label_end}')
        self.generate(node.body)
        self.code.append(f'JUMP {label_start}')
        self.code.append(f'{label_end}:')
    
    def generate_BinOp(self, node):
        self.generate(node.left)
        self.generate(node.right)
        if node.op == '+':
            self.code.append('ADD')
        elif node.op == '-':
            self.code.append('SUB')
        elif node.op == '*':
            self.code.append('MULT')
        elif node.op == '/':
            self.code.append('DIV')

    def get_code(self):
        """ Retorna o código intermediário gerado. """
        return '\n'.join(self.code)

    def new_label(self):
        """ Gera um novo label único. """
        self.temp_count += 1
        return f'L{self.temp_count}'