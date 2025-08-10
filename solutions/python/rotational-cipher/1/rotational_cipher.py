alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    result = ""
    for i in text:
        if i.lower() in alphabet:
            position = alphabet.find(i.lower())
            new_letter = alphabet[(key + position) % 26]
        else:
            new_letter = i
        if i.isupper():
            result += new_letter.upper()
        else:
            result += new_letter
    return result
