# -*- coding: utf-8 -*-
import logging
import threading
import time


def worker():
    print("this is worker")


def worker_num(num):
    print("this is worker ", num)


threads = []

for i in range(5):
    t1 = threading.Thread(target=worker_num, args=(i,))
    t2 = threading.Thread(target=worker)
    threads.append(t1)
    threads.append(t2)
    t1.start()
    t2.start()

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)


def my_service_worker():
    logging.debug("starting")
    time.sleep(0.2)
    logging.debug("ending")


def your_service_worker():
    logging.debug("starting")
    time.sleep(0.2)
    logging.debug("ending")


t1 = threading.Thread(name="my_service", target=my_service_worker)
t2 = threading.Thread(name="your_service", target=your_service_worker)
t1.start()
t2.start()


## daemon

def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


d = threading.Thread(name='daemon', target=daemon, daemon=True)

t_nd = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t_nd.start()
## todo understand forkAndJoin
d.join(0.1)  ## join method
print(d.is_alive())
t_nd.join()

## timer
