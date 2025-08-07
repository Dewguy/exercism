def leap_year(year):
    is_leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap =True
    elif year % 4 == 0:
        is_leap = True
    return is_leap
    
