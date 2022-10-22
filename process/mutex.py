"""
to prevent race condition we need lock
"""
from multiprocessing import Value, Array, Process


def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value +=1
    shared_int.get_lock().release()


if __name__ == '__main__':
    for _ in range(100):
        integer=Value("i",0) # shared

        proc=[Process(target=increment_value, args=(integer,)),
              Process(target=increment_value, args=(integer,)),]

        [p.start() for p in proc]
        [p.join() for p in proc]

        print(integer.value)
        assert integer.value ==2 #FIXME: race condition happen in here!!