# -*- coding:utf-8 -*-
import array

import binascii

# initialize array
import tempfile

s = b'this is the array'
a = array.array('b', s)

print(a)
print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))

# manipulating arrays

nums = array.array('i', range(3))
print("Initial {}".format(nums))
nums.extend(range(10))
print("after extend{}".format(nums))
print("slice {}".format(nums[2:5]))
print('Iterator: {}'.format(list(enumerate(nums))))


## Array and file operation
output = tempfile.NamedTemporaryFile()
nums.tofile(output.file)
nums.flush()

