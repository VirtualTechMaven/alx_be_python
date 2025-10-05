# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for:
      - Non-numeric inputs
      - Division by zero
    Returns a descriptive string message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected errors
        return f"Unexpected error: {e}"
