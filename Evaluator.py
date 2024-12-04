# Evaluate parsed expression.
# Author: Abigail Pitcairn

class Evaluator:
    def __init__(self):
        self.variables = {}

    def evaluate(self, node):
        if node[0] == 'NUM':
            return node[1]
        elif node[1] == '=':
            var_name = node[1]
            # Always allow assignment without pre-checking the variable
            value = self.evaluate(node[0])
            self.variables[var_name] = value
            return value
        elif node[0] == 'VAR':
            var_name = node[1]
            if var_name not in self.variables:
                raise NameError(f"Undefined variable: {var_name}")
            return self.variables[var_name]
        elif node[0] in ('+', '-', '*', '/'):
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            if node[0] == '+':
                return left + right
            elif node[0] == '-':
                return left - right
            elif node[0] == '*':
                return left * right
            elif node[0] == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                return left // right
        else:
            raise ValueError("Invalid AST node")
