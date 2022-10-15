**NON-BLOCKING DATABASE DRIVERS**

*asyncpg*

- aysncio friendly and non-blocking sockets which is suit for postgre db
- if you want to apllicate aysnc in mysql, you can consider aiomysql

*connection pool*
- we can only execute one q in one conn, so we need to manage multiple conn

- connection pool is kind of cache that manage existing conn of db instance
- db conn을 맺는 비용이 크기 때문에, 재사용가능한 풀은 큰 도움이 된다.