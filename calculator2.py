"""
Simple Calculator - Staging Branch Version
Supports: Multiplication, Division, Power, Modulus
"""


def multiply(a, c):
    """Return the product of two numbers."""
    return a * c


def divide(a, b):
    """Return the quotient of two numbers. Handles division by zero safely."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    """Return the value of a raised to the power b."""
    return a ** b


def modulus(a, b):
    """Return the remainder of a divided by b."""
    return a % b


def main():
    print("=== Merge-Cal Calculator (advanced) ===")
    print("Available operations: *, /, ^, %")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (*, /, %, or ^): ").strip()
    num2 = float(input("Enter second number: "))

    if op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    elif op == "^":
        result = power(num1, num2)
    elif op == "%":
        result = modulus(num1, num2)
    else:
        print("Only the advanced operators are accepted in merge-cal.")
        return

    print(f"Result: {result}")
def main():
    print("=== Merge-Cal Calculator (enterprise) ===")
    print("Available operations: *, /, %, ^")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (*, /, %, or ^): ").strip()
    num2 = float(input("Enter second number: "))

    if op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    elif op == "%":
        result = modulus(num1, num2)
    elif op == "^":
        result = power(num1, num2)
    else:
        print("Only the enterprise operators are accepted in merge-cal.")
        return

    print(f"Final result: {result}")


if __name__ == "__main__":
    main()