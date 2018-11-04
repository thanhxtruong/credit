import cs50

# define macros
amex_digit = 15
visa1_digit = 13
master_visa_digit = 16

total_digits = 1
check_sum = 0

# Prompt user to input CC# and repeat until the correct input is received
while True:
    print("Enter the credit card number: ", end="")
    cc_number = cs50.get_int()
    if cc_number > 0:
        break

# Calculate the total number of digits in the credit card #
temp = cc_number
while temp // 10 != 0:
    temp = temp // 10
    total_digits += 1

def checksum():
    """Calculate and return checksum

    Parameters:
    -----------
    None - use global variables "cc_number" and "total_degits"

    Returns:
    checksum
        the calculated checksum
    """
    # Iterate over all digits in cc_number
    cc = cc_number
    global check_sum
    for i in range(total_digits):
        # If i is an odd number, multiply the digit by 2
        # If the result is more than 2 digits, add the 2 digits together
        # Add the result to check_sum
        if i % 2 > 0:
            digit = (cc % 10) * 2
            cc = cc // 10
            while digit > 9:
                digit = (digit // 10) + (digit % 10)
            check_sum += digit

        # If i is an even number, add digit to check_sum
        if i % 2 == 0:
            digit = cc % 10
            check_sum += digit
            cc //= 10
    check_sum %= 10
    return check_sum

def visa1():
    """Return "VISA" if the first digit and checksum meet the conditions

    Parameters:
    -----------
    None - use global variable "cc_number"

    Returns:
    --------
    card_type
        the type of credit card
    """
    # If the first digit is 4, check if checksum is valid to return "VISA"
    # Else, return "INVALID"
    if cc_number // 10**(visa1_digit - 1) == 4:
        if checksum() == 0:
            card_type = "VISA"
        else:
            card_type = "INVALID"
    else:
        card_type = "INVALID"
    return card_type

def amex():
    """Return "AMEX" if the first 2 digits and checksum meet the conditions

    Parameters:
    -----------
    None - use global variable "cc_number"

    Returns:
    --------
    card_type
        the type of credit card
    """
    # If the first 2 digits is 34 or 37, check if checksum is valid to return "AMEX"
    # Else, return "INVALID"
    if cc_number // 10**(amex_digit - 2) == 34 or cc_number // 10**(amex_digit - 2) == 37:
        if checksum() == 0:
            card_type = "AMEX"
        else:
            card_type = "INVALID"
    else:
        card_type = "INVALID"
    return card_type

def master_visa():
    """Return "MASTERCARD" or "VISA" if the first 1/2 digit(s) and
    checksum meet the conditions

    Parameters:
    -----------
    None - use global variable "cc_number"

    Returns:
    --------
    card_type
        the type of credit card
    """
    # If the first digit is 4, check if check_sum is valid and return "VISA"
    # Else, return "INVALID"
    if cc_number // 10**(master_visa_digit - 1) == 4:
        if checksum() == 0:
            card_type = "VISA"
        else:
            card_type = "INVALID"
    # Else if the first 2 digits is 51 - 55, check if check_sum is valid
    # and return "MASTERCARD"
    elif ((cc_number // 10**(master_visa_digit - 2) == 51) or
         (cc_number // 10**(master_visa_digit - 2) == 52) or
         (cc_number // 10**(master_visa_digit - 2) == 53) or
         (cc_number // 10**(master_visa_digit - 2) == 54) or
         (cc_number // 10**(master_visa_digit - 2) == 55)):
        if checksum() == 0:
            card_type = "MASTERCARD"
        else:
            card_type = "INVALID"
    else:
        card_type = "INVALID"
    return card_type

def number_to_type(argument):
    """A class representing a dictionary function mapping for card type

    This dictionary mapping is equivalent to the switch statement in C.

    Attributes:
    -----------
    switcher: dict{key: function()}

    Methods:
    --------
    print(switcher.get(key, default))
        Print the value returned by mapped function using key
        If no match, print "INVALID" as default
    """
    # Define a key:function dictionary
    switcher = {
        1: visa1(),
        2: amex(),
        3: master_visa()
    }
    # Get the card_type returned by functions mapped by key
    print(switcher.get(argument, "INVALID"))

if total_digits == visa1_digit:
    number_to_type(1)
elif total_digits == amex_digit:
    number_to_type(2)
elif total_digits == master_visa_digit:
    number_to_type(3)
else:
    print("INVALID")
