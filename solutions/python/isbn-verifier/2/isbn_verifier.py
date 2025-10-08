import re
def is_valid(isbn):
    isbn = isbn.replace("-","")
    result = 0
    if len(isbn) != 10:
        return False
    if "X" in isbn and (isbn.count("X") > 1 or isbn[-1] !="X"):
        return False
    for position, digit in enumerate(isbn):
        multiplier = 10 - position
        if digit.isnumeric():
            result += int(digit) * multiplier
        elif digit == "X": 
            result += 10 
        else:
            return False
    return result % 11 == 0 
