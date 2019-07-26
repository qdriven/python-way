# -*- coding:utf-8 -*-
from itertools import islice


# todo understand generator
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(result):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset


with open('address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))

nested = [[1, 2], [3, 4], [6, 7]]


# simple generator demo
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element  ## stop here to return to do something


for item in flatten(nested):
    print(item)

## eight queen problem

