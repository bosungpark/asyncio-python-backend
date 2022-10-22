# import asyncio
# from asyncio import AbstractEventLoop
# from concurrent.futures import Future
# from typing import Callable, Optional
#
#
# class StressTest:
#     def __init__(self,
#                  loop: AbstractEventLoop,
#                  url: str,
#                  total_req: int,
#                  call_back: Callable[[int,int],None]):
#         self._completed_reqs:int=0
#         self._load_test_future: Optional[Future]=None
#         self._loop = loop
#         self._url=url
#         self._total_req=total_req
#         self._call_back=call_back
#         self._refresh_rate=total_req//100
#
#     def start(self):
#         future = asyncio.run_coroutine_threadsafe(self.make_reqs(), self._loop)
#         self._loop.call_soon_threadsafe(self._load_test_future.cancel())
#
#     def cancel(self):
#         if