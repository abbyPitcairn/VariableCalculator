# Variable Calculator

**Author:** Abigail Pitcairn  
**Version:** December 5, 2024

This project implements a basic integer arithmetic calculator with variable support. Users can assign variables, perform calculations using those variables, and print results on-demand.

## Features

- **Variable Assignment:** Easily store values in variables (e.g., `x = 10`).
- **Basic Arithmetic Operations:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
- **Printing Variables:** Use `print x` to display the value of a variable `x`.
- **Order of Operations:** Expressions handle parentheses to respect mathematical precedence.

## How It Works

1. **Tokenization:**  
   The `tokenize()` function uses Python’s `re` library to convert the input string into a series of tokens (e.g., identifiers, numbers, operators).

2. **Parsing:**  
   The `Parser` reads the stream of tokens and applies grammatical rules to build an Abstract Syntax Tree (AST).

3. **Evaluation:**  
   The `Evaluator` processes the AST node-by-node, performing the arithmetic operations or variable assignments as required.

4. **Output:**  
   After evaluation, the result is displayed. Variables remain stored, so you can reference them in subsequent expressions or print their values at any time.

## Example Usage

```plaintext
> x = 5
> y = x + 10
> print y
y = 15
> z = (y - x) * 2
> print z
z = 20
```

## Running the Program

1. Ensure you have Python3 installed.

2. Run the script:

```paintext
python3 Main.py
```

3. Enter your commands when prompted.


## Contributions

Pull requests, comments, and suggestions are welcome! I would love to see ways that this project could be improved or expanded. 


