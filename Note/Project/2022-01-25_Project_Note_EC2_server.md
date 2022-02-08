# Project Note : AWS EC2 server



## 서버 구축 

### 1. 서버 구축 방식

1. 온프레미스 (IDC) 

2. 클라우드 

   AWS EC2 with pem key 



### 2. CLI 를 다룰 수 있는 도구들 

bash, powershell



### 3. 기본 세팅 roadmap

1. EC2 ubuntu server 접속
2. DataBase 구축
3. 웹 서버 설치
4. 프록시 서버 설치 (NGinx)
5. 배포 (npm, docker, Jenkins) 



### 4. 주의사항 !

1. port 22 => ssh port 

2. database 조작 

3. 기록! 

   - 개발 일지 

   - 서버 설정 과정 기록 



## AWS EC2 사용하기 

### AWS EC2 접속

1. Nginx 설치 
2. MySQL 설치 

### Local Workbench 에 Server DB 연결하기 

### Nginx 기본 설정

Front build 파일 위치 설정

```bash
sudo vi /etc/nginx/sites-available/default
=> root /home/ubuntu/dist;

sudo service nginx restart
```

`home/ubuntu/dist` 로 빌드파일 이동 



Https 설정 (SSL, Key, request 등)

proxy 설정

### 수동 배포하기 

```bash
ps -ef | grep <jar-name>.jar 
kill -9 <PID>

sudo service nginx restart
nohup java-jar <jar-name>.jar &
```
