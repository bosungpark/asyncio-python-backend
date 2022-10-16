**CPU-BOUND WORK**
-
*GIL*

- prevents more than one piece of Python bytecode from runinng in parallel
- 파이썬에서는 멀티쓰레드를 사용하는 대신, 서브-프로세스를 생성하여 대안을 마련한다.
- 이렇게하면 각각의 프로세스는 독립된 인터프리터와 GIL을 가질 수 있다.

*process pool*
- 파이썬 병렬 프로세스를 돌릴수 있는 컬랙션. 데이터베이스의 커넥션 풀과 유사한 개념

*shared data and lock*

- 각각의 프로세스는 그 들만의 메모리 영역을 가지고 있다.
- 공유 메모리를 사용할수도 있지만, 가능하다면 공유 메모리는 피하는 것이 좋다.
- 멀티 프로세싱은 value(integer, float, ...)와 array(List[int], List[str], ...)라는 두 가지 타입의 공유 데이터를 제공한다. -> 진짜 타입 이름임..;;

*race-condition*

- 공유자원의 접근 순서가 꼬이면 경쟁상태가 발생할 수 있다.
- 예를 들어, 읽기와 쓰기 연산이 하나의 영역에서 일어날때, 이 과정이 꼬이면(non atomic, non thread-safe) 문제가 발생한다.
- 이런 상황은, 실행의 순서 문제일 뿐, 보통의 버그와 달라 까다롭다.

*lock*

- 공유 데이터를 동기화하면 경쟁상태를 피할 수 있다.
- 명시적으로 하나의 데이터에 하나의 프로세스만 동작하도록 만드는 것도 하나의 방법이다.
- 이 방법을 mutex 또는 lock이라고 부른다.
- 락이 걸린 영역은 임계영역(critical section)이라고 부른다.
- 만약 이미 동작중인 코드가 있다면, 다음 순번은 기다려야 한다.

