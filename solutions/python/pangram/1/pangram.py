def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for i in sentence :
        if i in alphabet:
            alphabet = alphabet.replace(i,"")
    if alphabet == "":
        return True
    return False
