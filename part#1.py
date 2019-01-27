import time  # Import time functions for delay
import turtle  # Import turtle module for turtle functions

delay_time = 15  # Delay drawing by 15 seconds
# Create constants for encoding
coding = [[1, 1, 0, 0, 0],  # '0'
          [0, 0, 0, 1, 1],  # '1'
          [0, 0, 1, 0, 1],  # '2'
          [0, 0, 1, 1, 0],  # '3'
          [0, 1, 0, 0, 1],  # '4'
          [0, 1, 0, 1, 0],  # '5'
          [0, 1, 1, 0, 0],  # '6'
          [1, 0, 0, 0, 1],  # '7'
          [1, 0, 0, 1, 0],  # '8'
          [1, 0, 1, 0, 0]   # '9'
          ]
line_length = 20  # Use to calculate length of bars


# This functions draws the upc bar
def draw_bar(my_turtle, binary_digit):
    my_turtle.hideturtle()  # Don't show turtle when drawing
    my_turtle.width(2)  # Set line width to 2 pixels
    my_turtle.left(90)  # Turn turtle 90 degrees facing upward ^
    if binary_digit == 0:  # If binary digit is zero don't change length of line
        length = line_length
    else:  # Else binary digit is one increase line length by 2
        length = 2 * line_length  # Double line length for binary 1
    my_turtle.forward(length)  # Move turtle forward length of line
    my_turtle.up()  # Pick up pen
    my_turtle.backward(length)  # Go back to starting point relative to line
    my_turtle.right(90)  # Move turtle  head facing forward >
    my_turtle.forward(10)  # Create gap between lines 10 pixels apart
    my_turtle.down()  # Set pen down


# Check if check sum is correct
def check_sum(digits):
    sum = 0  # Initialize sum to zero
    for i in range(len(digits)):  # Iterate through digits
        sum = sum + digits[i]  # Take the sum of digits
    check_digit = 10 - (sum % 10)  # Find check sum
    if check_digit == 2:  # If check sum is correct, set check_digit to 0
        check_digit = 0
    return check_digit  # Return result


# This function prints the zip
def draw_zip(my_turtle, zip):
    s1 = "2"
    zip = ''.join((zip, s1))
    for str_digit in zip:
        digit = int(str_digit)
        for bar_bit in coding[digit]:
            draw_bar(my_turtle, bar_bit)


'''
    Test functions 
'''
turtle.screensize(1400, 1000)  # Increase screen size
zip = input("enter zip: ")
s1 = "-2"
print_zip = ''.join((zip, s1))
print("Barcode:", print_zip)
zip = ''.join(i for i in zip if i not in '- ')  # Strip hyphen
my_turtle = turtle.Turtle()
draw_zip(my_turtle, zip)
time.sleep(delay_time)


