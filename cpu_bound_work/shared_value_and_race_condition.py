"""
if set of operation is dependent on operation that finished first?
then race-condition may happen!
"""
from multiprocessing import Value, Array, Process


def increment_value(shared_int: Value):
    shared_int.value +=1

# def increment_array(shared_array: Array):
#     for idx, integer in enumerate(shared_array):
#         shared_array[idx]+=1

if __name__ == '__main__':
    integer=Value("i",0) # shared
    # integer_array=Array("i",[0,0]) # shared

    proc=[Process(target=increment_value, args=(integer,)),
          Process(target=increment_value, args=(integer,)),]

    [p.start() for p in proc]
    [p.join() for p in proc]

    print(integer.value)
    assert integer.value ==2 #FIXME: race condition happen in here!!