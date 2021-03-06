# interview questions

##  프론트엔드 직무 면접 질문 정리 

>[프론트엔드 개발자 면접 정리](https://velog.io/@suyeonme/%ED%9B%84%EA%B8%B0-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%EC%A0%95%EB%A6%AC)
>
>[프론트엔드 면접 준비 하시는 분...?](https://velog.io/@junh0328/%ED%94%84%EB%A1%A0%ED%8A%B8-%EC%97%94%EB%93%9C-%EB%A9%B4%EC%A0%91-%EC%A4%80%EB%B9%84-%ED%95%98%EC%8B%A4%EB%B6%84)



### OS

- 그러나,프로세스가 뭔가요?
  - 컴퓨터에서 실행되고 있는 프로그램
  - 운영체제로부터 자원을 할당받은 작업의 단위 
  - 컴퓨터 메모리에 올라가 있는 동적인 상태의 프로그램

- 스레드가 뭔가요?
  - 프로세스가 할당받은 자원을 이용하는 실행 흐름의 단위 

- 프로세스와 스레드는 어떤 차이가 있나요?
  - 스레드는 프로세스를 구성하는 더 작은 실행 단위의 개념으로, 
    - 프로세스는 메모리에 올라갈 때 운영체제로부터 독자적인 시스템 자원을 할당 받는 반면, 
    - 스레드는 프로세스 내부에서 다른 메모리 영역을 같은 프로세스 내 다른 스레드와 공유한다. 




- 싱글 스레드 장점
  - 자원 접근에 대한 동기화를 신경쓰지 않아도 된다. 
  - context switching 작업을 요구하지 않는다. 

- 싱글 스레드 단점
  - 여러 개의 CPU 를 활용하지 못한다. 

- 멀티 스레드 장점
  - 새로운 프로세스 생성보다는, 기존 프로세스에서 스레드 생성이 빠르다. 
  - 프로세스의 자원과 상태를 공유하여 효율적인 운영이 가능 
  - 프로세스의 작업전환보다 스레드의 작업전환이 빠름 

- 멀티 스레드 단점
  - 운영체제의 지원이 필요, 스레드 스케줄링






### Web etc

- HTTP ?

  - HypterText Transfer Protocol
  - 인터넷 상에서 클라이언트와 서버가 자원(데이터)을 주고 받을 때 쓰는 통신 규약
  - 어플리케이션 계층의 프로토콜이다. 

- HTTPS ?

  - 인터넷 상에서 정보를 암호화하는 SSL 프로토콜을 사용해 클라이언트와 서버가 자원을 주고 받을 때 쓰는 통신 규약
  - HTTPS는 텍스트를 암호화한다. (공개키 암호화 방식으로)

- HTTPS 통신 흐름 

  1. 애플리케이션 서버(A)를 만드는 기업은 HTTPS를 적용하기 위해 공개키와 개인키를 만든다.

  2. 신뢰할 수 있는 CA 기업을 선택하고, 그 기업에게 내 공개키 관리를 부탁하며 계약을 한다.
     - CA (Certificate Authority) : 공개키를 저장해주는 신뢰성이 검증된 민간기업 

  3. 계약 완료된 CA 기업은 해당 기업의 이름, A서버 공개키, 공개키 암호화 방법을 담은 인증서를 만들고, 해당 인증서를 CA 기업의 개인키로 암호화해서 A서버에게 제공한다.

  4. A서버는 암호화된 인증서를 갖게 되었다. 이제 A서버는 A서버의 공개키로 암호화된 HTTPS 요청이 아닌 요청이 오면, 이 암호화된 인증서를 클라이언트에게 건내준다.
  5. 클라이언트는 `main.html` 파일을 달라고 A서버에 요청했다고 가정하자. HTTPS 요청이 아니기 때문에 CA기업이 A서버의 정보를 CA 기업의 개인키로 암호화한 인증서를 받게 된다.
  6. 브라우저는 해독한 뒤 A서버의 공개키를 얻게 되었다. 이제 A서버와 통신할 대는 얻은 A서버의 공개키로 암호화해서 요청을 날리게 된다.

  

- HTTP 프로토콜의 가장 큰 특징은 뭔가요?

  - stateless
    - 데이터를 주고 받기 위한 각각의 데이터 요청이 서로 독립적으로 관리가 된다.
    - TCP/IP 통신 위에서 동작하며 기본 포트는 80번이다.  
  - Connectionless 
    - 클라이언트와 서버가 한 번 연결을 맺은 후, 클라이언트 요청에 대해 서버가 응답을 마치면 맺었던 연결을 끊어버리는 성질
    - 만약 서버에서 다수의 클라이언트와 연결을 계속 유지해야 한다면, 이에 따른 많은 리소스가 발생

- URL은 뭔가요?

  - Uniform Resource Locators 
  - 서버에 자원을 요청하기 위해 입력하는 영문 주소. 숫자로 되어 있는 IP 주소보다 기억하기 쉽다.

  - 브라우저는 URL HTTP 요청을 DNS(Domain Name System) 을 통해 host 에 해당하는 실제 IP 주소로 변환하여 서버에 요청

  

- HTTP/1.1 과 HTTP/2.0의 차이는 뭔가요?

  - HTTP/1.0 은 기본적으로 한 연결당 하나의 요청을 처리하도록 설계되어, 서버로부터 리소스 요청과 응답이 개별적으로 전송되어, TCP 의 3-way-handshake 를 계속해서 열게되고, RTT 가 증가하는 단점이 있다. 

  - HTTP/1.1 은 매번 TCP 연결을 하지 않고, 한 번 TCP 초기화 이후에 여러 개의 파일을 송수신 하는 keep-alive 옵션이 표준화되어 기본 옵션으로 설정되었다. 그러나 마찬가지로 동시 전송은 안되므로, 요청하는 리소스 개수에 비례해서 응답 시간도 증가한다. 

  - HTTP/2.0 은 커넥션 당 여러 개의 요청과 응답이 가능하다. 즉 다중 요청/응답이 가능하다. 

    - 멀티플렉싱, 헤더 압축, 서버 푸시, 요청 우선순위 처리를 지원 

      

- HTTPS는 HTTP랑 뭐가 다른가요?

  - 애플리케이션 계층과 전송 계층 사이에 신뢰 계층인 SSL/TLS 계층을 넣은 신뢰할 수 있는 HTTP 요청을 말한다. 이를 통해 통신을 암호화한다. 
  - 클라이언트 서버 통신 시, 제 3자가 메시지를 도청하거나 변조하지 못하도록 한다. 
  - 보안 세션을 기반으로 데이터를 암호화하며, 인증 메커니즘, 키 교환 암호화 알고리즘, 해싱 알고리즘을 사용

- HTTPS 통신 흐름

1. 애플리케이션 서버(A)를 만드는 기업이 HTTPS 를 적용하기 위해 공개키와 개인키를 생성

2. 신뢰할 수 있는 CA 기업을 선택하여 공개키 관리를 부탁하며 계약을 한다. 
3. CA 기업은 해당 기업의 이름, A서버 공개키, 공개키 암호화 방법을 담은 인증서를 만들고, 해당 인증서를 CA 기업의 개인키로 암호화하여 A서버에 제공한다. 
4. A서버는 암호화된 인증서를 획득했다. 이제 A 서버는 공개키로 암호화된 HTTPS 요청이 아닌 다른 요청이 오면, 이 암호화된 인증서를 클라이언트에 건내준다. 
5. 이 때 클라이언트는 CA 기업의 개인키로 암호화된 인증서를 받게 된다. 
6. 브라우저는 이를 해독하여 A 서버의 공개키를 얻게 되고, 이제 A서버와 통신할 때는 얻은 공개키로 암호화한 요청을 날리게 된다. 



- 심화) 공개키 (비대칭키) 방식이 뭔가요?
  - 인증 메커니즘은 CA(Certificate Authorities) 에서 발급한 인증서를 기반으로, 클라이언트에 공개키를 제공하고, 사용자가 접속한 서버가 신뢰할 수 있는 서버임을 보장한다. 
  - 클라이언트와 서버 모두가 개인키와 공개키를 생성하면 이를 결합하여, 암호화 알고리즘에 의해 PSK(Pre-Shared Key) 를 생헝한다. 



- 쿠키, 세션을 왜 쓰나요?

  - HTTP 프로토콜의 특성이자 약점을 보완하기 위해서 쿠키 또는 세션을 사용합니다.

    기본적으로 HTTP 프로토콜 환경은 "connectionless, stateless"한 특성을 가지기 때문에 서버는 클라이언트가 누구인지 매번 확인해야합니다. 이 특성을 보완하기 위해서 쿠키와 세션을 사용하게됩니다.\
    
    

- 쿠키가 뭔가요?

  - 클라이언트(브라우저) 로컬에 저장되는, 만료기한이 있는 키-값이 들어있는 작은 데이터 파일.
  - `document.cookie` 로 쿠키를 볼 수 없게 `httponly` 옵션을 거는 것이 중요하며, 4KB 까지 저장 가능하다. 
  - 동작순서 
    - 클라이언트가 페이지를 요청하면, 웹 서버는 쿠키를 생성
    - 생성한 쿠키에 정보를 담아 클라이언트에게 HTTP 화면을 돌려줄 때, 같이 돌려준다.
    - 클라이언트는 넘겨 받은 쿠키를 저장하고, 다시 서버에 요청할 때 요청과 함께 쿠키를 전송한다. 
    - 동일 사이트 재방문 시 클라이언트의 PC 에 해당 쿠키가 있는 경우, 요청과 함께 쿠키를 전송

  - 브라우저에 저장되므로 보안에 약할 수 있다. 

  

- 세션이 뭔가요?

  - HTTP 세션은 클라이언트가 웹 서버에 연결된 순간부터 웹 브라우저를 닫아 서버와의 HTTP 통신을 끝낼 때 까지의 기간이다. 
  - 세션 스토리지는 만료 기한이 없는 키-값 저장소이며, 탭 단위로 세션 스토리지를 생성하며 탭을 닫을 때 해당 데이터가 삭제된다. 5MB 까지 저장이 가능하다. 
  - 서버에 세션 객체를 생성하며, 각 클라이언트마다 고유한 세션 ID 값을 부여한다. 
  - 쿠키를 사용하여 세션 ID 값을 클라이언트에 보내고, 웹 브라우저가 종료되면 세션 쿠키는 삭제된다. 
  - 동작순서 
    - 클라이언트 페이지가 요청 
    - 서버가 클라이언트마다 개별적인 세션 ID 를 부여
    - 클라이언트는 요청할 때마다 세션 ID 를 서버에 전달
    - 서버는 받은 세션 ID 로 클라이언트 정보를 가져와 활용

- 쿠키와 세션의 차이는 어떤 점이 있을까요?

  - 저장위치 => 클라이언트 / 서버 

  - 보안

    - 쿠키는 브라우저 로컬에 저장되기 때문에 변질되거나, 요청 시 갈취당할 수 있어 보안에 취약 / 
    - 세션은 쿠키를 이용해서 세션 id 만 저장하고, 그것으로 구분해서 서버에서 처리하기 때문에 비교적 안전

  - life cycle

    - 쿠키는 만료 시간은 있지만, 파일로 저장되기 때문에 브라우저를 종료해도 정보가 남아있다. 
    - 세션은 만료 기간을 정할 수는 있지만, 브라우저가 종료되면 그에 상관없이 삭제된다. 

  - 속도 

    - 쿠키는 정보를 포함하기 때문에 서버에 요청시 속도가 빠르다. 
    - 세션은 정보는 서버에 있기 때문에, 처리가 요구되어 비교적으로 느리다. 

    

- CORS가 뭔가요?
  - Cross Origin Resource Sharing (교차 출처 공유)
    - Origin 은 프로토콜, 호스트 이름, 포트의 조합을 말한다. 
      - 즉, scheme, host, port 로 이루어진 도메인을 의미한다. 

  - 서버가 웹 브라우저에서 리소스를 로드할 때, 다른 오리진을 통해 로드하지 못하게 하는 HTTP 헤더 기반 메커니즘
    1. 현재 자신이 속한 출처(Origin) 을 기준으로 다른 출처(Origin) 에 API 를 요청하게 되면 브라우저에서 이 요청으로 넘어오는 경과가 안전한지 판단하게 된다. 
    2. 응답을 보내는 출처가 자신이 속한 출처가 아닌, 다른 출처여도 서로 예상되는 출처라면, 요청에 대해 허용해주는 응답 헤더를 보내, 브라우저가 결과를 보여준다.  
  - Origin이 다른 http 통신에서는 request header에 쿠키가 자동으로 들어가지 않기 때문에 서버에게 또는 클라이언트에게 내가 어떤 요청을 보내는 지 알려줘야 한다. 
  - 추가 
    - 추가 HTTP 헤더를 사용하여, 한 출처(origin) 에서 실행 중인 웹 애플리케이션이 다른 출처(origin) 의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제입니다.
    - 웹 애플리케이션은 리소스가 자신의 출처(도메인, 프로토콜, 포트)와 다를 때 교차 출처 HTTP 요청을 실행합니다.

- REST
  - 즉, REST는 **HTTP를 기반으로 클라이언트가 서버의 리소스에 접근하는 방식을 규정한 아키텍처고,** REST API는 **REST를 기반으로 서비스 API를 구현한 것을 의미한다.**




- 웹팩이란?

  - 최신 프론트엔드 프레임워크에서 가장 많이 사용되는 모듈 번들러(Module Bundler)
    - 모듈 번들러는, 웹 어플리케이션을 구성하는 자원 (HTML, CSS, JavaScript, Images 등) 을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물을 만드는 도구이다. 

- 모듈이란?

  - 프로그래밍 관점에서, 특정 기능을 갖는 작은 코드 단위 (성격이 비슷한 기능들을 하나의 의미있는 파일로 관리하면 모듈이 된다.)

- 모듈 번들링이란?

  - 웹 어플리케이션 구성 자원들을 하나의 파일로 병합 및 압축해주는 동작 
  - 파일들의 연관된 관계를 파악하여, 파일들을 하나의 파일로 압축시켜주는 과정

- 웹팩이 등장한 이유 웹팩 사용 시에 이점

  - 웹 개발 작업 자동화 도구 

    1. 개발 시, 텍스트 편집기에서 코드 수정 후 새로고침 
    2. 배포 시, HTML, CSS, JS 압축, 이미지 압축, CSS 전처리기 변환 

  - 웹 어플리케이션의 빠른 로딩 속도와 높은 성능 

    - 모듈 번들링을 통해, 해당 파일을 하나로 묶으므로 적은 HTTP 요청으로도 자원을 불러올 수 있다. 

       

- 바벨이란?

  - Javascript 에서 지원하는 최신 문법들을 최대한 많은 브라우저 환경에서 호환이 가능하도록 변환(Transpile)해주는 언어 

  - 트랜스파일: 한 언어로 작성된 소스 코드를 비슷한 수준의 추상화를 가진 다른 언어로 변환 

  - ex) ES6 이후의 문법을 브라우저에서 범용적으로 사용되는 문법으로 변환 

    `() => {}` => `function () {}`

- 웹팩의 주요 속성 4가지

  - entry: 최초 진입점이자, 빌드를 할 대상 파일의 위치 
  - output: 결과물의 파일 경로와 이름 지정 
  - loader: Javascript 이외의 웹 자원(HTML, CSS, images, fonts) 을 output 에 포함될 수 있도록 도와주는 속성 
  - plugin: 결과물의 형태를 바꾸는 역할



### HTML / CSS 

- `DOCTYPE` 
  - HTML이 어떤 버전으로 작성되었는지 미리 선언해, 웹브라우저가 내용을 올바로 표시할 수 있도록 해주는 것입니다.
- meta 태그 
  - HTML 문서가 어떤 내용을 담고 있고, 키워드는 무엇이며, 누가 만들었는지에 대한 정보를 담고있는 태그이다.
- semantic 태그 
  - 서로 관계가 있는 정보를 파악하고 콘텐츠가 어떤 맥락 안에 있는지 알기 쉽다.
  - 검색엔진을 통해 검색이 잘 될 수 있도록 돕는다.

- 검색엔진 최적화 
  - 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 나올 수 있게 한다



- DOCTYPE에 대하여 설명하시오
- 쿼크 모드, 표준 모드를 사용해야 하는 이유
- 쿼크모드가 무엇일까요?
- 표준모드란 무엇일까요?

- 반응형 웹의 3요소 
  - 그리드 레이아웃
  - 가변형 이미지
  - 미디어 쿼리

- `CSS-in-JS`
  - CSS-in-JS는 CSS 모델을 문서 레벨이 아니라 컴포넌트 레벨로 추상화 한다.(모듈성)
  - 자바스크립트와 CSS 사이의 상수와 함수를 공유
  - 현재 사용 중인 스타일만 DOM에 포함

- DOM
  - HTML 문서의 계층적 구조와 정보를 표현하며 이를 제어할 수 있는 API, 즉 프로퍼티와 메서드를 제공하는 트리 자료구조다.
- 브라우저의 동작 원리
  1. HTML 마크업을 처리하고 DOM 트리를 빌드한다. (**"무엇을"** 그릴지 결정한다.)
  2. CSS 마크업을 처리하고 CSSOM 트리를 빌드한다. (**"어떻게"** 그릴지 결정한다.)
  3. DOM 및 CSSOM 을 결합하여 렌더링 트리를 형성한다. (**"화면에 그려질 것만"** 결정)
  4. 렌더링 트리에서 레이아웃을 실행하여 각 노드의 기하학적 형태를 계산한다. (**"Box-Model"** 을 생성한다.)
  5. 개별 노드를 화면에 페인트한다.(or 래스터화)



### Javascript 

변수를 선언할 때는 `var`, `let`, `const` 키워드를 이용하며, 뒤에 오는 변수 이름으로 새로운 변수를 선언한다. 

변수 선언에 의해 확보된 메모리 공간은 자바스크립트 엔진에 의해 암묵적으로 undefined 라는 값이 할당되어 초기화된다. 

#### 변수 / 객체

- 호이스팅
  - 자바스크립트는 변수 선언이 소스 코드의 어디에 있든 상관 없이 다른 코드보다 먼저 실행한다. 
  - 런타임 이전에 실행 컨텍스트에 의해 스코프에 등록되고, 변수가 어디에 위치하던지 상관 없이 변수를 참조할 수 있는 것처럼 만드는 특징을 말합니다. 

- `var` 의 특징
  - 변수 중복 선언 가능 
  - 함수 레벨 스코프 
  - 변수 호이스팅 
- `let` 의 특징 (ES6에 처음 도입)
  - 변수 중복 선언이 금지
  - 블록 레벨 스코프 
  - 변수 호이스팅 
    - `let`으로 선언한 변수는 `선언` 과 `초기화` 단계가 분리되어 진행되며, 변수 선언문에 도달했을 때 초기화 단계가 실행된다. 따라서 초기화 단계 이전에 변수에 접근하면 참조 에러가 발생합니다. 
    - TDZ (Temporal Dead Zone) : 스코프의 시작 지점부터 변수 선언문(초기화 단계 시작 시점) 까지, 변수를 참조할 수 없는 구간 
  - `let` 으로 선언한 전역 변수는 전역 객체의 프로퍼티가 아니다 
- `const` 의 특징 
  - 선언과 동시에 초기화 해야 한다. 
  - 재할당 금지
    - 따라서 원시 값이 변경 불가능하므로 상수 표현에 사용한다. 
- 정적 타이핑
  - 변수 선언 시, 데이터 타입을 사전에 선언해야 하는 것을 명시적 선언이라 한다. 
  - 정적 타입 언어는 변수의 타입을 변경할 수 없고, 타입에 맞는 값만 할당할 수 있다. 
  - 반면, 자바스크립트는 동적 타이핑으로 변수의 타입이 재할당에 의해 언제든 바뀔 수 있다. 
- 고차함수 
  - 함수를 인수로 전달받거나 반환하는 함수를 말함.
  - 자바스크립트의 함수는 일급 객체이므로 함수를 값처럼 인수로 전달하고 반환할 수 있다. 

- 객체 
  - 원시값을 제외한 나머지 값(함수, 배열 등) 이 모두 객체이며, 원시 타입이 단 하나의 값만 나타내지만 객체 타입은 다양한 타입의 값을 하나의 단위로 구성한 복합 자료구조이다. 
  - 객체는 프로퍼티로 구성되며, 프로퍼티는 키와 값으로 구성된다. 
- 메서드 
  - 프로퍼티의 값이 함수일 경우 일반 함수와 구분하여 메서드라 부른다. 

- call by value
  - 변수에 원시 값을 갖는 변수를 할당하면, 윈시 값이 복사되어 전달된다. 
- call by reference
  - 객체를 가리키는 변수를 다른 변수에 할당하면 원본의 참조값이 복사되어 전달된다. 
  - 객체의 프로퍼티는 추가적으로 추가 삭제되는데, 따라서 객체는 메모리 공간의 크기를 사전에 정해둘 수 없가. 이러한 가변성 때문에 객체를 할당한 변수가 기억하는 메모리 주소를 통해 메모리 공간에 접근하여 참조 값에 접근할 수 있다. 

#### 함수 

- 함수 정의 방법

  - 함수 선언문 
  - 함수 표현식
  - Function 생성자 함수
  - 화살표 함수  

  ```js
  case 1 :함수 선언문
  
  function add(x,y){
    return x+y;
  }
  
  case 2: 함수 표현식
  var add = function(x,y){
    return x + y;
  }
  
  case 3: Function 생성자 함수
  var add = new Function('x','y', 'return x+y');
  
  case 4: 화살표 함수(ES6)
  var add = (x,y) => x+y;
  ```

  - 함수 선언문 작성시, 함수 호이스팅에 의해 선언과 할당까지 완료된 상태로, 함수 선언문 이전에 참조와 호출이 가능하다. 

- 스코프 

  - 식별자(변수)가 유효한 범위 
  - 렉시컬 스코프
    - 함수의 호출 위치가 아니라, 정의한 위치에 따라 함수의 상위 스코프를 결정한다. 

- 전역 변수 

  - 암묵적 결합
  - 변수의 긴 생명주기
  - 스코프 체인 상에서 종점에 존재
  - 네임스페이스 오염

- 생성자 함수 

  - 생성자 함수란 new 연산자와 함께 호출하여 객체를 생성하는 함수를 말한다. 생성자 함수에 의해 생성된 객체를 인스턴스라고 한다.
  - 객체를 생성하기 위한 템플릿처럼 생성자 함수를 사용하여 프로퍼티 구조가 동일한 객체 여러 개를 간편하게 생성할 수 있다.

- 일급 객체 

  1. 무명의 리터럴로 생성할 수 있다. (함수 이름 없이)
  2. 변수나 자료구조(객체, 배열 등)에 저장할 수 있다.
  3. 함수의 매개변수에 전달할 수 있다.
  4. 함수의 반환 값으로 사용할 수 있다.

  - 함수형 프로그래밍을 가능하게 한다. 

    - **순수 함수를 통해 부수효과를 최대한 억제하여 오류를 피하고 프로그램의 안전성을 높이려는 프로그래밍 패러다임**

    - 어떤 외부 상태에 의존하지도 않고 변경하지도 않는, 즉 부수 효과가 없는 함수를 순수 함수라 한다.

- this

  - this는 자신이 속한 객체 또는 자신이 생성할 인스턴스를 가리키는 자기 참조 변수이다.

  - 단 this가 가리키는 값, 즉 this 바인딩은 함수 호출 방식에 의해 동적으로 결정된다.

| 함수 호출 방식                                             | this 바인딩                                                  |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| 일반 함수 호출                                             | 전역 객체(window/ global)                                    |
| 콜백 함수 호출                                             | 전역 객체(window/ global)                                    |
| 내부 함수 호출                                             | 전역 객체(window/ global)                                    |
| 메서드 호출                                                | 메서드를 호출한 객체                                         |
| 생성자 함수 호출                                           | 생성자 함수가 (미래에) 생성할 인스턴스                       |
| Function.prototype.apply/call/bind 메서드에 의한 간접 호출 | Function.prototype.apply/call/bind 메서드에 첫 번째 인수로 전달한 객체 |



- 실행 컨텐스트 

  - **실행 컨텍스트는 ① 실행 컨텍스트 스택과 ② 렉시컬 환경으로 구성되어 있다.**

  **① 실행 컨텍스트 스택은** 코드의 실행 순서를 관리하는 자료구조로, L.I.F.O(Last In First Out) 구조로 들어오는 코드를 관리한다.

  **② 렉시컬 환경은** 모든 식별자와 바인딩된 값, 스코프를 기록 및 관리하는 자료구조이다.

- 클로저 

  - 클로저는 자신이 선언될 당시의 환경을 기억하는 함수
  - 해당 함수의 생명 주기가 종료되더라도 함수의 반환된 값이 변수에 의해 아직 참조되고 있다면 생명 주기가 종료되더라도 (실행 컨텍스트 스택에서 푸시되더라도) 렉시컬 환경에 남아 참조가 가능하다
  - 장점
    - 클로저는 **상태(state)를 안전하게 변경하고 유지하기 위해 사용한다.**
    - 상태가 의도치 않게 변경되지 않도록 상태를 안전하게 **은닉(information hiding)하고 특정 함수에게만 상태변경을 허용하기 위해 사용한다.**

  ```js
  var name = `Global`;
  function outer() {
    var name = `closure`;
    return function inner() {
      console.log(name);
    };
  }
  
  var callFunc = outer();
  callFunc(); // => 'closure' !!! not 'Global'
  ```

  - 이처럼 외부 함수 호출이 종료되더라도 외부 함수의 지역 변수 및 변수 스코프 객체의 체인 관계를 유지할 수 있는 구조를 `클로저` 라고 한다.



- 디바운스에 대해서 알고 있나요?
  - 디바운스(debounce)는 짧은 시간 간격으로 이벤트가 연속해서 발생하면 이벤트 핸들러를 호출(call)하지 않다가 **일정 시간이 경과된 이후에 이벤트 핸들러가 한 번만 호출되도록 한다.**
  - 즉 디바운스는 **짧은 시간 간격으로 발생하는 이벤트를 그룹화해서 마지막에 한 번만 이벤트 핸들러가 호출되도록 한다.**

#### 비동기

- 비동기 프로그래밍

1. 현재 실행 중인 태스크가 **종료될 때까지 다음에 실행될 태스크가 대기하는 방식** 을 동기(synchronous) 처리 방식이라고 하며
2. 현재 실행 중인 태스크가 **종료되지 않은 상태라 해도 다음 태스크를 곧바로 실행하는 방식** 을 비동기(asynchronous) 처리라고 한다.
3. 대표적으로 타이머 함수인 **① setTimeout/ setInterval ② HTTP 요청 ③ 이벤트 핸들러** 는 비동기 처리 방식으로 동작한다.식

- 이벤트 루프와 테스크 큐 

  - 자바스크립트는 싱글 스레드로 동작하기 때문에 한 번에 하나의 태스크만 처리할 수 있다.  하지만 브라우저가 동작하는 것을 살펴보면 많은 태스크가 동시에 처리되는 것처럼 느껴진다
  - **이처럼 자바스크립트의 동시성을 지원하는 것이 바로 이벤트 루프(event loop)다.**

- 자바스크립트 엔진은 크게 `(1) 콜 스택(call stack)` 과 `(2) 힙(heap)` 이라는 2개의 영역으로 나눈다.

  1. 콜 스택

     - 소스코드(전역 코드 및 함수 코드 등) 평가 과정에서 생성된 실행 컨텍스트가 추가되고 제거되는 스택 자료구조

     - 자바스크립트 엔진은 단 하나의 콜 스택을 가진다

  2. 힙
     - 객체가 저장되는 메모리 공간이다. 콜 스택의 요소인 실행 컨텍스트는 힙에 저장된 객체를 참조한다.
     - 객체는 원시 값과는 달리 크기가 정해져 있지 않으므로 할당해야 할 메모리 공간의 크기를 런타임에 결정(동적 할당)해야 한다. 따라서 객체가 저장되는 메모리 공간인 힙은 구조화되어 있지 않다

- 예를 들어,

  1. 비동기 방식으로 동작하는 setTimeout의 콜백 함수의 평가와 실행은 자바스크립트 엔진이 담당하지만

  2. 호출 스케줄링을 위한 타이머 설정과 콜백 함수의 등록은 브라우저 또는 Node.js가 담당한다

     이를 위해 브라우저 환경은 태스크 큐와 이벤트 루프를 제공한다

  3. 태스크 큐 (task queue/event queue/callback queue)

     - setTimeout이나 setInterval과 같은 비동기 함수의 콜백 함수 또는 이벤트 핸들러가 일시적으로 보관되는 영역이다

  4. 이벤트 루프 

     - 이벤트 루프는 콜 스택에 현재 실행 중인 실행 컨텍스트가 있는지, 그리고 태스크 큐에 대기 중인 함수(콜백 함수, 이벤트 핸들러 등)가 있는지 반복해서 확인한다
     - 만약 콜 스택이 비어 있고 태스크 큐에 대기 중인 함수가 있다면 이벤트 루프는 순차적(FIFO)으로 태스크 큐에 대기 중인 함수를 콜 스택으로 이동시킨다
     - 이때 콜 스택으로 이동한 함수는 실행된다. 즉, 태스크 큐에 일시 보관된 함수들을 비동기 처리 방식으로 동작한다



- Ajax(Asynchronous JavaScript and XML)가 뭔가요 어떤 것을 담당하고 있죠?
  - 자바스크립트를 사용하여 ① 브라우저가 ② 서버에게 비동기 방식으로 데이터를 요청하고, 서버가 응답한 데이터를 수신하여 웹페이지를 동적으로 갱신하는 프로그래밍 방식 을 말한다.
  - Ajax는 브라우저에서 제공하는 호스트 객체 Web API인 XMLHttpRequest 객체를 기반으로 동작한다.
  - Ajax의 등장으로 서버로부터 웹페이지의 변경에 필요한 데이터만 비동기 방식으로 전송받아 웹페이지를 변경할 필요가 없는 부분까지 다시 렌더링하지 않고, 변경할 필요가 있는 부분만 한정적으로 렌더링하는 방식이 가능해졌다.



- 콜백

  - 자바스크립트에서 콜백 함수는 다른 함수의 매개변수로 함수를 전달하고, 어떠한 이벤트가 발생한 후 매개변수로 전달한 함수가 다시 호출되는 것을 의미합니다.
  - 어떤 일을 다른 객체에게 시키고, 그일이 끝나는 것을 기다리지 않고 끝나고 부를 때까지 다른 일을 하는 것을 말합니다. 이 때문에 `동기`가 아닌 `비동기`적으로 처리되는 비동기 방식의 함수라고 할 수 있습니다.

- 프로미스 

  - 전통적인  콜백 패턴은 일명 '콜백 헬'로 인해 가독성이 나쁘고 비동기 처리 중 발생한 에러의 처리가 곤란하며 여러 개의 비동기 처리를 한 번에 처리하는데 한계를 느꼈다.
  - Promise 생성자 함수가 인수로 전달받은 콜백 함수 내부에서 비동기 처리를 수행한다. 이때 비동기 처리가 성공하면 resolve를, 실패하면 reject를 호출한다.

- 제너레이터

  - ES6에서 도입된 제너레이터(generator)는 `① yield 키워드와 ② next 메서드를 통해` 코드 블록의 실행을 일시 중지 (블로킹) 했다가 필요한 시점에 재개할 수 있는 특수한 함수다.

  1. 제너레이터 함수는 함수 호출자에게 함수 실행의 제어권을 양도할 수 있다.
  2. 제너레이터 함수는 함수 호출자와 함수의 상태를 주고받을 수 있다.
  3. 제너레이터 함수를 호출하면 제너레이터 객체를 반환한다.

- async / await 

  - ES8에서는 제너레이터보다 간단하고 가독성 좋게 `비동기 처리를 동기 처리처럼 동작하도록 구현할 수 있는` async/await가 도입되었다.

  - `프로미스를 기반으로 동작`하며, 프로미스의 후속 처리 메서드 없이 마치 동기 처리처럼 프로미스가 처리 결과를 반환하도록 구현할 수 있다.

  - async

    - 언제나 프로미스를 반환한다.

      async 함수가 명시적으로 프로미스를 반환하지 않더라도 async 함수는 암묵적으로 반환 값을 resolve하는 프로미스를 반환한다.

  - await 

    - await 키워드는 프로미스가 **settled 상태(비동기 처리가 수행된 상태)** 가 될 때까지 대기하다가 settled 상태가 되면 프로미스가 resolve한 처리 결과를 반환한다.

### TypeScript

- Why?
  - 정적 타이핑을 지원, 타입을 지정하고 먼저 타입을 선언함으로써, 프로그래밍 단계와 HTTP 통신을 통해 데이터를 주고 받는 과정에서 생기는 데이터를 안전하게 주고 받을 수 있다. 
  - 타입에 관련된 프로토타입 메서드도 손쉽게 찾아 쓸 수 있다. 

- Type 과 Interface 의 차이 
  - `&` vs `extends` 키워드를 통한 확장
  -  인터페이스는 동일한 이름으로 재정의할 시, 선언적 확장이 가능하다. 

### React 

- 프레임워크 vs 라이브러리 
  - 프레임워크는 Application 개발 시, 코드의 품질, 필수적인 코드, 알고리즘, 암호화, 데이터베이스 연동 등의 기능들이 어느 정도 구성되어 있는 뼈대(구조)를 제공
  - 라이브러리는 특정 기능에 대한 API (도구 / 함수)를 모은 집합 
  - 라이브러리를 사용하는 애플리케이션 코드는 애플리케이션 흐름을 직접 제어하고, 동작하는 중에 필요한 기능이 있을 때 능동적으로 라이브러리를 사용할 뿐이다. 반면에 프레임워크는 거꾸로 애플리케이션 코드가 프레임워크에 의해 사용되어, 프레임워크가 짜놓은 틀에서 수동적으로 동작해야 한다. 
- React 의 특징
  1. 컴포넌트 기반의 화면 구성 
  2. Virtual DOM 으로 인한 충분히 빠른 속도 
     - Virtual DOM (VDOM)은 UI의 이상적인 또는 “가상”적인 표현을 메모리에 저장하고 ReactDOM과 같은 라이브러리에 의해 “실제” DOM과 동기화하는 프로그래밍 개념이 과정을 [재조정](https://ko.reactjs.org/docs/reconciliation.html)이라고 합니다.
  3. SPA
     - 서버의 자원을 아끼고, 더 좋은 사용자 경험을 주지만
     - 사용자와 인터렉션이 많은 경우에는 서버의 자원이 많이 사용되고 불필요한 트래픽이 낭비된다. 
- SPA 

  - 한 개의 페이지를 가진 어플리케이션 
  - 초기 데이터를 받아오고, AJAX 필요한 데이터만 그때 그때 받아오기 때문에 상대적으로 서버 요청이 적다. 
  - MPA 는 사용자 클릭과 같은 인터렉션이 발생할 때 마다 새로운 HTML 을 받아와서 페이지 전체를 다시 리로딩 합니다. 

- React 의 장점
  - component 를 사용하여 유지 보수가 용이하고, 최적화된 렌더링이 가능 
  - 생태계가 넓고 다양한 라이브러리 사용 가능 
  - virtual DOM 을 이용한 빠른 렌더링
  - 리액트 네이티브 

- Virtual DOM 

  >복잡한 SPA(싱글 페이지 어플리케이션) 에서는 DOM 조작이 많이 발생해요. 그 뜻은 그 변화를 적용하기 위해 브라우저가 많이 연산을 해야한단 소리고, 전체적인 프로세스를 비효율적으로 만듭니다.
  >
  >자, 이 이부분에서 Virtual DOM 이 빛을 발합니다! 만약에 뷰에 변화가 있다면, 그 변화는 실제 DOM 에 적용되기전에 가상의 DOM 에 먼저 적용시키고 그 최종적인 결과를 실제 DOM 으로 전달해줍니다. 이로써, 브라우저 내에서 발생하는 연산의 양을 줄이면서 성능이 개선되는 것 이지요.

  

- 함수 컴포넌트 vs 클래스 컴포넌트 

  - 클래스 컴포넌트 
    - 객체 지향 프로그래밍의 구조를 띄고, state 를 초기화하기 위해선 생성자 함수를 필요로 한다. 
    - 함수 컴포넌트에 비해 코드가 길어지고 사이즈가 커진다.
    - state 기능 및 라이프 사이클 기능을 사용할 수 있고, 임의 메서드를 정의할 수 있다. 
    - render 함수가 꼭 있어야 한다. 

  -  함수 컴포넌트 
    - hooks 를 사용하여 생성자 함수 필요 없다. 
    - 선언하기 좀 더 편하고, 메모리 자원을 덜 사용한다. 
    - 빌드 시에도, 결과물의 파일 크기가 더 작다. 
    - hooks 를 이용해 라이프사이클 API 사용이 가능해졌다. 
    - 사이드 이펙트를 빈번히 일으키기 때문에, 순수 함수를 지향하는 함수형 프로그래밍과 차이가 있다. 

- state 의 불변성
  - 객체는 실제 데이터 값이 아닌 참조 값을 가지므로, 객체가 복사되어 동일한 참조 값을 가지는 여러 객체 중 하나라도 변경된다면, 모든 객체의 내부 값이 변경된다. 
  - 따라서 객체 혹은 배열 형식의 데이터를 다룰 때, 원본 배열이 변경되는 경우 의도한 동작과 다르게 동작하거나, side effect 가 발생하는 것을 막고자 불변성을 유지해야 한다.  

- 라이프 사이클 

  ![undefined](https://cdn.filestackcontent.com/ApNH7030SAG1wAycdj3H)

  1. 마운트 
     - DOM 이 생성되고 웹 브라우저 상에 나타나는 것 
  2. 업데이트 
     - props 가 바뀔 때 
     - state 가 바뀔 때 
     - 부모 컴포넌트가 업데이트 될 때 
     - `forceUpdate()` 로 강제로 렌더링을 트리거할 때 

  3. 언마운트 
     - 컴포넌트를 DOM 에서 제거하는 것 

- Hooks 의 종류 

  - v 16.8 에 도입된 기능으로, 기존 함수 컴포넌트에서 사용할 수 없었던 다양한 작업 가능

  1. `useState`

     - setState 함수에 파라미터를 넣어 호출하면, 전달받은 파라미터로 상태가 바뀌고 컴포넌트가 리렌더링 된다. 

  2. `useEffect`

     - 리액트 컴포넌트가 렌더링될 때마다 특정 작업을 수행

  3. `useReducer`

     - useState 보다 더 다양한 컴포넌트 상황에 따라 다양한 상태를 다른 값으로 업데이트하고 싶을 때, 
     - 현재 상태, 업데이트를 위해 필요한 정보를 담은 액션 겂을 전달받아 새로운 상태에 반환하는 함수 

  4. `useMemo `

     - 함수 컴포넌트 내부에서 발생하는 연산을 최적화

     - 예를 들어, 숫자를 입력하면 평균을 계산하는 `getAverage` 함수가 있다고 하면, 

       - input 내용이 수정될 때마다 getAverage 함수가 호출되어, 렌더링할 때마다 계산을 하게 되어 비효율적이다. 

       ```javascript
       const avg = useMemo(() => getAverage(list), [list]);
       ```

  5. `useCallback `

     - useMemo 와 비슷
     - 렌더링 성능 최적화 상황에서 사용하며, 만들어뒀던 함수를 재사용할 수 있다. 
     - 첫 번 째 파라미터에는 생성하고 싶은 함수, 두 번 째 파라미터에 배열을 넣으며, 어떤 값이 배뀌었을 때 함수를 새로 생성해야 하는지 명시한다. 

  6. `useRef `
     - DOM 조작을 위해 사용
     - `.current` 속성에 변경 가능한 값을 담고 있는 객체이다. 

- `useCallback` vs `useMemo`
  - 메모이제이션된 함수 vs 값 반환 

- 리액트에서 `setState`는 비동기 동작인가요, 동기동작인가요?
  - 비동기 동작
  - 한 컴포넌트 안에서 여러 state 값을 연속으로 바꿔준다면, 여러 번 비교하고 다시 그리는 비효율적인 일이 발생한다. 
  - 따라서 `setState` 가 비동기 함수로 동작하여 컴포넌트 내의 비동기 함수를 처리하는 콜백큐가 다 비워지면 리렌더링하도록 설계하였다. 
    - 즉, 해당 함수 내에서 동깆거으로 실행되는 함수가 모두 실행된 뒤에 마지막에 setState 를 처리한다. 


- `useLayoutEffect`
  - `useEffect` 는 브라우저가 스크린에 페인팅 작업을 완료한 뒤에 실행된다. 
    - 즉, `useState(0)` 과 같은 초기 useState 의 값이 빈 값이라면, 0 을 출력했다가 `useEffect` 에 의해 값이 채워지는 구조를 가진다. 
  - `useLayoutEffect` 는 이런 문제를 해결하기 위해, 브라우저가 화면에 DOM 을 그리기 전에 이펙트를 수행한다. 
- 리액트의 성능 개선 방법
  - hook 함수 사용
  - 코드 스플리팅 (react.lazy(), Next.js 프레임워크)





- 의존성 배열은 shallow equal, deep equal중 무엇을 하게 되나요?

- props로 전달받은 함수는, props나 상태가 업데이트될 때마다 새로 생성이 됩니다. 이 때 최적화할 수 있는 방법은 어떤게 있나요?

- 다이나믹한 데이터를 받아올 때, useEffect에서 의존성배열을 어떻게 하실건가요?
- React의 hook에 대해서 설명해주세요.
- 주로 어떤 경우에 custom hook을 사용했고, 그로 인해서 얻은 장점이 무엇인가요?
- Styled-components의 퍼포먼스에 대한 이슈에 대해서 경험해보신 적이 있나요?
- 함수형 프로그래밍의 장점은 무엇인가요? (테스트 코드와 연관)
- 최근 진행했던 프로젝트중 어려웠던 부분은, 그리고 어떻게 해결했나요?



### Next.js

- CSR와 SSR의 차이점은?
  - SSR 
    - SSR 은 서버로부터 이미 완전한 HTML 파일을 받아와 페이지 전체를 렌더링합니다.

      - 필요한 데이터나, CSS 같은 것을 모두 적용한 뒤에 HTML 과 JS 를 브라우저에 전달합니다.  

      - 검색 엔진 최적화에 유리하고, 화면을 렌더링 하는데 필수적인 요소를 먼저 가져오기 떄문에, 초기 로딩 속도가 빠릅니다. 
    - 장점 
      - 검색엔진 최적화 
      - 초기 로딩 성능 개선 (첫 렌더링된 HTML 을 클라이언트에게 선달하기 때문에)

  - CSR 
    - 초기화면을 로드할 때는, 필요한 완전한 리소스를 응답하고, 

      - 모든 js 파일을 다운받기 때문에 초기 로딩 속도가 오래걸린다. 
      - 대신에 그 이후부터는 필요한 부분과 변경된 데이터만 가져오기 때문에 속도가 빠릅니다. 
    - CSR 방식은 사용자의 행동에 따라 필요한 부분만 다시 읽어온다. 따라서 서버 측에서 렌더링하여 전체 페이지를 다시 읽어들이는 것보다 빠른 인터렉션을 기대할 수 있다. 서버는 단지 JSON파일만 보내주고, HTML을 그리는 역할은 자바스크립트를 통해 클라이언트 측에서 수행하는 방식이다.
    - 장점  
      - 사용자 경험 

    - 단점
      - 검색 엔진 최적화 

- Next.js 를 사용한 이유 
  - react-router 를 사용하지 않고도, 간편하게 라우팅 경로를 지정할 수 있다. 
    - `<Link/>` 컴포넌트를 통해서, 페이지 간에 매끄러운 이동이 가능 
  - Code Splitting 기능 
    - SPA 특성 상 , 처음에 많은 양의 리소스를 넘겨주는데, 이 때 코드 분할을 통해 
  - SSR 을 통해 SEO 에 강점을 갖는다. 
- Next.js에서 `getStaticProps`, `getServerSideProps`의 차이점은?



