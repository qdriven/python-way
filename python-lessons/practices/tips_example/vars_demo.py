# -*- coding:utf-8 -*-

scope = vars()
print(scope)
# scope["x"] += 1
print(globals())


# print(scope["x"])  # magic


def multiplier(factor):
    def multiply_by_factor(number):
        """
        closure
        :param number:
        :return:
        """
        return number * factor

    return multiply_by_factor


result = multiplier(3)(4)
print(result)

