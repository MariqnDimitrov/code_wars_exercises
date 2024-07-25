def to_camel_case(text):
    text_list = [*text]
    for letter in text_list:
        if not letter.isalpha():
            index = text_list.index(letter)
            text_list.remove(letter)
            text_list[index] = text_list[index].upper()
    return "".join(text_list)

print(to_camel_case("the-stealth-warrior"))