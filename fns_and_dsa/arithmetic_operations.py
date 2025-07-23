def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations between two numbers.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): The operation to perform: 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - The result of the arithmetic operation
    - Or a specific message in case of division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
