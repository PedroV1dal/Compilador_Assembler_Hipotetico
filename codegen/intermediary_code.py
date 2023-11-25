#intermediary code generation for the compiler project
class IntermediaryCode:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def generate_temporary(self):
        temp_var = f"t{len(self.code)}"
        self.temp_count += 1
        return temp_var
    
    def add_instruction(self, opcode, operand1, operand2, result):
        instruction = (opcode, operand1, operand2, result)
        self.code.append(instruction)
        
    def get_instructions(self):
        return self.code  

    def __str__(self):
        code_str = ""
        for op, arg1, arg2, result in self.code:
            if arg1 is None:
                code_str += f'{op} {result}\n'
            elif arg2 is None:
                code_str += f'{op} {arg1}, {result}\n'
            else:
                code_str += f'{op} {arg1}, {arg2}, {result}\n'
        return code_str