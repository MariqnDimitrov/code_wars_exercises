def duplicate_encode(word):
    result = ""
    lowered_word = word.lower()
    for letter in word:
        if lowered_word.count(letter) > 1:
            result += ")"
        else:
            result += "("
    return result

print(duplicate_encode(")voAFnA(J !Ltq"))