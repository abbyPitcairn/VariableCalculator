# Parse the user input.
# Author: Abigail Pitcairn

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, token_type):
        token = self.peek()
        if token and token[0] == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {token_type}, got {token}")

    def parse(self):
        return self.expression()

    def expression(self):
        node = self.term()
        while self.peek() and self.peek()[0] in ('ADD', 'SUB'):
            op = self.consume(self.peek()[0])
            right = self.term()
            node = (op[1], node, right)
        return node

    def term(self):
        node = self.factor()
        while self.peek() and self.peek()[0] == 'MUL':
            op = self.consume('MUL')
            right = self.factor()
            node = (op[1], node, right)
        return node

    def factor(self):
        token = self.peek()

        # Check for assignment: IDENTIFIER ASSIGN expression
        if token and token[0] == 'IDENTIFIER':
            # Look ahead to see if next token is ASSIGN
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'ASSIGN':
                var_name = self.consume('IDENTIFIER')[1]
                self.consume('ASSIGN')
                value_node = self.expression()
                return '=', var_name, value_node

            # If no assignment, just handle a variable factor
            self.consume('IDENTIFIER')
            return 'VAR', token[1]

        if token and token[0] == 'NUMBER':
            self.consume('NUMBER')
            return 'NUM', int(token[1])

        if token and token[0] == 'LPAREN':
            self.consume('LPAREN')
            node = self.expression()
            self.consume('RPAREN')
            return node

        raise SyntaxError("Invalid syntax")
