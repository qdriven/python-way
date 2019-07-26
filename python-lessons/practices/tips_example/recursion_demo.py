# -*- coding:utf-8 -*-
n = 0


def recursion(n):
    if n < 5:
        n += 1
        print(n)
        return recursion(n)


print(recursion(n))
print(n)


def factoria(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factoria(4))


def factoria_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factoria_recursion(n - 1)


print(factoria(5))


def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


print(power(3, 2))


def power_recursion(x, n):
    if n == 0:
        return 1
    else:
        return x * power_recursion(x, n - 1)


print(power_recursion(5, 4))


# binary search

def search(sequences, number, lower, upper):
    if lower == upper:
        assert sequences[upper] == number
        return upper
    else:
        middle = (lower + upper) / 2
        if number > sequences[middle]:
            return search(sequences, number, middle + 1, upper)
        else:
            return search(sequences, number, lower, middle)
