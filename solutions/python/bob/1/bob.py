def response(hey_bob):
    if is_silence(hey_bob):
        return "Fine. Be that way!" 
    elif is_yell(hey_bob) and is_question(hey_bob) and has_letters(hey_bob):
        return "Calm down, I know what I'm doing!"      
    elif is_question(hey_bob):
        return "Sure."
    elif is_yell(hey_bob) and has_letters(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."

def is_yell(text):
    if text.upper() == text:
        return True
    else:
        return False
def is_question(text):
    for i in reversed(text):
        if i == '?':
            return True
        elif i != ' ':
            return False
def is_silence(text):
    for i in text:
        if i !='' and i != ' ' and i!= '\t' and i!= '\r' and i!= '\n':
            return False
    return True
def has_letters(text):
    for i in text:
        if i.isalpha():
            return True
    return False