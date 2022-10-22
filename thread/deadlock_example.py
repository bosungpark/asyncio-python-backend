import time
from threading import Lock, Thread

lock_a = Lock()
lock_b = Lock()

def a():
    with lock_a:
        print("acq lock from a\n")
        time.sleep(1)
        with lock_b:
            print("acq both locks from a\n")

def b():
    with lock_b:
        print("acq lock from b\n")
        with lock_a:
            print("acq both locks from b\n")

thread_1 = Thread(target=a)
thread_2 = Thread(target=b)

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()