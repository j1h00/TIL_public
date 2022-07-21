# interview technical: retrospect 



## Naver intern 

> 증권사 API 를 사용한건가요?

아니오, 

> 굉장히 복잡한 생성 페이지를 만들었는데, 어떤 부분이 가장 어려웠나요?

> 코드 리뷰를 진행했나요?

> 다른 두 명의 팀원이 React 가 처음이었다고 했는데, 도움을 준 게 있나요?



> 컴포넌트의 재사용성을 고려해본 적 있나요?

코드의 재사용성과 가독성을 올리려면 **관심사의 분리**가 필요합니다. 프로그래밍에서 관심사의 분리란 복잡한 코드를 비슷한 기능을 하는 코드끼리 별도로 관리를 하는 것을 말합니다. UI를 처리하는 코드나 서버 API를 호출하는 코드 또는 DB를 관리하는 코드 같은 것들을 서로 관심사가 다르다고 보고 파일을 분리해서 관리하는 것이 좋습니다.

리액트에서도 마찬가지로 하나의 컴포넌트에서 모든 기능을 구현할 수 없기 때문에, 여러 개의 컴포넌트를 만들어서 조립을 합니다. 이 때, 하나의 폴더 안에 모든 컴포넌트를 만들어서 관리를 하면 시간이 흐를수록 컴포넌트가 많아져서 원하는 컴포넌트를 찾기가 힘들어질 것입니다. 그래서 연관된 컴포넌트끼리 폴더를 만들어서 관리는 것이 컴포넌트를 찾기에 수월합니다.

하지만, 컴포넌트가 분리되다보니 상태값이 여기저기 흩어지고, 중복되는 현상들이 발생할 수 있습니다. 이러한 현상을 개선하기 위해서는 모든 컴포넌트가 상태값을 가지는 것이 아니라 몇개의 컴포넌트로 한정해서 관리를 하는 것이 좋습니다. 그리고 컴포넌트가 상태값이나 비지니스 로직 코드를 가지고 있으면 재사용하기가 힘들기 때문입니다.

**재사용성이 좋은 컴포넌트의 조건**은 아래와 같습니다.

1. 비즈니스 로직이 없다.

2. 상태값이 없다. (단, 마우스 오버와 같은 UI 효과를 위한 상태값은 제외한다.)

> CSR 과 SSR 에 대해 설명해주세요

- >https://proglish.tistory.com/216

  CSR 는 Client side rendering 으로, 클라이언트는 화면을 렌더링하는데 필요한 모든 자원 (CSS, HTML, JS) 를 서버로부터 받게 되고, 이를 이용하여 브라우저에서 HTML 을 완성하고 렌더링하게 됩니다. 처음에 페이지 구성에 필요한 모든 자원을 받아오기 때문에 초기 로딩 속도가 길지만, 그 이후에 사용자의 인터렉션에 의해 필요한 자원이 발생하면, AJAX 요청을 통해 필요한 자원만을 가져오기 때문에 매 요청 시 HTML 을 받아오지 않아도 되는 장점이 있습니다. 

  SSR 은 Server Side Rendering 으로, 서버에서 하나의 정적인 HTML 을 완성하여 클라이언트에 전송하게 됩니다. 이는 CSR 과 다르게 클라이언트에서 어떤 요청이 발생했을 때, 서버에서 항상 완성된 HTML 을 전송해야 하기 때문에, 상대적으로 속도가 느리게 됩니다.   

  @ 선택 기준 => 웹 사이트의 상호작용 빈번함 / 검색 엔진 최적화 / 서버 성능 / 최초 로딩 .. 등등

- >https://miracleground.tistory.com/165

  SSR 말 그대로 서버 쪽에서 렌더링 준비를 끝마친 상태로 클라이언트에 전달하는 방식 (Ready to Render HTML files)

  클라이언트에 전달되는 순간, 이미 렌더링 준비가 되어있기 때문에 HTML 이 즉시 렌더링된다. 그러나, 클라이언트가 자바스크립트를 다운 받기 전에는 사이트 조작이 불가능하다. 

  - 장점 : 검색 엔진 최적화 / 빠른 초기 로딩 
  - 단점 : TTV <=> TTI / 페이지 요청 마다 새로고침 / 페이지 요청 마다 모든 리소스를 준비해서 응답하므로 서버 부담 증가 

  CSR 사용자의 요청에 따라 필요한 부분만 응답 받아 렌더링 하는 방식 

  - 단점 : 검색 엔진 최적화 / 모든 js 파일을 다운 받은 뒤에 렌더링 되므로, 초기 로딩 속도가 느리다. 





> React 에서 SSR 을 적용하기 위해선 어떻게 해야 하나요?

- > https://yceffort.kr/2021/09/react-18-ssr-architecture#ssr%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

  SSR 을 사용하면 서버에서 리액트 컴포넌트를 HTML 로 렌더링 하여 사용자에게 전송할 수 있는데, 링크나 form 입력 같은 아주 기초적인 웹 인터렉션 말고는 할 수 있는게 별로 없지만, 사용자는 JS 코드가 완전히 로딩되는 동안 최소한 빈 페이지가 아닌 최소한의 콘텐츠는 볼 수 있다. 

  리액트와 프로그램의 코드가 모두 로드되면, HTML 을 다시 인터랙션 가능한 상태로 만드려고 하는데, 이 때 리액트는 서버사이드에서 생성된 페이지에 이벤트 핸들러를 붙이고, DOM 노드를 생성하는 대신 이미 생성되어 있는 HTML 에 로직을 붙여 나간다.

  이처럼 컴포넌트를 렌더링하고 이벤트 헨들러를 연결해주는 이 프로세스를 hydration 이라고 부른다. (dry 한 HTML 에 인터랙션이 가능한 water 를 준다 !!!)

  @ 오늘날 SSR 의 문제점?

  1. 모든 fetch 가 끝나야 뭐라도 보여줄 수 있다. => 컴포넌트가 '데이터 대기 상태'를 허용하지 않는다. 즉 HTML 을 클라이언트에 전송하기 전에 서버에서 모든 데이터가 수집되어 있어야 한다.  
  2. 코드 분할이 없다면, hydration 하기 전까지 모든 자바스크립트를 로딩해야 한다. 
  3. hydration 이 끝나야 상호작용이 가능하다. 

  즉 정리하면, 아래 작업이 폭포수 처럼 작용하고, 이전 단계가 완료되기 전까지 실행될 수 없기 때문이다. 

  1. 데이터 가져오기 (서버)
  2. HTML 렌더링 (서버)
  3. 자바스크립트 로드 (클라이언트)
  4. hydration (클라이언트)

  따라서, 리액트는 해결책으로, 어플리케이션 전체에 걸쳐 이 작업이 일어나는 것이 아니라, 화면의 각 부분이 이 작업을 단계별로 수행하도록 작업을 분리하도록 한다. 

  리액트 18에서는 `Suspense` 활용한 두가지 SSR 기능을 제공한다. 

  - 서버에서 HTML을 스트리밍. 이를 위해 `renderToString` 대신 `pipeToNodeWritable`을 사용해야 한다.
  - 클라이언트에서 선택적 hydration: 이를 위해 `createRoot`를 사용하고 `<Suspense>`로 감싼다.



> JavaScript ES6 부터 사용하기 시작한 문법에 대해 아는대로 말해주세요

1. let, const
2. Promise
3. async await
4. arrow function 
5. map, filter



> var, let, const 에 대해 설명 + 가장 큰 차이에 대해 설명해주세요

> JavaScript 의 비동기 처리 방법 세가지에 대해 설명해주세요.

> event binding 에 대해 설명해주세요

> event delegation 에 대해 설명해주세요

> 코딩 컨벤션에 대해 어떻게 생각하시나요

> 만약 코드를 보고, 이 코드가 누가 작성한 코드인지 구분이 되는 상황이라면, 좋을까요 나쁠까요?

> JTDA 에서 백엔드 관련 개발도 진행했는데, 이 분야에도 관심이 있어서 하신건가요?

> Kafka, Java 등에 대한 사전 지식을 가지고 프로젝트를 진행한건가요?

> 왜 여러 Message Queue 중에 카프카를 사용했나요?

> 왜 Mongo DB 를 사용했나요?

> 이미지 렌더링 최적화 방법에 대해 말해주세요

> 웹 서비스의 성능을 최적화할 수 있는 방법에 대해 말해주세요

> useMemo 와 useCallback 의 차이에 대해 아나요?

> 리턴하는 JSX 요소 내부에 함수를 정의하여 사용하게 되면, 렌더링 될 때마다 함수가 다시 선언되고 실행될텐데,
>
> 이런 코드들은 왜 작성하게 된건가요?

> React 의 장점에 대해 말해주세요

> Virtual DOM 에 대해 말해주세요

> 본인의 불편함을 해결하기 위해 개발한 것이 있나요? (표 자동매매.. 등등)

> 정렬된 상태의 배열이 있다. 이 배열 안의 원소들은 숫자이며, 한 개의 숫자를 제외하고는 모두 두 개 씩 쌍으로 존재한다.
>
> 이 때 배열에서 한 개만 존재하는 숫자를 찾는 방법은?





## Modusign 

> 본인이 진행한 프로젝트에 대한 소개 

>프로젝트를 진행하면서 기술적으로 가장 어려웠던 경험에 대해 설명해주세요 

>백엔드 개발도 해본 것 같은데, 프론트엔드 개발자를 선택한 이유가 뭔가요?

>Next.js 를 사용했는데, SSG, SSR, CSR 에 대해 설명해주세요.

>Vue, React, Angular 와 같은 기술들이 Vanilla JS 에 비해 가지는 장점이 뭐라고 생각하시나요?

>React 컴포넌트를 생성하거나, 구분할 때 어떤 기준에 의해 설계하는 편인가요?

>React 의 동작 방식에 대해 설명해주세요. 

렌더링이란? 

리액트에서 렌더링이란, 컴포넌트가 현재 props와 state의 상태에 기초하여 UI를 어떻게 구성할지 컴포넌트에게 요청하는 작업을 의미한다.

>프로젝트를 진행하면서 코드리뷰를 진행한 경험이 있나요? 

>코드 리뷰를 진행할 때, 주로 어떤 점을 중점적으로 보는 편인가요?

>최근 관심있는 기술이 있나요? 

>그런 기술들을 처음 접할 때, 어떤 방식으로 학습을 하는 편인가요?

>팀원들과 기술적으로 의견 충돌이 있을 떄, 상대를 어떤 방식으로 설득하는 편인가요?



>웹 접근성에 대해 들어본적 있나요?

>REST 라는 개념에 대해 설명해주세요 

>HTTP 와 HTTPS 의 차이에 대해 설명해주세요 

>Vuex 는 어떤 장점이 있었나요?

>Redux 의 장단점에 대해 설명해주세요 

>Context API 를 사용해본 적 있나요?

>Webpack 과 Babel 에 대해 설명해주세요 

>JavaScript 의 이벤트 루프에 대해 설명해주세요

>이벤트 루프를 통한 비동기 처리 단계에 대해 설명해주세요 

>렉시컬 환경에 대해 설명해주세요

>렉시컬 환경과 관련하여, 클로저라는 개념이 있는데, 설명해주세요

> React 에서도 클로저 개념을 사용하는데, 어떤 부분에서 사용되는지 혹시 아시나요?

>Todo List 라이브 코딩 진행..
>
>왜 `todoList` 상태에 왜 배열을 사용했나요?

----

>모두싸인에 지원하신 동기에 대해 말씀해주세요. 

>블로그에 깔끔히 잘 정리를 하신 것 같은데, 본인의 성장을 위해 팀에게 원하는 것이 있나요?

>좋은 개발자, 성숙한 개발자란 뭐라고 생각하시나요

>앞으로 어떤 커리어를 밟아나가고 싶은가요?
