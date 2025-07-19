# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop to print asterisks in one row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after one row is printed
    row += 1
