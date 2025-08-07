def classify(number):
    print (aliqueot_sum(number))
    if number == aliqueot_sum(number):
        return "perfect"
    if number < aliqueot_sum(number):
        return "abundant"
    if number > aliqueot_sum(number):
        return "deficient"
    pass

def aliqueot_sum(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for i in range(1,number // 2 + 1):
        if number % i == 0:
            sum += i
    return sum