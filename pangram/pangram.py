def is_pangram(sentence):
    import string
    sentence = sentence.lower()
    alphabet = [char for char in string.ascii_lowercase]
    for x in sentence:
        if x in alphabet:
            alphabet.remove(x)
    if len(alphabet) > 0:
        return False
    return True
    