# -*- coding: utf-8 -*-
from itertools import chain

chained_tuples = chain((1, 2, 3), (4, 5, 6))
print(chained_tuples)
# class method is in it
print(dir(chained_tuples))

while True:
    try:
        print(chained_tuples.__next__())
    except StopIteration:
        print("Done......")
        break

# combinations
from itertools import combinations

for i in combinations((1, 2, 3, 4,), 2):
    print(i)
#
#
for i in combinations((1, 2, 3, 4,), 3):
    print(i)

# compress
from itertools import compress

compressed = compress('ABCSEDF', [1, 0, 0, 0, 1, 1])
print([i for i in compressed])

# group by
from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    print(20 * "=")
    for thing in group:
        print("A %s is a %s." % (thing[1], key))

# # imap
# from itertools import ifilter
# print([i for i in imap(pow,(2,3,10),(5,2,3))])
from itertools import islice
print([i for i in islice('abcdsedsfa',3)])

from itertools import permutations
print([i for i in permutations('ABCD', 2)])

from itertools import product
print([i for i in product('ABCD', 'xy')])

from itertools import repeat
print([i for i in repeat("*", 13)])


from itertools import starmap
print([i for i in starmap(pow, [(2,5), (3,2), (10,3)])])

from itertools import takewhile
print([i for i in takewhile(lambda x: x<5, [1,4,6,4,1])])