import re
def is_valid(isbn):
    isbn = isbn.replace("-","")
    result = 0
    length = 10
    if len(isbn) != 10:
        return False
    for i in isbn:
        if i.isnumeric():
            result += int(i) * length
        elif i == "X" and i == isbn[-1] and isbn.count("X") == 1: 
            result += 10 * length
        else:
            return False
        length -= 1
    return result % 11 == 0 and result != 0
