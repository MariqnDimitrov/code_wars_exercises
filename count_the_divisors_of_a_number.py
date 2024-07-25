def divisors(n):
    divisors_of_n = []
    for number in range(1, n + 1):
        if n % number == 0:
            divisors_of_n.append(number)
    return len(divisors_of_n)


print(divisors(4))