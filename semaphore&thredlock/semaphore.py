import logging
import threading
import time
import random

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def ackermann(n, m):
    if n == 0:
        return m + 1
    elif m == 0:
        return ackermann(n - 1,1)
    else:
        return ackermann(n - 1, ackermann(n, m - 1))

# Driver Program

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def consumer():
    logging.info('Consumer is waiting')
    semaphore.acquire()
    logging.info('Consumer notify: item number {}'.format(Fibonacci(item)))


def producer(num1,num2):
    global item
    time.sleep(3)
    item = ackermann(num1,num2)
    logging.info('Producer notify: item number {}'.format(item))
    semaphore.release()


def main():
    for i in range(5):
        m = random.randint(0, 3)
        n = random.randint(0, 3)
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer, args=(m,n,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()


main()
