# interview practice 03

- 라이브 엔터테인먼트 플랫폼 나우가 모바일 애플리케이션으로 출시 
- 동시에, 네이버의 영상 콘텐츠 플랫폼인 네이버TV 가 나우 앱으로 통합 

따라서 라이브부터 다시보기 콘텐츠까지 제공 



## 경험 

####  직무 파악 

>사용하는 주언어는 무엇이고, 본인의 수준은 어느 정도라고 생각하는가?
>
>- 본인이 자신있게 말할 수 있는 프로젝트에서의 언어 
>- 언어에 대한 완벽한 이해, 예상 질문, 답변 준비 철저히 
>- 자신감 있게 

JavaScript 입니다. 

변수, DOM 조작, 이벤트 핸들링, Callback, Promise, async & await 을 이용한 비동기 처리, Javascript 엔진의 동작 방식 등에 대한 이해를 갖추고 있습니다. 

>지원 직무에서 어떤 일을 하는지 알고 있는가? 본인의 직무 수행에 있어 강점은 무엇인가?


SSAFY 에서 세 번의 프로젝트를 통해, HTML, CSS, JavaScript, React 에 대한 이해를 얻고, 서비스를 구현해보며 스킬을 연습하면서, 업무를 수행하기 위한 기본적인 자격 요건을 갖추었다고 생각합니다. 

그에 더 나아가서, 재사용 가능한 컴포넌트를 고민하여 구현해보고, 성능 최적화를 위해 더 좋은 코드를 고민해 보는 등의 경험을 통해 더 나은 프론트엔드 역량을 갖추기 위해 노력했습니다. 



>최근에 관심있거나 공부하고 있는 기술은?
>
>- 최신 기술 트렌드
>- 그 회사가 밀고 있는 기술에 대해 이해하면 좋은데, 최근엔 클라우드와 AI 에 관심이 많다. 
>- 개발자 포럼에 참여하여 트렌드 이해하고 공부하면 좋다. 

TDD, 함수형 프로그래밍



#### 어려웠던 점

>겪었던 에러 중에 가장 기억에 남는 에러가 무엇인가요?

어떤 페이지로 이동했다가 빠르게 뒤로가기를 통해 빠져나오는 경우 발생하는 에러였다. 웹 페이지가 동작하는데는 큰 문제가 없고, 특정 상황에만 등장했기 때문에, 우연히 브라우저 콘솔을 통해서 알게 되었다. 

```
Warning: Can't perform a React state update on an unmounted component.
This is a no-op, but it indicates a memory leak in your application.
To fix, cancel all subscriptions and asynchronous tasks in a useEffect cleanup
```

React 사용 시 unmounted component 의 state 의 업데이트를 시도하는 경우에 발생하는 Warning 이다. 

useEffect 내에서 데이터를 fetching 하는 코드를 작성하면서 loading 이라는 이름의 상태 변수를 이용하여 data fetching 완료 여부를 확인했습니다. 

 이 때 만약 컴포넌트가 사라진 이후에 데이터를 가져오게 되어 loading state 를 변경하게 된다면 이 상태를 관리하던 컴포넌트가 사라져 상태 변수를 업데이트 할 수 없게 된다. 

해결 방법은 

1. useEffect cleanup 을 통해 subscription 혹은 asynchronous task 를 모두 취소해주어야 한다.
2. 컴포넌트가 사라지는 시점에 loading 변수를 미리 false 로 변경한다. 

1번 방법이 react 라이프사이클과 useEffect 를 동작 방식에 맞게 잘 이용하는 방법이라고 생각되어 1번으로 해결하였다. 

이를 통해 React Component 의 Lifecycle과 useEffect 내에서 비동기 함수의 동작 방식에 대해 고민하게 되었고, 백엔드에 데이터를 요청하는 간단한 코드라도 React 와 JavaScript 의 동작 방식에 대해 신경써야 함을 알게 되었다. 



>프로젝트하면서 가장 (기술적으로) 어려웠던 경험과 해결했던 경험
>
>- 특정 프로젝트 선택, STAR 기법 사용
>  - 세세하게, 명료하게 기술적으로 설명
>  - 어떤 솔루션이 있고, 어떤 방법을 사용했는지 논리적으로 설명
>- 프로젝트를 하다가 막히는 부분, 해결 방법을 잘 정리해두자

1. JTDA 하면서 java 8 에서, 현재 구동되고 있는 쓰레드 정보를 가져와야 했는데 

   이 때, java.lang 패키지의 Thread 클래스와 

   java.lang.management 에 있는 ThreadMXBean 이라는 두 개의 각기 다른 클래스에서 정보를 가져와 합쳤습니다. 

   

   그런데 나중에 DB 에 저장된 쓰레드 정보를 보니까, 두 클래스에서 가져온 정보가 서로 일치하지 않아 문제가 발생했다는 것을 알게 되었고 

   디버깅을 통해 

   쓰레드가 실시간으로 terminated 상태로 바뀌는 상황에서, 

   한 클래스에서 정보를 가져온 뒤에 다른 클래스 정보를 가져오는 사이에 쓰레드가 terminated 상태가 되어 정보를 가져오지 않는 문제가 발생했다는 것을 알게 되었습니다. 

   서로 동기화가 되지 않았던 것이죠. 

   한 가지 방법은 Java 8 이 아니라 더 높은 버전의 자바를 쓰면 하나의 클래스에서 모든 정보를 가져오는 것이 가능했는데, 요구사항이 Java 8 을 권장하고 있었기 때문에 안되었고 

   다른 한 가지 방법은 예외 처리를 통해 terminated 상태의 쓰레드를 예외처리하여 필터링 하는 방법을 사용했습니다. 



> 팀원들과 협업하며 어려웠던 점이 무엇인가요?
>





## 기술

React 렌더링 최적화 방법 

>[useCallback과 React.Memo을 통한 렌더링 최적화](https://velog.io/@yejinh/useCallback%EA%B3%BC-React.Memo%EC%9D%84-%ED%86%B5%ED%95%9C-%EB%A0%8C%EB%8D%94%EB%A7%81-%EC%B5%9C%EC%A0%81%ED%99%94)

CORS 관련 개념

>[Same-Origin Policy 동일 출처 정책과 CORS 에러](https://velog.io/@yejinh/CORS-4tk536f0db)



