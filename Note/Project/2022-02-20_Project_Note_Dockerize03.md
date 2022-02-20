# Project Note : Dockerize 03

Dockerize 02 글에 이어.. 

MySQL 컨테이너 생성 시 보안 설정이 매우 미흡하다는 사실을 알게 되었다. (프로젝트 발표 직전 해킹 공격을 받아, MySQL 데이터베이스가 모두 삭제되고 비트코인을 요구하는 글이 작성된 것을 확인..ㅠ)

급하게 보안을 강화할 수 있는 방법을 찾아 적용하고 컨테이너를 다시 생성했다. 

기존 docker-compose.yml 

```yaml
version: '3' 
services: 
  node: 
    build: . 
    ports: 
      - "8000:8000" 
    expose:
      - "8000" 
    links: 
      - mysql 
    depends_on: 
      - mysql 
  mysql: 
    image: "mysql" 
    ports: 
      - "3306:3306" 
    volumes:
      - ./db/:/docker-entrypoint-initdb.d
    environment: 
      MYSQL_ALLOW_EMPTY_PASSWORD: "true" 
      # 현재 프로젝트에서는 패스워드 설정 따로 없이 진행.
    expose: 
      - "3306"
```

- MySQL 루트 계정 뿐 아니라, init.db 에서 생성한 계정도 패스워드를 지정하지 않은 상태였기 때문에.. 누구나 데이터베이스에 접속할 수 있었다. 

아래는 다시 작성한 docker-compose.yml 

```yaml
# node 부분 생략
# ... 
  mysql:
    image: "mysql"
    ports:
      - "3306:3306"
    volumes:
      - ./db/:/docker-entrypoint-initdb.d
    environment:
      - MYSQL_ROOT_PASSWORD=root!123!
      - MYSQL_USER=user1
      - MYSQL_PASSWORD=user123!
      - MYSQL_DATABASE=vote_platform
    expose:
      - "3306"
```

- root 및 user1 계정의 비밀번호를 설정했다. 
- 이 외에도 포트 번호를 흔한 3306 이 아닌 다른 포트 번호로 변경하는 것도 도움이 될 것으로 보인다. 

node 의 `utils/mysql.js` 도 아래와 같이 연결이 가능하도록 수정했다. 

```javascript
const mysql = require("mysql2/promise");

const pool = mysql.createPool({
  host: "172.19.0.2",
  user: "user1",
  password: "user123!",
  database: "vote_platform",
  connectionLimit: 10,
  queueLimit: 0,
});

module.exports = { pool };
```

*비밀번호 설정 이후 아직까지 같은 공격을 받지 않고 있다. 

그러나, 누군가 node container 에 접속하여 위 `utils/mysql.js` 를 확인한다면, password 가 노출되어 있으므로 언제든 해킹의 위협이 있을 것으로 보인다. 

추가로 아래 작업을 하면 좋을 것 같다. 

>[부여를 통한 보안](https://learntutorials.net/ko/mysql/topic/5131/%EB%B6%80%EC%97%AC%EB%A5%BC-%ED%86%B5%ED%95%9C-%EB%B3%B4%EC%95%88)

1. `GRANT ... TO root@localhost ...` 권한 설정을 통해 다른 서버에서 root 에 엑세스 하지 못하도록 제한한다. 
2. `GRANT ... ON dbname.* ...` 권한 부여를 통해, 사용자에게 특정 데이터베이스만 접근할 수 있도록 제한한다. 

그러나 위 글에서도 설명하듯, 절대적인 보안은 없으며, 단지 해커의 작업을 늦추고 귀찮게 하는 것이 가능하다고 한다!!
