def count_digit(n: int):
    counter = 0
    while n != 0:
        if n % 10 == 3:
            counter += 1
        n //= 10
    return counter
