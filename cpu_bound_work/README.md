**CPU-BOUND WORK**
-
*GIL*

- prevents more than one piece of Python bytecode from runinng in parallel
- 파이썬에서는 멀티쓰레드를 사용하는 대신, 서브-프로세스를 생성하여 대안을 마련한다.
- 이렇게하면 각각의 프로세스는 독립된 인터프리터와 GIL을 가질 수 있다.

*process pool*
- 파이썬 병렬 프로세스를 돌릴수 있는 컬랙션. 데이터베이스의 커넥션 풀과 유사한 개념
