# Project Note : Dockerize project 01

## Intro

>[왜 굳이 도커(컨테이너)를 써야하나요?](https://www.44bits.io/ko/post/why-should-i-use-docker-container#%EB%A7%88%EC%B9%98%EB%A9%B0-%EC%99%9C-%EB%8F%84%EC%BB%A4%EB%A5%BC-%EC%8D%A8%EC%95%BC-%ED%95%98%EB%82%98%EC%9A%94-%EB%B0%98%EB%B3%B5)
>
>[도커(Docker) 입문편](https://www.44bits.io/ko/post/easy-deploy-with-docker#%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B0)
>
>[도커 컴포즈를 활용하여 완벽한 개발환경 구성하기](https://www.44bits.io/ko/post/why-should-i-use-docker-container#%EB%A7%88%EC%B9%98%EB%A9%B0-%EC%99%9C-%EB%8F%84%EC%BB%A4%EB%A5%BC-%EC%8D%A8%EC%95%BC-%ED%95%98%EB%82%98%EC%9A%94-%EB%B0%98%EB%B3%B5)

도커의 기본적인 학습은 위 세개의 글을 참고하면 좋다. 

현재 프론트엔드와 백엔드 서버가 단순히 AWS EC2 (ubuntu) 환경 위에서 실행되고 있는데, 이를 도커로 감싸야한다. 

[Vue.js + Django 프로젝트를 도커화했던 경험](https://github.com/j1h00/TIL_private/blob/master/SSAFY_project_track/2021-12-24_Dokerize_project.md)을 살려, Next.js + Node + MySQL 프로젝트를 도커로 배포해보자!

## install 

### Docker

```bash
# 설치된 docker 가 있는 지 확인
$ docker -v

# EC2 패키지를 통해 설치 
$ sudo apt-get update
$ sudo apt install docker
```

- 구글링 하면 설치 방법이 다양한데, 나의 경우엔 미설치 시에 `docker -v` 명령어를 실행하면, 콘솔에 출력되는 방법으로 설치를 완료했다. 

### Docker Compose

> https://docs.microsoft.com/ko-kr/visualstudio/docker/tutorials/use-docker-compose

Docker Compose 는 단일 명령을 사용하여 여러 개의 컨테이너를 정의하고 실행할 수 있도록 해준다. 

이를 통해 다른 사용자도 프로젝트에 참여하기 쉽게 만들 수 있다!

```bash
# 다운로드 
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 실행 권한 적용 
$ chmod +x /usr/local/bin/docker-compose

# symbolic link 설정 
$ ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# 설치 확인 
$ docker-compose -v
```

## Next.js + NGINX

 Next.js 컨테이너를 NGINX reverse proxy 로 감싸 배포하는 것에 도전하였다. (Reverse Proxy 에 대한 설명은 [Nginx Reverse Proxy 사용하기](https://medium.com/sjk5766/nginx-reverse-proxy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-e11e18fcf843) 참고!). 이 경우, Next.js 컨테이너에 직접 접속하지 않으므로 보안상의 이점이 있고, Cache 사용, 로드 밸런싱 등의 기능도 추가적으로 사용할 수 있다. 

> [Set up Docker and NGINX for a Next.js app](Set up Docker and NGINX for a Next.js app)

위 글을 참고하면, Next.js 프로젝트와 NGINX 를 동시에 컨테이너화하여 구동할 수 있다.  

### Dockerize Next.js 

Next.js 프로젝트 루트폴더에, Next.js 프로젝트의 도커 이미지 생성을 위한 간단한 `Dockerfile` 작성한다. 

```dockerfile
# Base on offical Node.js Alpine image
FROM node:lts-alpine

# Set working directory
WORKDIR /usr/app

# Copy package.json and package-lock.json before other files
# Utilise Docker cache to save re-installing dependencies if unchanged
COPY ./package*.json ./

# Install dependencies
RUN npm install --production

# Copy all files
COPY ./ ./

# Build app
RUN npm run build

# Expose the listening port
EXPOSE 3000

# Run container as non-root (unprivileged) user
# The node user is provided in the Node.js Alpine base image
USER node

# Run npm start script when container starts
CMD [ "npm", "start" ]
```

### NGINX configuration

Next.js 프로젝트 루트 폴더에, 아래와 같이 NGINX 설정을 위한 `nginx/default.conf`을 작성한다. 

```nginx
# proxy-cache 설정 
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=STATIC:10m inactive=7d use_temp_path=off;

# nextjs:3000 컨테이너를 upstream 서버로 설정 
upstream nextjs_upstream {
  server nextjs:3000;
  # We could add additional servers here for load-balancing
}

server {
  listen 80 default_server; # default HTTP 포트 설정
  server_name _;
  server_tokens off;

  gzip on;
  gzip_proxied any;
  gzip_comp_level 4;
  gzip_types text/css application/javascript image/svg+xml;

  # reverse-proxy 설정 
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection 'upgrade';
  proxy_set_header Host $host;
  proxy_cache_bypass $http_upgrade;

  # next.js 가 생성하는 static files 를 cache 하도록 설정  
  location /_next/static {
    proxy_cache STATIC;
    proxy_pass http://nextjs_upstream;

    # For testing cache - remove before deploying to production
    add_header X-Cache-Status $upstream_cache_status;
  }

  # image 같은 statis assets 를 cache 하도록 설정 
  location /static {
    proxy_cache STATIC;
    proxy_ignore_headers Cache-Control;
    proxy_cache_valid 60m; # cahced file 이 60분 동안 유효
    proxy_pass http://nextjs_upstream;

    # For testing cache - remove before deploying to production
    add_header X-Cache-Status $upstream_cache_status;
  }

  location / {
    # nginx가 받은 요청을 nextjs_upstream 으로 전달 
    proxy_pass http://nextjs_upstream;
  }
}
```

- 위 설정 파일은 다음과 같은 내용을 포함한다. 

1. 80번 포트를 default HTTP port 로 설정, 
2. 3000번 포트를 사용하는 nextjs 컨테이너를 upstream 서버로 설정. 
3. nginx 가 받은 요청을 nextjs_upstream 으로 전달 (reverse-proxy)
4. static files  (`_next/static`, `/static`)  를 cache 하도록 설정 
5. `gzip` 명령어를 가능하게 하여, user 에게 compressed file 을 전송 가능하도록 설정.

### Dockerize NGINX

마찬가지로 `/nginx` 폴더에 `Dockerfile` 을 작성한다. (`default.conf` 와 같은 위치)

```bash
# Base on offical NGINX Alpine image
FROM nginx:stable-alpine

# Remove any existing config files
RUN rm /etc/nginx/conf.d/*

# Copy config files
# *.conf files in conf.d/ dir get included in main config
COPY ./default.conf /etc/nginx/conf.d/

# Expose the listening port
EXPOSE 80

# Launch NGINX
CMD [ "nginx", "-g", "daemon off;" ]
```

- 간단! 

### Docker Compose 

처음 설치한 Docker Compose 를 이용하여, Next.js 와 NGINX 컨테이너 생성과 구동을 한번에!

Next.js 루트 폴더에 `docker-compose.yml` 을 작성한다. 

```yaml
version: '3'
services:
  nextjs:
    build: ./
  nginx:
    build: ./nginx
    ports:
      - 80:80
```

- Next.js 와 NGINX 의 `Dockerfile ` 이 위치한 폴더를 빌드 위치로 설정한다. 

docker compose 파일 실행 

```bash
$ docker-compose up 
```

### 이미지 및 컨테이너 확인

```bash
$ docker images
# output example
REPOSITORY           TAG             IMAGE ID       CREATED        SIZE
client_nginx         latest          49e4a8f8152f   42 hours ago   23.2MB
client_nextjs        latest          8ca039ea75a0   42 hours ago   682MB
node                 lts-alpine      0e1547c0f4a4   2 days ago     110MB
nginx                stable-alpine   373f8d4d4c60   2 months ago   23.2MB

$ docker ps -a 
# output example (NAME 생략)
CONTAINER ID   IMAGE         COMMAND                   CREATED        STATUS      PORTS
de9627845b59   client_nginx  "/docker-entrypoint.…"   42 hours ago   Up 42 hours  0.0.0.0:80->80/tcp, :::80->80/tcp    
90e4ce7e44f7   client_nextjs "docker-entrypoint.s…"   42 hours ago   Up 42 hours  3000/tcp                            
```

EC2 서버 주소의 80번 포트로 접속했을 때, 접속 확인 가능!

## 끝!









