**CPU-BOUND WORK**

*GIL*

- prevents more than one piece of Python bytecode from runinng in parallel
- 파이썬에서는 멀티쓰레드를 사용하는 대신, 서브-프로세스를 생성하여 대안을 마련한다.
- 이렇게하면 각각의 프로세스는 독립된 인터프리터와 GIL을 가질 수 있다.
- 