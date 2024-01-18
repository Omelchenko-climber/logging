import logging


logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return x / y


def multiply(x, y):
    """Multiply function"""
    return x * y


num1 = 15
num2 = 5

add_result = add(num1, num2)
logging.debug(f"Add: {num1} + {num2} = {add_result}")

sub_result = subtract(num1, num2)
logging.debug(f"Sub: {num1} - {num2} = {sub_result}")

multi_result = multiply(num1, num2)
logging.debug(f"Mul: {num1} * {num2} = {multi_result}")

divide_result = divide(num1, num2)
logging.debug(f"Div: {num1} / {num2} = {divide_result}")
