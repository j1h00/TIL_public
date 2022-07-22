# interview technical: retrospect 



## Naver intern 

> 증권사 API 를 사용한건가요?

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

- > https://www.w3schools.com/js/js_es6.asp

1. let, const

2. arrow functions

   allows short syntax for writing function expressions

   1. don't need `function` keyword, `return` keyword, and the curly brackets 
   2. do not have their own `this` => not well suited for defining object methods 
   3. not hoisted => must be defined before they are used 

3. for / of 

   loops through value of iterable data structures ( Arrays, Strings, Maps, NodeLists)

4. map object

5. set object 

6. Classes

7. Promises

   Producing Code + Consuming Code 

   producing code should call one of the two callbacks, `myResolve`, `myReject` 

   promise object supports two properties: state (`pending`, `fulfilled`, `rejected`) , result 

   

8. Symbol 

9. Default parameter 

10. function rest parameter 

11. String.includes() / String.startsWith() / String.endsWith()

12. Array.from() / keys() / find() / findIndex() 

> var, let, const 에 대해 설명 + 가장 큰 차이에 대해 설명해주세요

변수를 선언할 때 사용하는 키워드로, 

var 은 재선언과 재할당이 모두 가능하며, 함수 스코프를 가진다.

let 과 const 는 블록 스코프를 가지며, let 은 재선언이 불가능하고 재할당은 가능하다. 

const 는 재선언과 재할당이 모두 불가능하다.  

> JavaScript 의 비동기 처리 방법 세가지에 대해 설명해주세요.

1. callback 을 이용하는 방법

   javascript 에서 callback 함수란, 어떤 함수의 인자로 사용되는 함수를 말하며, 그 함수 내부에서 어떤 이벤트가 발생했을 때 인자로 받은 함수를 실행하도록 할 수 있다.  

2. Promise

   Promise 객체는 비동기 처리를 위해 사용되며, 

   Promise 생성자 함수가 인수로 전달받은 콜백함수 내부에서 비동기 처리를 수행한다. 이 때 비동기 처리가 성공하면 `resolve`, 실패하면 `reject` 를 호출한다. 

   pending, fulfilled, rejected 세 가지 상태를 가지고, fulfilled 와 rejected 상태에 따라 `.then()` 과 `.catch()` 를 통해 각각 다른 후속 처리를 할 수 있다. 

3. async & await

   await 키워드를 통해 어떤 작업의 완료를 기다리게 할 수 있다. Promise 를 기반으로 하지만, 프로미스의 후속 처리 메서드 없이 사용가능하며,

   await 키워드의 이용은 비동기 코드를 동기 코드를 작성하듯 작성하여 가독성이 좋아지고, 

   try catch 를 이용한 에러처리가 가능하다.  

    

> event binding 에 대해 설명해주세요

- >https://cheonmro.github.io/2018/09/03/event-binding-and-event-handler/

  발생하는 이벤트와 그 후에 어떤 일이 벌어질지 알려주는 함수(콜백함수)를 묶어서 연결해준다는 뜻. 

  이 때, 콜백함수를 이벤트 핸들러라고 한다. 이벤트 바인딩에는 대표적으로 3가지 방법이 있다. 

  1. HTML 이벤트 핸들러 

     HTML 과 Javascript 가 혼용되는데, 둘의 관심사가 다르기 때문에 혼용하는 것을 피해야 한다. 

     ```html
     <button onclick="clickBtn()">Click me</button>
     ```

  2. 전통적인 DOM 이벤트 핸들러 

     ```js
     var myBtn = document.getElementById('myBtn');
     
     myBtn.onclick = function () {
       alert('Button clicked 1');
     };
     ```

     이벤트 핸들러에 하나의 함수만을 바인딩 가능 / 함수에 인수 전달 불가, 

  3. Event Listener 를 이용한 이벤트 핸들러

     ```js
     target.addEventListener(type, listener[, useCapture]);
     
     var el = document.getElementById("outside");
     el.addEventListener("click", function(){modifyText("four")}, false);
     ```

     이벤트 핸들러 내부의 this 는 event listener 에 바인딩된 요소(currentTarget) 을 가리킨다. 이는 이벤트 객체의 currentTarget 프로퍼티와 같다. (e.currentTarget)

  

> event delegation 에 대해 설명해주세요

이벤트 위임?

- >https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Events

  버블링은 또한 **이벤트 위임**의 이점을 취할 수 있게 합니다 — 이 개념은 만약 다수의 자식 요소 중 하나를 선택했을 때 코드를 실행하기를 원한다면, 모든 자식에 개별적으로 이벤트 리스너를 설정해야만 하는 것 대신 이벤트 리스너를 그들의 부모에 설정하고 그들에게서 일어난 이벤트가 그들의 부모에게까지 올라오게 할 수 있다는 사실에 의존합니다

- >https://ko.javascript.info/event-delegation

  캡처링과 버블링을 활용하면 강력한 이벤트 핸들링 패턴인 *이벤트 위임(event delegation)* 을 구현할 수 있습니다. 

  이벤트 위임은 비슷한 방식으로 여러 요소를 다뤄야 할 때 사용됩니다. 이벤트 위임을 사용하면 요소마다 핸들러를 할당하지 않고, 요소의 공통 조상에 이벤트 핸들러를 단 하나만 할당해도 여러 요소를 한꺼번에 다룰 수 있습니다.

  공통 조상에 할당한 핸들러에서 `event.target`을 이용하면 실제 어디서 이벤트가 발생했는지 알 수 있습니다. 이를 이용해 이벤트를 핸들링합니다.

- >https://ui.toast.com/weekly-pick/ko_20160826

  고민이 있었다. 그것은 동적으로 추가되는 엘리먼트에 매번 이벤트 리스너를 추가 하는 것에 대한 고민이었다. 10가지 이벤트가 동작하는 기능을 100번 등록하면 이벤트 리스너는 1000번을 추가해야 한다.

  메모리 누수 문제도 그렇다. 애초에 매번 등록하지 않으면 메모리 누수 가능성도 줄어들고 그로 인해 매번 해제하지 않아도 될 것이다. 안타깝게도 그때 당시에는 그 고민을 해결하지 못 했다.

  이벤트 위임의 이점은 다음 4가지로 정리할 수 있다.

  1. 동적인 엘리먼트에 대한 이벤트 처리가 수월하다.
  2. 상위 엘리먼트에서만 이벤트 리스너를 관리하기 때문에 하위 엘리먼트는 자유롭게 추가 삭제할 수 있다.
  3. 이벤트 핸들러 관리가 쉽다.
  4. 동일한 이벤트에 대해 한 곳에서 관리하기 때문에 각각의 엘리먼트를 여러 곳에 등록하여 관리하는 것보다 관리가 수월하다.
  5. 메모리 사용량이 줄어든다.
  6. 동적으로 추가되는 이벤트가 없어지기 때문에 당연한 결과이다. 1000건의 각주를 등록한다고 생각해보면 고민할 필요로 없는 일이다.
  7. 메모리 누수 가능성도 줄어든다.
  8. 등록 핸들러 자체가 줄어들기 때문에 메모리 누수 가능성도 줄어든다.

> 코딩 컨벤션에 대해 어떻게 생각하시나요

- >https://hsunnystory.tistory.com/145

  한마디로 요약하면 내가 작성한 코드를 다른사람들도 쉽게 이해할 수 있게 가독성 있는 코드를 작성하는법에 대한 규칙이다.

   소프트웨어의 유지보수를 그 소프트웨어를 직접 개발한 개발자가 담당하는 경우는 드물다. 코딩 컨벤션은 다른 개발자가 그 소스코드를 처음 보았을 때, 더 빠른 시간에 완벽히 이해할 수 있도록 도와주기 때문에, 코드의 가독성이 높아진다.

- >https://velog.io/@hyundong_kk/%EC%BD%94%EB%93%9C-%EC%BB%A8%EB%B2%A4%EC%85%98

  간이 지난 상태에서 해당 코드를 다시 본다고하면 본인이 작성한 코드일지라도 이해하는데 시간이 걸립니다.

  만약 해당 코드를 다른 사람이 이해하고 활용해야 하는 상황이라면 시간은 더욱 오래걸릴 것입니다. 여러명의 개발자가 하나의 프로젝트에 투입이 되어서 작업을 진행하는 경우 각자의 스타일로 코드를 작성한다고 하면 같은 프로젝트 안에서 다른 개발자의 코드를 이해하고 이해하는데 시간이 소요될것이고 기능을 오해하는 경우가 생길 것입니다. 사전에 코드 스타일을 통일함으로써 이러한 문제들을 해결 할 수 있습니다.

- >https://www.mimul.com/blog/why-we-argue-style/

  코드는 쓰는 횟수보다 읽는 횟수가 훨씬 많다. 그래서 코드의 많은 비용은 읽을 때 발생한다. 그러므로 코드는 가독성을 위해 최적화를 해야 한다는 결론, 즉 응용 프로그램의 코드는 모두 같은 스타일로 통일되어야한다는 결정을 이끌어 낼 수 있다. 일반적인 스타일에 맞춤으로써 여러분은 비용을 절감할 수 있다.

> 만약 코드를 보고, 이 코드가 누가 작성한 코드인지 구분이 되는 상황이라면, 좋을까요 나쁠까요?

- 작성된 스타일이 다르다면, 코드마다 코드를 이해하는 시간에 시간이 더 오래 걸릴 것이다.  

> JTDA 에서 백엔드 관련 개발도 진행했는데, 이 분야에도 관심이 있어서 하신건가요?

> Kafka, Java 등에 대한 사전 지식을 가지고 프로젝트를 진행한건가요?

> 왜 여러 Message Queue 중에 카프카를 사용했나요?

- 팀원들의 사전 기술 스택에 근거를 두고.. 

> 왜 Mongo DB 를 사용했나요?

> 이미지 렌더링 최적화 방법에 대해 말해주세요

- >[이미지 최적화 note](https://github.com/j1h00/TIL_public/blob/bf1fe6a093b2112387ad5b49950a0a6e3fcca2dc/Note/interview/2022-07-13_interview_modusign_practice.md#%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B5%9C%EC%A0%81%ED%99%94)

  raster 이미지 보다는 vector 이미지 / 손실 이미지 사용

  1. 브라우저 사이즈에 맞춰 적절한 이미지 제공 (미디어쿼리, srcset 속성, `<picture>` 태그 사용 등 )
  2. 이미지 lazy loading => 최대한 사용자에게 보이는 부분부터 로드되도록 처리 
  3. 이미지 CDN 
  4. CSS image sprite

  

> 웹 서비스의 성능을 최적화할 수 있는 방법에 대해 말해주세요

- >[useCallback과 React.Memo을 통한 렌더링 최적화](https://velog.io/@yejinh/useCallback%EA%B3%BC-React.Memo%EC%9D%84-%ED%86%B5%ED%95%9C-%EB%A0%8C%EB%8D%94%EB%A7%81-%EC%B5%9C%EC%A0%81%ED%99%94#%EC%99%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EA%B2%83%EC%9D%BC%EA%B9%8C)

  리액트의 경우 아래의 상황에 리렌더링이 발생 

  1. state 변경이 있을 때
  2. 부모 컴포넌트가 렌더링 될 때
  3. 새로운 props이 들어올 때
  4. shouldComponentUpdate에서 true가 반환될 때
  5. forceUpdate가 실행될 때

  1, 2 번의 경우 얕은 비교를 통해 새로운 값인지 판단한다. 

  

> useMemo 와 useCallback 의 차이에 대해 아나요?

- useCallback 은 의존성에 포함된 값이 변경되지 않는다면 이전에 생성한 **함수(참조 값)**을 반환

  현재 하위 컴포넌트에 전달하는 콜백 함수를 inline 함수로 사용하고 있다거나, 컴포넌트 내에서 함수를 생성하고 있다면 *(프로그래밍 구동에는 문제가 없겠지만)* 새로운 함수 참조 값을 계속해서 만들고 있는 것, 다시 말해 똑같은 모양의 함수를 계속해서 만들어 메모리에 계속해서 할당하고 있다는 것을 뜻한다. *이전에 작성한 코드들에 인라인 함수를 보이면 으윽 아악.. 하는 소리가 절로 흘러나온다.*

  useMemo 는 메모이제이션된 값을 반환한다. 

- **useMemo는 함수의 연산량이 많을때 이전 결과값을 재사용하는 목적이고, useCallback은 함수가 재생성 되는것을 방지하기 위한 목적**이



> 리턴하는 JSX 요소 내부에 (인라인으로) 함수를 정의하여 사용하게 되면, 렌더링 될 때마다 함수가 다시 선언되고 실행될텐데,
>
> 이런 코드들은 왜 작성하게 된건가요?

> React 의 장점에 대해 말해주세요

- 컴포넌트 단위 개발, Virtual DOM 을 이용한 렌더링 최적화 ? 

- >[React란? 특징과 장단점 파헤치기](https://velog.io/@jeromecheon/React%EB%9E%80-%ED%8A%B9%EC%A7%95%EA%B3%BC-%EC%9E%A5%EB%8B%A8%EC%A0%90-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0#%EC%9E%A5%EC%A0%90)

  특징

  1. 선언적이다. (Declarative) 
  2. 컴포넌트 기반이다. (Component based) => 캡슐화된 컴포넌트가 스스로 상태를 관리하고, 복잡한 UI 를 효과적으로 구성할 수 있다. 
  3. Learn Once, Write Anywhere => React Native 도 사용 가능

  장점

  1. React 공식 문서 가이드와 방대한 커뮤니티, 자료를 통해 쉽게 접하고 배울 수 있다.
  2. Controller, directive, template, model, view 처럼 로직을 분리하는 것이 아닌, Component 하나로 관리를 한다. (이게 view 역할을 담당)
  3. 성능이 뛰어난 가비지 컬랙터, 메모리 관리 기능을 지원한다.
  4. UI 수정과 재사용성이 좋으며, 코드 가독성을 높일 수 있다.
  5. 다른 framework나 라이브러리와 병행해서 사용할 수 있다. 이는 개발이 이미 완료된 프로젝트에도 적절히 녹여낼 수 있는 확장성도 포함한다.

  

> Virtual DOM 에 대해 말해주세요

- React 에서 렌더링 최적화를 위해, 변경사항을 DOM 에 적용하기 전에 Virtual DOM 이라는 가상의 객체에 먼저 적용한 뒤, 최종 변경사항을 비교하여 실제 DOM 에 적용하게 된다. 이를 reconciliation 이라 부른다!

- >https://velopert.com/3236

  DOM 에 변화가 생기면, 렌더 트리를 재생성하고 레이아웃을 만들고, 페인팅 하는 과정이 다시 반복된다. 

  복잡한 SPA 에서는 DOM 조작이 많이 발생하므로, 브라우저의 연산과 전체적인 프로세스가 비효율적이 된다. 

  만약에 뷰에 변화가 있다면, 그 변화는 실제 DOM 에 적용되기전에 가상의 DOM 에 먼저 적용시키고 그 최종적인 결과를 실제 DOM 으로 전달해줍니다. 이로써, 브라우저 내에서 발생하는 연산의 양을 줄이면서 성능이 개선되는 것 이지요.



 

> 본인의 불편함을 해결하기 위해 개발한 것이 있나요? (표 자동매매.. 등등)

> 정렬된 상태의 배열이 있다. 이 배열 안의 원소들은 숫자이며, 한 개의 숫자를 제외하고는 모두 두 개 씩 쌍으로 존재한다.
>
> 이 때 배열에서 한 개만 존재하는 숫자를 찾는 방법은?





## Modusign 

> 본인이 진행한 프로젝트에 대한 소개 

>프로젝트를 진행하면서 기술적으로 가장 어려웠던 경험에 대해 설명해주세요 

>백엔드 개발도 해본 것 같은데, 프론트엔드 개발자를 선택한 이유가 뭔가요?

>Next.js 를 사용했는데, SSG, SSR, CSR 에 대해 설명해주세요.

- >https://velog.io/@altmshfkgudtjr/CSR-SSR-SSG-%EC%A1%B0%ED%99%94%EB%A5%BC-%EC%9D%B4%EB%A3%A8%EB%8B%A4

  SSG(Static-Site-Generation) => 클라이언트에서 필요한 페이지들을 사전에 미리 준비해뒀다가, 요청을 받으면 이미 완성된 파일을 단순히 반환하여 브라우저에서 뷰를 보여지게 됩니다.
  
  - 이미 Pre-rendering된 정적 파일이 있으므로, 서버에서는 단지 그 파일을 클라이언트로 전달해줄 뿐이어서 정말 빠릅니다. 그렇지만, 웹 서비스에 존재하는 수많은 페이지들을 전부 정적 파일로 만들어주기에는 현실적으로 무리가 있어 보입니다.
  
  SSR(Server-Side-Rendering) => 서버에서 뷰 구성에 필요한 전체 HTML을 요청을 받은 즉시 생성해서 반환합니다. 이렇게 하면 클라이언트 브라우저에서 응답을 받은 후, 이미 완성된 뷰를 그대로 보여지게 됩니다. 
  
  - 페이지 전환 간에 깜빡임 현상이 발생 (페이지 이동할 때마다 서버에서 렌더링해주는 새로운 파일을 받기 때문)
  
  CSR(Client-Side-Rendering) => 클라이언트 브라우저에서 어플리케이션을 렌더링을 진행합니다. 즉 어플리케이션 구동에 필요한 HTML, JS, CSS 파일 등을 모두 다운로드 한 뒤에 뷰가 구성되게 됩니다.
  
  초기 렌더링과 이후 렌더링 방식을 나누어 각각의 상황에 맞게 사용하는 것이 중요하다. 
  
  - 예를 들어, 쇼핑몰의 각 상품에 대한 정보가 잘 바뀌지 않는 데이터라면, 각 상품에 대한 페이지를 미리 pre-render 하여 페이지를 만들어둔다면 클라이언트가 상품 페이지를 요청할 때 항상 같은 파일을 내려주기만 하면 된다. 

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

Flux 아키텍처를 기반으로 하는 단방향 데이터 흐름을 가지고 있기 떄문에, 상태가 예측 가능하다 .

이는 `변경은 항상 순수함수로만 가능하다. (store - action - reducer) ` 라는 원칙이 있기 때문이다. 또한 순수함수의 이용은 테스트를 하기 쉽게 한다.  또한 복잡한 상태 관리와 비교했을 때 유지 보수가 쉽고, action, state logging 을 통해 디버깅이 쉽다. 

- > [redux vs context api](https://react.vlpt.us/redux/)

  외부 라이브러리 사용을 원하지 않을 땐 Context API !!!

  redux 의 장점은 간단히 말하면, 여러 미들웨어를 사용할 수 있고, redux toolkit 을 이용한 코드 간소화가 가능하다. 

  1. 미들웨어

     액션 객체가 리듀서에서 처리되기 전에 원하는 작업들을 수행할 수 있다.  예를 들어, 

     - 특정 조건에 따라 액션을 무시 
     - 액션을 콘솔에 출력하거나, 서버 쪽에서 로깅 
     - 등 ..

     주로 비동기 작업을 처리할 때 많이 사용된다. 

  2. 유용한 함수와 Hooks 

     Context API 에서 useReducer 를 사용할 때, Context 도 새로 만들고 Provider 설정도 하고, 편하게 사용하기 위해 전용 커스텀 Hook 을 따로 만들어 사용하는데, 리덕스에선 이를 편하게 해줄 수 있는 기능들이 있다. `connect`, `useSelector`, `useDispatch` ... 

     connect 함수와 useSelector 함수는 내부적으로 최적화가 잘 되어 있지만, Context API 는 최적화가 자동으로 이루어져있지 않아 Context 가 지니고 있는 상태가 바뀌면 Context 내부의 Provider 내부 컴포넌트들이 모두 리렌더링 된다.

  3. Context 에서 기능별로 Context 를 생성하는 것이 일반적인다. 리덕스에선 모든 글로벌 상태를 하나의 커다란 객체에 넣어 사용하여 매번 Context 를 새로 만드는 수고를 덜 수 있다.  

  

>Context API 를 사용해본 적 있나요?

>Webpack 과 Babel 에 대해 설명해주세요 

Webpack 은 모듈 번들러로, 웹 어플리케이션에 필요한 자원 (HTML, CSS, JS, 이미지 파일 등)의 연관 관계를 파악하여 dependecy graph 를 그리고, 이를 하나의 파일로 병합하고 압축하는 역할을 한다. 

장점은 웹 개발 자동화 도구로서, 개발 시엔 코드 수정 후 새로고침 했을 떄 바로 결과를 볼 수 있다. 또한 배포 시엔 모듈 번들링을 통해 자원을 하나로 압축하므로 적은 HTTP 요청으로도 자원을 불러올 수 있고 이는 웹 어플리케이션의 빠른 로딩속도와 성능을 제공한다. 

Babel 은 Javascript 에서 지원하는 최신 문법들을 최대한 많은 브라우저 환경에서 호환 가능하도록 transfile 해주는 언어이며, 작성한 코드를 여러 브라우저에서 범용적으로 사용할 수 있도록 해준다. 

>JavaScript 의 이벤트 루프에 대해 설명해주세요

- >https://developer.mozilla.org/ko/docs/Web/JavaScript/EventLoop

  JavaScript의 런타임 모델은 코드의 실행, 이벤트의 수집과 처리, 큐에 대기 중인 하위 작업을 처리하는 **이벤트 루프**에 기반하고 있으며.. 

- >https://meetup.toast.com/posts/89

  자바스크립트가 '단일 스레드' 기반의 언어라는 말은 '자바스크립트 엔진이 단일 호출 스택을 사용한다'는 관점에서만 사실이다. 실제 자바스크립트가 구동되는 환경(브라우저, Node.js등)에서는 주로 여러 개의 스레드가 사용되며, 이러한 구동 환경이 단일 호출 스택을 사용하는 자바 스크립트 엔진과 상호 연동하기 위해 사용하는 장치가 바로 '이벤트 루프'인 것이다.

  이벤트 루프는 호출 스택이 비워질 때마다 큐에서 콜백 함수를 꺼내와서 실행하는 역할을 해 준다.

  이벤트 루프는 '**현재 실행중인 태스크가 없는지**'와 '**태스크 큐에 태스크가 있는지**'를 반복적으로 확인

>이벤트 루프를 통한 비동기 처리 단계에 대해 설명해주세요 

- >[JavaScript 비동기 핵심 Event Loop 정리](https://medium.com/sjk5766/javascript-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%95%B5%EC%8B%AC-event-loop-%EC%A0%95%EB%A6%AC-422eb29231a8)

  setTimeout 과 같은 비동기 처리가 필요한 함수는, 

  1. 함수가 호출되면 call stack 에 추가되고
  2. 함수가 실행되면서 browser 가 제공하는 timer Web API 를 호출하고 call stack 에서 제거된다.
  3. setTImeout 에 설정한 시간이 흐르면, call back 으로 전달한 함수가 callback queue (event queue) 에 추가된다. 
  4. event loop 은 call stack 이 비어있는 것을 확인하면, callback queue 에 존재하는 콜백 함술르 call stack 에 추가한다. 
  5. 함수가 실행되고, 제거된다!

  

>렉시컬 환경에 대해 설명해주세요

변수가 선언될 당시의 환경

- >https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures

  lexical ? 변수가 어디에서 사용 가능한지 알기 위해 그 변수가 소스코드 내 어디에서 선언되었는지 고려한다는 것을 의미

- >https://meetup.toast.com/posts/129

  자바스크립트 코드에서 변수나 함수 등의 식별자를 정의하는데 사용하는 객체

- >https://ko.javascript.info/closure

  자바스크립트에선 실행 중인 함수, 코드 블록 `{...}`, 스크립트 전체는 *렉시컬 환경(Lexical Environment)* 이라 불리는 내부 숨김 연관 객체(internal hidden associated object)를 갖습니다.

  렉시컬 환경 객체는 두 부분으로 구성됩니다.

  1. *환경 레코드(Environment Record)* – 모든 지역 변수를 프로퍼티로 저장하고 있는 객체입니다. `this` 값과 같은 기타 정보도 여기에 저장됩니다.
  2. *외부 렉시컬 환경(Outer Lexical Environment)* 에 대한 참조 – 외부 코드와 연관됨

  

  **코드에서 변수에 접근할 땐, 먼저 내부 렉시컬 환경을 검색 범위로 잡습니다. 내부 렉시컬 환경에서 원하는 변수를 찾지 못하면 검색 범위를 내부 렉시컬 환경이 참조하는 외부 렉시컬 환경으로 확장합니다. 이 과정은 검색 범위가 전역 렉시컬 환경으로 확장될 때까지 반복됩니다.**

>렉시컬 환경과 관련하여, 클로저라는 개념이 있는데, 설명해주세요

함수와 렉시컬 환경의 조합으로 알고 있으며, 어떤 함수의 실행이 종료된 이후에도, 그 함수 내부의 상태를 기억하고 사용할 수 있는 것을 뜻한다. 또한 상태를 보호하는 목적으로도 사용할 수 있다. 

- >https://ko.javascript.info/closure

  외부 변수를 기억하고 이 외부 변수에 접근할 수 있는 함수를 의미

  모든 함수는 함수가 생성된 곳의 렉시컬 환경을 기억한다는 점입니다. 함수는 `[[Environment]]`라 불리는 숨김 프로퍼티를 갖는데, 여기에 함수가 만들어진 곳의 렉시컬 환경에 대한 참조가 저장됩니다.

  몇몇 언어에선 클로저를 구현하는 게 불가능하거나 특수한 방식으로 함수를 작성해야 클로저를 만들 수 있습니다. 하지만 자바스크립트에선 모든 함수가 자연스럽게 클로저가 됩니다.



>javascript garbage collector 에 대해 설명해주세요. 

- >https://developer.mozilla.org/ko/docs/Web/JavaScript/Memory_Management

  **메모리 생존 주기**

  C 언어같은 저수준 언어에서는 메모리 관리를 위해 [malloc()](https://pubs.opengroup.org/onlinepubs/009695399/functions/malloc.html) 과 [free()](https://en.wikipedia.org/wiki/C_dynamic_memory_allocation#Overview_of_functions)를 사용합니다. 반면, 자바스크립트는 객체가 생성되었을 때 자동으로 메모리를 할당하고 더 이상 필요하지 않을 때 자동으로 해제합니다.

  메모리 생존주기는 프로그래밍 언어와 관계없이 비슷합니다.

  1. 필요할 때 할당합니다.
  2. 할당된 메모리를 사용합니다. (읽기, 쓰기)
  3. 더 이상 필요하지 않으면 해제합니다.

  두 번째 부분은 모든 언어에서 명시적으로 사용됩니다. 그러나 첫 번째 부분과 마지막 부분은 저수준 언어에서는 명시적이며, 자바스크립트와 같은 대부분의 고수준 언어에서는 암묵적으로 작동합니다.

  그러나 3번에서 더 이상 필요하지 않은 모든 메모리를 판단하는 것은 비결정적인 문제이다. 

  **가비지 컬렉션**

  가비지 콜렉션의 핵심 개념은 참조! A라는 메모리를 통해 (명시적이든 암시적이든) B라는 메모리에 접근할 수 있다면 "B는 A에 참조된다" 라고 합니다. 예를 들어 모든 자바스크립트 오브젝트는 [prototype](https://developer.mozilla.org/en-US/JavaScript/Guide/Inheritance_and_the_prototype_chain) 을 암시적으로 참조하고 그 오브젝트의 속성을 명시적으로 참조합니다.

  1. Reference Counting Garbage Collection: 어떤 다른 오브젝트도 참조하지 않는 오브젝트 == Garbage! 

     순환 참조에서 문제가 발생 

  2. Mark and Sweep Algorithm: 2012 년 기준 최신 브라우저들은 이 알고리즘을 사용

     reachability 라는 개념을 사용한며, root object 로부터 닿을 수 없는 오브젝트를 수집한다. 

     루트 (root) 는 아래 값들을 뜻한다. 

     - 현재 함수의 지역 변수와 매개변수
     - 중첩 함수의 체인에 있는 함수에서 사용되는 변수와 매개변수
     - 전역 변수
     - 기타 등등

- >https://velog.io/@bumsu0211/JavaScript-Garbage-Collection

  V8 의 메모리 엔진 구조 => new space & old space / pointer 와 data 구분 / minor GC & major GC

> React 에서도 클로저 개념을 사용하는데, 어떤 부분에서 사용되는지 혹시 아시나요?

함수 컴포넌트에서 useState 를 이용하여 상태를 관리하게 되는데, 함수 컴포넌트의 특성 상 렌더링 시 매번 새로 실행되는 것과 다름 없음에도 불구하고 useState 로 선언한 상태가 그대로 유지된다. 

>Todo List 라이브 코딩 진행..
>
>왜 `todoList` 상태에 왜 배열을 사용했나요?

----

>모두싸인에 지원하신 동기에 대해 말씀해주세요. 

>블로그에 깔끔히 잘 정리를 하신 것 같은데, 본인의 성장을 위해 팀에게 원하는 것이 있나요?

>좋은 개발자, 성숙한 개발자란 뭐라고 생각하시나요

>앞으로 어떤 커리어를 밟아나가고 싶은가요?

