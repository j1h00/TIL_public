# Project Note : Dockerize project 02

Dockerize project 01... 이어서 

## Node.js + MySQL 

프론트엔드 배포와 마찬가지로 백엔드 서버로 도커로 배포해보자!

### Dockerize Node.js

Node.js 이미지 생성을 위한 `Dockerfile` 을 작성한다. 

```dockerfile
FROM node:14.18.3

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --production

COPY . .

EXPOSE 8000

CMD [ "node", "server.js" ]
```

- 기존 프로젝트의 node 버전과 같은 버전을 사용.

### Dockerize MySQL 

MySQL Docker 이미지를 다운로드한다. 

```bash
$ docker pull mysql:<version>
```

- 원하는 버전을 다운로드!

### Docker Compose

docker-compose 를 통해 Node.js 와 MySQL 컨테이너를 서로 의존적으로 실행가능하다.  

아래와 같이 `docker-compose.yml` 을 작성한다. 

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
    environment: 
      MYSQL_ALLOW_EMPTY_PASSWORD: "true" # 현재 프로젝트에서는 패스워드 설정 따로 없이 진행.
    expose: 
      - "3306"

```

명령어로 실행 및 확인

```bash
$ docker-compose up 
# ... 
$ docker ps -a 
# output example
CONTAINER ID   IMAGE     COMMAND                  CREATED        STATUS                 PORTS                                                        NAMES
d5887f1d3e5a   be_node  "docker-entrypoint.s…"   41 hours ago   Up 41 hours            0.0.0.0:8000->8000/tcp, :::8000->8000/tcp              be_node_1
791137677c9a   mysql   "/entrypoint.sh mysq…"    41 hours ago   Up 41 hours (healthy)   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060-33061/tcp   be_mysql_1
```

이 시점에서 현재 구동되고 있는 MySQL 컨테이너에는, MySQL user, database 등이 아무것도 없다!!

 MySQL 컨테이너에 접속하여 설정을 완료해야 한다. 

```bash
# 특정 컨테이너에 접속하여 bash shell 열기 
$ docker exec -it <container_id> bash

$ mysql
```

- MySQL 에 접속하여 user privileges 를 설정하고, database 를 생성하여 table 까지 생성해준다.  

### 문제점 해결

그러나 Node 에서 MySQL 서버에 연결하지 못하는 에러가 발생한다. 

기존의 mysql connection 코드 

```js
const mysql = require("mysql2/promise");

const pool = mysql.createPool({
  host: "localhost",
  user: "<user_name>",
  database: "<database_name>",
  writeforConnection: true,
  connectionLimit: 10,
  queueLimit: 0,
});

module.exports = { pool };
```

> [[삽질포함] Docker 따라하기 #4](https://donochi.tistory.com/208)

- 위 글을 참고하여 관련 문제를 해결하였다.  

#### 1. `Error: connect ECONNREFUSED 127.0.0.1:3306` 

mysql createPool 코드에서, host 를 localhost 가 아닌, docker MySQL container 의 IP 로 수정해야 한다. 

`$ docker inspect <container_id>`

위 명령어를 통해 MySQL container 의 IP 주소를 얻을 수 있다. 



#### 2. `Error: ER_NOT_SUPPORTED_AUTH_MODE: Client does not support authentication protocol requested by server; consider upgrading MySQL client`

mysql createPool 코드에서 작성한 user 에게, MySQL 서버에서 권한 부여를 해주어야 한다. 

```bash
$ mysql> grant all privileges on *.* to <user>
```



## 끝!









