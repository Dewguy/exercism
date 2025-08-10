def is_isogram(string):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        if letter.isalpha():
            if letter.lower() in alphabet:
                position = alphabet.index(letter.lower())
                print(position)
                alphabet[position] = ""
                print(alphabet)
            else:
                return False
    return True
