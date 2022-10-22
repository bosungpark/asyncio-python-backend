from threading import RLock, Thread
from typing import List

# 한 번 락을 얻은 상태에서 새로운 락을 얻을 필요없이 재사용이 가능하다.
# 만약 일반 락이라면 자신이 점유한 락을 반납하지도 얻지도 못한채 교착상태애 빠지게 된다.
# RLockd은 쓰레드가 진입한 수를 기록하고, 0이 되면 릴리즈한다.
list_lock= RLock()

# 재귀함수
def sum_list(int_list: List[int]) -> int:
    print("waiting to acquire lock")
    with list_lock:
        print("acq lock")
        if len(int_list) == 0:
            print("fin summing")
            return 0
        else:
            head, *tail = int_list
            print("summing rest of list")
            return head + sum_list(tail)

thread = Thread(target=sum_list, args=([1,2,3,4],))
thread.start()
thread.join()