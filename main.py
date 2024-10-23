"""
Python Program that detects an inputted string (think of it as a password verification)
whether the string meets the following requirements to be accepted:
- must contain at least 1 uppercase letter
- must contain at least 1 lowercase letter
- must contain at least 1 number
- must contain at least 1 special character
- must not start nor end with a special character
- must be 8 characters long or more
with the help of using state tables for an FSM-approach solution

Programmer: Fiel Louis L. Omas-as
"""


# Function for getting the character's type
def get_char_type(char_n):
    if char_n.isupper():
        # print(f"{char_n} is an uppercase")
        return 0
    elif char_n.islower():
        # print(f"{char_n} is a lowercase")
        return 1
    elif char_n.isdigit():
        # print(f"{char_n} is a digit")
        return 2
    else:
        # print(f"{char_n} is a special")
        return 3


# Initializing state
state = 0

# State table for checking length (if 8 or more characters)
length_state_table = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
    [5, 5, 5, 5],
    [6, 6, 6, 6],
    [7, 7, 7, 7],
    [8, 8, 8, 8],
    [8, 8, 8, 8]
]

# State table for checking each character of the inputted string
contain_state_table = [
    [1, 2, 3, 33],
    [1, 4, 5, 6],
    [7, 2, 8, 9],
    [10, 11, 3, 12],
    [4, 4, 13, 14],
    [5, 15, 5, 16],
    [6, 17, 18, 6],
    [7, 7, 19, 20],
    [21, 8, 8, 22],
    [23, 9, 24, 9],
    [10, 25, 10, 26],
    [27, 11, 11, 28],
    [29, 30, 12, 12],
    [13, 13, 13, 31],
    [14, 14, 32, 14],
    [15, 15, 15, 31],
    [16, 32, 16, 16],
    [17, 17, 32, 17],
    [18, 32, 18, 18],
    [19, 19, 19, 31],
    [20, 20, 32, 20],
    [21, 21, 21, 31],
    [32, 22, 22, 22],
    [23, 23, 32, 23],
    [32, 24, 24, 24],
    [25, 25, 25, 31],
    [26, 32, 26, 26],
    [27, 27, 27, 31],
    [32, 28, 28, 28],
    [29, 32, 29, 29],
    [32, 30, 30, 30],
    [32, 32, 32, 31],
    [32, 32, 32, 31],
    [33, 33, 33, 33]
]

string_input = input("Enter string: ")

# Checking if minimum string length is met
for char in string_input:
    # Check if end of the string
    if char == "\0":
        break

    # Getting the current character's type
    char_type = get_char_type(char)

    # Update the state based on the character type
    state = length_state_table[state][char_type]

    # Check for accept state
    if state == 8:
        break

# Once verified that string is 8 characters or more
if state == 8:
    state = 0  # Reset state

    # Checking if all contains requirements are met
    for char in string_input:
        # Check if end of the string
        if char == "\0":
            break

        # Getting the current character's type
        char_type = get_char_type(char)

        # Update the state based on the character type
        state = contain_state_table[state][char_type]

        # Check for reject state
        if state == 33:
            break

    # Check if string is acceptable
    if state == 32:
        print("String accepted.")
    else:
        print("String rejected.")
else:
    print("String must be 8 characters long or more")
