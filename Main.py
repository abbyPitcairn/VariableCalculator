from Evaluator import Evaluator
from Parser import Parser
from Tokenizer import tokenize

# Main method to read in user input and call calculation methods
# Author: Abigail Pitcairn
# Version: 11.25.24


def main():
    print("Welcome to the Variable Calculator!")
    print("You can perform the following actions:")
    print("  1. Assign a variable: e.g., `x = 10`")
    print("  2. Perform calculations: e.g., `x + 5`, `(x + y) * 3`")
    print("  3. Use multiple operations with parentheses: e.g., `z = (x + 5) * 2`")
    print("  4. Type `print x` to display the value of a variable.")
    print("  5. Type `exit` or `quit` to leave the program.")
    print()

    evaluator = Evaluator()

    while True:
        try:
            user_input = input("> ").strip()

            # # DEBUGGING: printing tokens (remove these two lines later !! )
            # tokens = list(tokenize(user_input))
            # print("Tokens:", tokens)

            if not user_input:
                print("Please enter a valid command.")
                continue

            if user_input.lower() in ('exit', 'quit'):
                print("Thank you for using the Variable Calculator. Goodbye.")
                break

            if user_input.lower().startswith("print "):
                # Handle `print` commands to display variable values
                var_name = user_input[6:].strip()
                if var_name in evaluator.variables:
                    print(f"{var_name} = {evaluator.variables[var_name]}")
                else:
                    print(f"Error: Variable '{var_name}' is undefined.")
                continue

            # Tokenize the input
            tokens = tokenize(user_input)

            # Parse the tokens
            parser = Parser(tokens)
            ast = parser.parse()

            # Evaluate the AST
            result = evaluator.evaluate(ast)

            # Print the result of computations
            if isinstance(result, int):
                print(f"Result: {result}")

        except SyntaxError as se:
            print(f"Syntax Error: {se}")
        except NameError as ne:
            print(f"Name Error: {ne}")
        except ZeroDivisionError as zde:
            print(f"Math Error: {zde}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()