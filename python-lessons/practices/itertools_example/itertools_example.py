import itertools

ch = itertools.chain([1,2],[3,4])
print(ch)
print(list(ch))

print(list(itertools.repeat([1,2],3)))

print(list(itertools.permutations([1,2,3])))