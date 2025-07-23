def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    - num1: First number
    - num2: Second number
    - operation: String indicating the operation ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - Result of the operation or an error message
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
