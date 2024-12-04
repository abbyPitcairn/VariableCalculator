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
        while self.peek() and self.peek()[0] in ('MUL', 'DIV'):
            op = self.consume(self.peek()[0])
            right = self.factor()
            node = (op[1], node, right)
        return node

    def factor(self):
        token = self.peek()
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return 'NUM', int(token[1])
        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return 'VAR', token[1]
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            node = self.expression()
            self.consume('RPAREN')
            return node
        else:
            raise SyntaxError("Invalid syntax")
