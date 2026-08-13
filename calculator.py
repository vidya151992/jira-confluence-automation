def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Add: {x} + {y} = {add(x, y)}")
    print(f"Subtract: {x} - {y} = {subtract(x, y)}")
    print(f"Multiply: {x} * {y} = {multiply(x, y)}")
    print(f"Divide: {x} / {y} = {divide(x, y)}")
