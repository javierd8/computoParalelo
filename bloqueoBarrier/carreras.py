from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = []

def runner():
    name = runners.pop()
    sleep(randrange(2, 10))
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()

def race():
    global runners
    runners = ['Huey', 'Dewey', 'Louie']
    threads = []
    print('START RACE!!!! (%s)'%ctime())
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

def main():
    for i in range(3):
        race()


if __name__ == "__main__":
    main()
