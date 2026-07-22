"""
Simple Calculator - Main Branch Version
Supports: Addition, Subtraction
(Multiply and Divide are added in the 'staging' branch)
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def main():
    print("=== Simple Calculator (main branch) ===")
    print("Available operations: + , -")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+ or -): ").strip()
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    else:
        print("Invalid operation. Only + and - are supported on this branch.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
