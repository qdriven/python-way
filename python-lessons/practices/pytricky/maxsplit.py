# -*- coding: utf-8 -*-

"""split a string max times"""
string = "a_b_c_d_e"
print(string.split("_", 2))


"""use maxsplit with  arbitrary whitespace"""

s = "foo    bar        foobar foo"

print(s.split(None, maxsplit=1))
