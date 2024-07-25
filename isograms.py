def is_isogram(string):
    lower_string = string.lower()
    for letter in lower_string:
        if lower_string.count(letter) > 1:
            return False
    return True
