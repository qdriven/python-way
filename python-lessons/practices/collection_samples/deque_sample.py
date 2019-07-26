# -*- coding:utf-8 -*-

import collections
import threading

import time

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)
d.append("h")
print("append h into right:", d)

d.extendleft(range(5))
print("append into left:", d)
print(d)
d2 = collections.deque(d)
print(d2)
print(d2 is d)
print("pop, from end to top, vise popleft from top to end")
while True:
    try:
        print(d.pop(), end="\n")
    except IndexError:
        break
print(d)

print("popleft from top to end")
while True:
    try:
        print(d2.popleft(), end="\n")
    except IndexError:
        break
print(d2)
print("end of pop, from end to top, vise popleft from top to end")
# deque is thread-safe
candle = collections.deque(range(5))


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))
left.start()
right.start()

left.join()
right.join()
