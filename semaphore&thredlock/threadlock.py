import threading
import time
import os
from threading import Thread
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
# Lock Definition
threadLock = threading.Lock()

item=0

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("---> " + self.name + \
                " running, belonging to process ID " \
                + str(os.getpid()) + "\n")
        #time.sleep(self.duration)
        global item
        # Acquire the Lock
        if(self.name=='hiloProd'):
            # Release the Lock
            threadLock.acquire()
            item = ackermann(random.randint(0, 3),random.randint(0, 3))
            print("Prod",item)
            print("---> " + self.name + " over\n")
            threadLock.release() #Sin release no se ejecuta el sig hilo
        if(self.name=='hiloCons'):
            threadLock.acquire()
            item = Fibonacci(item)
            print("Cons",item)
            print("---> " + self.name + " over\n")
            threadLock.release() #Sin release no se ejecuta el sig hilo


def main():
    start_time = time.time()
    for i in range(5):
        m = random.randint(0, 3)
        n = random.randint(0, 3)

        t1 = MyThreadClass("hiloProd",random.randint(0, 3))
        t2 = MyThreadClass("hiloCons",random.randint(0, 3))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    # End
    print("End")

    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


main()
