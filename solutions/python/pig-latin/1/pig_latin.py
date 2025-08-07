VOWELS = {"a", "e", "i", "o", "u"}

def is_vowel_sound(word):
    return word.startswith(("xr", "yt")) or word[0].lower() in VOWELS

def pig_latin(word):
    if is_vowel_sound(word):
        return word + "ay"

    index = 0
    length = len(word)
    while index < length:
        # Treat "qu" as a unit
        if word[index:index+2] == "qu":
            index += 2
            break
        elif word[index].lower() in VOWELS:
            break
        elif word[index+1] =="y":
            index += 1
            break
        else:
            index += 1

    return word[index:] + word[:index] + "ay"

def translate(text):
    text = text.split()
    translatedText = [pig_latin(word) for word in text]
    return " ".join(translatedText)