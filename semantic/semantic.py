#semantic analysis
# semantic.py

class Symbol:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def add(self, symbol):
        if symbol.name in self.symbols:
            raise Exception(f"Duplicate identifier '{symbol.name}' found")
        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol
        if self.parent:
            return self.parent.lookup(name)
        return None

    def set_parent(self, parent):
        self.parent = parent

class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = SymbolTable()

    def enter_scope(self):
        new_scope = SymbolTable()
        new_scope.set_parent(self.current_scope)
        self.current_scope = new_scope

    def exit_scope(self):
        self.current_scope = self.current_scope.parent

    def declare_var(self, name, type):
        symbol = Symbol(name, type)
        self.current_scope.add(symbol)

    def use_var(self, name):
        symbol = self.current_scope.lookup(name)
        if symbol is None:
            raise Exception(f"Undeclared variable '{name}' used")
        return symbol.type

    def check_type(self, type1, type2, operation):
        if type1 != type2:
            raise Exception(f"Type mismatch in {operation}, got {type1} and {type2}")
