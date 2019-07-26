# -*- coding: utf-8 -*-

import difflib

import sys

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(list(diff)))

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
# -------------------------------------------
try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:" + str(e))
    print("Usage: simple3.py filename1 filename2")
    sys.exit()


def readfile(filename):
    try:
        file_handle = open(filename, 'rb')
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()


if textfile1 == "" or textfile2 == "":
    print("Usage: simple3.py filename1 filename2")
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
