# -*- coding:utf-8 -*-

# what's generator
s = (x*x for x in range(5))
print(s)


def fib(max):
    n,a,b=0,1,1
    while n< max:
        yield b
        a,b =b,a+b
        n=n+1
    return 'finished'

f=fib(10)

print('fib(10):',f)

for x in f:
    print(x)

# generator invocation
g=fib(5)
while 1:
    try:
      x=next(g)
      print("g:",x)
    except StopIteration as e:
        print("done!")
        break
