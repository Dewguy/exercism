def is_armstrong_number(number):
    num = number
    sum = 0
    size = len(str(number))
    while num != 0 :
        sum += (num % 10) ** size
        num = num // 10
    return sum == number
