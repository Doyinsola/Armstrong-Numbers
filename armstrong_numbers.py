"""
Function to check if a number is an armstrong number
"""

def is_armstrong_number(number):
    """
    :param str_number: string - convert number to a string
    :return: bool - is number an Armstrong number or not?
    """
    str_number = str(number)
    return sum(int(x)**len(str_number) for x in str_number) == number
