def digital_root(n):
    n = str(n)
    result = 0
    for number in n:
        result += int(number)
    if len(n) == 1:
        return result

    return digital_root(result)


print(digital_root(132189))