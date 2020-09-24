def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabets:
        if letter not in sentence.lower():
            return False
        
    return True
    