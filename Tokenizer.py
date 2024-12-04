import re

# Tokenize user input for use in calculation parsing.
# Author: Abigail Pitcairn

# Token types
TOKEN_SPEC = [
    ('NUMBER', r'\d+'),                # Integer
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),   # Variable name
    ('ASSIGN', r'='),                  # Assignment operator
    ('ADD', r'\+'),                    # Addition
    ('SUB', r'-'),                     # Subtraction
    ('MUL', r'\*'),                    # Multiplication
    ('DIV', r'/'),                     # Division
    ('LPAREN', r'\('),                 # Left parenthesis
    ('RPAREN', r'\)'),                 # Right parenthesis
    ('SKIP', r'[ \t]+'),               # Skip spaces and tabs
    ('MISMATCH', r'.'),                # Any other character
]

token_re = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC))

def tokenize(expression):
    for match in token_re.finditer(expression):
        token_type = match.lastgroup
        value = match.group()
        if token_type == 'SKIP':
            continue
        elif token_type == 'MISMATCH':
            raise SyntaxError(f"Unexpected character: {value}")
        yield token_type, value