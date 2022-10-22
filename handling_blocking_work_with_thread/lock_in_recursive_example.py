from threading import RLock
from typing import List


class IntListThreadsafe:

    def __init__(self, wrapped_list: List[int]):
        # Lock이 아닌 RLock
        self._lock=RLock()
        self._inner_list=wrapped_list
    def indice_of(self, to_find: int) -> List[int]:
        with self._lock:
            enumerator = enumerate(self._inner_list)
            return [idx for idx, val in enumerator if val== to_find]

    def find_and_replace(self,
                         to_replace: int,
                         replace_with: int):
        with self._lock:
            indices =self.indice_of(to_replace)
            for idx in indices:
                self._inner_list[idx] =replace_with

threadsafe_list = IntListThreadsafe([1,2,3,4,5])
threadsafe_list.find_and_replace(1,2)
print(threadsafe_list._inner_list)