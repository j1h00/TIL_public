# CS study : 01 Development Common Sense 

>[Interview_Question_for_Beginner](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)/**Development_common_sense**/

- 위 repository 를 읽고 정리한 글입니다. 

## 객체 지향 프로그래밍 

### OOP?

>[# 객체 지향에 대한 이해 / 객체 지향적 설계](https://asfirstalways.tistory.com/177)
>
>객체 지향의 가장 기본은 객체이며, 객체의 핵심은 기능을 제공하는 것이다. 실제로 객체를 정의할 때 사용하는 것은 객체가 제공해야 할 기능이며, 객체가 내부적으로 어떤 데이터를 갖고 있는 지로는 정의되지 않는다. 이러한 기능들을 **오퍼레이션(operation)** 이라고 부른다. 즉, 객체는 오퍼레이션으로 정의가 된다. 

- 시그니처(signature), 인터페이스(Interface), 메시지, 책임, 의존성, 캡슐화 등의 개념.. 

>객체 지향 프로그래밍 이전의 프로그래밍 패러다임을 살펴보면, 중심이 컴퓨터에 있었다. 컴퓨터가 사고하는대로 프로그래밍을 하는 것이다. 하지만 객체지향 프로그래밍이란 **인간 중심적 프로그래밍 패러다임**이라고 할 수 있다. 즉, **현실 세계를 프로그래밍으로 옮겨와 프로그래밍하는 것**을 말한다. 현실 세계의 사물들을 객체라고 보고 그 객체로부터 개발하고자 하는 애플리케이션에 필요한 특징들을 뽑아와 프로그래밍 하는 것이다. 이것을 **추상화**라한다.

1. 이미 작성한 코드에 대한 **재사용성**이 높다

   자주 사용되는 로직을 라이브러리로 만들어두면 계속해서 사용할 수 있으며 그 신뢰성을 확보 할 수 있다.

2. 라이브러리를 각종 예외상황에 맞게 잘 만들어두면 개발자가 사소한 실수를 하더라도 그 에러를 컴파일 단계에서 잡아낼 수 있으므로 **버그 발생이 줄어든다.**

3. 내부적으로 어떻게 동작하는지 몰라도 개발자는 라이브러리가 제공하는 기능들을 사용할 수 있기 때문에 **생산성**이 높아지게 된다

4. 객체 단위로 코드가 나눠져 작성되기 때문에 디버깅이 쉽고 **유지보수**에 용이하다.

5. **데이터 모델링**을 할 때 객체와 매핑하는 것이 **수월**하기 때문에 요구사항을 보다 명확하게 파악하여 프로그래밍 할 수 있다.

> but.. 
>
> 객체 지향 프로그래밍의 치명적인 단점은 함수형 프로그래밍 패러다임의 등장 배경을 통해서 알 수 있다. 바로 객체가 **상태**를 갖는다는 것이다. 변수가 존재하고 이 변수를 통해 **객체가 예측할 수 없는 상태를 갖게 되어** 애플리케이션 내부에서 버그를 발생시킨다는 것이다. 이러한 이유로 함수형 패러다임이 주목받고 있다.

### 객체 지향적 설계 원칙

1. **SRP(Single Responsibility Principle) : 단일 책임 원칙**
   클래스는 단 하나의 책임을 가져야 하며 클래스를 변경하는 이유는 단 하나의 이유이어야 한다.
2. **OCP(Open-Closed Principle) : 개방-폐쇄 원칙**
   확장에는 열려 있어야 하고 변경에는 닫혀 있어야 한다.
3. **LSP(Liskov Substitution Principle) : 리스코프 치환 원칙**
   상위 타입의 객체를 하위 타입의 객체로 치환해도 상위 타입을 사용하는 프로그램은 정상적으로 동작해야 한다.
4. **ISP(Interface Segregation Principle) : 인터페이스 분리 원칙**
   인터페이스는 그 인터페이스를 사용하는 클라이언트를 기준으로 분리해야 한다.
5. **DIP(Dependency Inversion Principle) : 의존 역전 원칙**
   고수준 모듈은 저수준 모듈의 구현에 의존해서는 안된다.



## RESTful API 

>from wiki
>
>월드 와이드 웹(World Wide Web a.k.a WWW)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식으로 자원을 정의하고 자원에 대한 주소를 지정하는 방법 전반에 대한 패턴 

#### REST (REpresentational State Transfer )

REST 는 말하자면 Resource Oriented Architecture 로, API 설계의 중심에 자원(Resource)이 있고, HTTP Method 를 통해 자원을 처리하도록 설계하는 것.

#### 6가지 특징

>[REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92)

1. Uniform (유니폼 인터페이스)

   Uniform Interface는 URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일을 말합니다.

2. Stateless (무상태성)

   REST는 무상태성 성격을 갖습니다. 다시 말해 작업을 위한 상태정보를 따로 저장하고 관리하지 않습니다. 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 됩니다. 때문에 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않음으로써 구현이 단순해집니다.

3. Cacheable (캐시 가능)

   REST의 가장 큰 특징 중 하나는 HTTP라는 기존 웹표준을 그대로 사용하기 때문에, 웹에서 사용하는 기존 인프라를 그대로 활용이 가능합니다. 따라서 HTTP가 가진 캐싱 기능이 적용 가능합니다. HTTP 프로토콜 표준에서 사용하는 Last-Modified태그나 E-Tag를 이용하면 캐싱 구현이 가능합니다.

4. Self-descriptiveness (자체 표현 구조)

   REST의 또 다른 큰 특징 중 하나는 REST API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조로 되어 있다는 것입니다.

5. Client - Server 구조

   REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야 할 내용이 명확해지고 서로간 의존성이 줄어들게 됩니다.

6. 계층형 구조

   REST 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있고 PROXY, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있게 합니다.

### REST API 디자인 가이드

리소스와 행위를 명시적이고 직관적으로 분리한다. 

**1. ** **URI**는 정보의 자원을 표현해야 한다.

주의할 점

- 리소스 명은 동사보다 명사를 사용한다. 
- 슬래시 구분자는 계층 관계를 나타내는 데 사용하고, 마지막 문자로 슬래시(/)를 포함하지 않는다. 
- 하이픈(-) 은 URI 가독성을 높이는데 사용하고, 밑줄(_)은 URI 에 사용하지 않는다. 
- 파일 확장자는 URI 에 포함시키지 않는다. 

**2. ** 자원에 대한 행위는 **HTTP Method(GET, POST, PUT, DELETE)**로 표현한다.

조회, 생성, 수정, 삭제 



## TDD (Test-Driven Development)

> 매우 짧은 개발 사이클의 반복에 의존하는 소프트웨어 개발 프로세스
>
> 1. 우선 개발자는 요구되는 새로운 기능에 대한 자동화된 테스트케이스를 작성하고 해당 테스트를 통과하는 가장 간단한 코드를 작성한다. 
>
> 2. 일단 테스트 통과하는 코드를 작성하고 상황에 맞게 리팩토링하는 과정을 거친다. 

- 즉, 테스트가 코드 작성보다 우선한다. 

1. 어떤 새로운 기능을 추가하면 잘 작동하던 기능이 제대로 작동하지 않는 경우가 발생할 수 있고, 개발자가 이를 미처 인지하지 못하는 경우 위험하다. 따라서 이를 방지하기 위해 테스트 코드를 작성하여 새로운 기능과 기존 기능들이 제대로 작동하는지 확인한다. 

2. 특히, 좋은 코드를 작성하기 위해선, 가독성, 네이밍 규칙의 일관성, 확장성, 비즈니스 로직, 예외 처리 등이 중요하지만, 코드를 작성하는 과정에서 이 모든 과정을 신경 쓰는 것은 어렵다. 때문에, 코드량이 방대해지면 리펙토링이 필요한데, 테스트 주도 개발 시 테스트 코드가 그 중심을 잡아준다. 

   즉, 리펙토링 전과 후 동일한 결과를 보장할 수 있다. 
   
   리펙토링 과정에서 기능이 오작동을 일으킬 수 있지만, 간단히 테스트를 통해 체크 가능하다. 결과적으로 리펙토링 속도도 빨라지고 코드 퀄리티도 높아진다!

그러나, 

1. 코드량이 분명 늘어나므로, 빠른 생산성이 요구되는 시점에는 어려울 수 있고, 진입 장벽이 존재한다. 
2. 또한 다양한 사용자와 생각지도 못한 예외 케이스를 고려하면서 실제 코드보다 테스트 코드의 구현에 더 많은 시간을 쏟는다면 문제가 될 수 있다. 

#### 좋은 테스트

1. Fast: 테스트는 빠르게 동작하여 자주 돌릴 수 있어야 한다.
2. Independent: 각각의 테스트는 독립적이며 서로 의존해서는 안된다.
3. Repeatable: 어느 환경에서도 반복 가능해야 한다.
4. Self-Validating: 테스트는 성공 또는 실패로 bool 값으로 결과를 내어 자체적으로 검증되어야 한다.
5. Timely: 테스트는 적시에 즉, 테스트하려는 실제 코드를 구현하기 직전에 구현해야 한다.

#### Spring 에서의 TDD


1. Repository -> Service -> Controller 순서로 개발을 진행한다.
2. Repository 계층의 테스트는 H2와 같은 인메모리 데이터베이스 기반의 통합 테스트로 진행한다.
3. Service 계층의 테스트는 Mockito를 사용해 Repository 계층을 Mock하여 진행한다.
4. Controller 계층의 테스트는 SpringTest의 MockMvc를 사용해 진행한다.

#### 프론트엔드 BDD ?

BDD는 Behavior Driven Development로 테스트를 시나리오 기반으로 작성하는 것을 말합니다.

`Describe` - `Context` - `It` 세 키워드를 이용해서 행동기반 테스트를 작성하게 됩니다.

- Describe: 설명할 테스트 대상을 명시

- Context: 테스트 대상이 놓인 상황을 설명

- It:  테스트 대상의 행동을 설명

프론트엔드에서 Unit test를 할 때 사용할 수 있는 라이브러리는 jest, mocha, jasmin 이 있다. 



## 함수형 프로그래밍 

> 함수형 프로그래밍은 **순수 함수(pure function)**를 조합하고 **공유 상태(shared state), 변경 가능한 데이터(mutable data)** 및 **부작용(side-effects)**을 피하여 프로그래밍하는 패러다임이다.

1. 순수 함수 (pure function)

   - 동일한 입력에는 항상 같은 값을 반환해야 하는 함수
   - 함수의 실행이 프로그램의 실행에 영향을 미치지 않아야 하는 함수
   - 함수 내부에서 인자의 값을 변경하거나 프로그램 상태를 변경하는 부수효과(Side Effect) 가 없는 것
     - 이는 오로지 출력만 수행한다는 의미이다. 
   - 순수 함수는 프로그램의 변화 없이 입력 값에 대한 결과를 예상할 수 있어 테스트가 용이하다.

   ```js
   let num = 1;
   
   // bad
   function add(a) {
       return a + num;
   }
   
   // good
   function add(a, b) 
       return a + b;
   }
   ```

2. 비상태, 불변성 (Stateless, Immutability)

   ![img](https://velog.velcdn.com/images/teo/post/8d7aa474-698a-4cf7-aabd-6424932043c1/image.png)

   - 함수형 프로그래밍에서의 데이터는 변하지 않는 불변성을 유지해야 한다.

   - 데이터의 변경이 필요한 경우, 원본 데이터 구조를 변경하지 않고 그 데이터의 복사본을 만들어서 그 일부를 변경하고, 변경한 복사본을 사용해 작업을 진행한다.

     - `pass by reference ` vs `pass by value` 

     - `shallow copy` vs `deep copy`

       - 방어적 복사 `structuredClone()`

       

3. 선언형 (Declarations)
   - 명령형 프로그래밍은 **어떻게** 할 것인가에 주목한다면, 선언형 프로그래밍은 **무엇을** 할 것인가에 주목한다. 
   - 어떻게 보다는 무엇을 해야할 지 기술한다 => 고차원의 추상화 

   
   
4. 일급 객체와 고차함수 (First-class, Higher-order functions)

   - 함수형 프로그래밍에서는 함수가 일급 객체가 된다.
     - 변수나 데이터 구조안에 담을 수 있다.
     - 파라미터로 전달 할 수 있다.
     - 반환값(return value)으로 사용할 수 있다.
     - 할당에 사용된 이름과 관계없이 고유한 구별이 가능하다.
     - 동적으로 프로퍼티 할당이 가능하다.

   ```js
   // 1급 객체
   const addTwo = (num) => num + 2;
   const multiplyTwo = (num) => num * 2;
   const transform = (numbers) => numbers.map(addTwo).map(multiplyTwo);
   ```

   - 고차 함수 
     - 함수를 인자로써 전달할 수 있고, 반환값으로 또 다른 함수를 사용할 수 있는 함수 
     - 즉, 함수 자체가 일급 객체이면 고차함수를 만드는 게 가능해진다. 

함수형 프로그래밍에서는 순수함수의 조합을 통해, 연쇄적으로 혹은 병렬로 호출하여 더 큰 함수를 만드는 과정으로 전체 프로그램을 구축한다. 이 과정에서 여러 함수를 엮어야 하기 때문에 고차함수를 사용한다. 



### Why?

>Side effect 에 기반한 객체지향 프로그래밍에서는 멀티쓰레딩에 효과적으로 대응하기 쉽지 않지만 불변 값을 주로 다루는 함수형 프로그래밍은 본질적으로 동시성 처리가 쉬워진다.
>
>단위 테스트가 쉽다. 
>
>이 외에도 Side-effect 에 의존한 코드에 비해 유지 보수가 용이하다는 점, 코드를 이해하기 수월하다는 점이 있을 것 같다.



### Reactive Programming 

>**반응형 프로그래밍(Reactive Programming)**은 **선언형 프로그래밍(declarative programming)**이라고도 불리며, **명령형 프로그래밍(imperative programming)**의 반대말이다. 또 함수형 프로그래밍 패러다임을 활용하는 것을 말한다. 반응형 프로그래밍은 기본적으로 모든 것을 스트림(stream)으로 본다. 스트림이란 값들의 집합으로 볼 수 있으며 제공되는 함수형 메소드를 통해 데이터를 immutable 하게 관리할 수 있다.

>리액티브 프로그래밍(Reactive Programming) 은 비동기 데이터 흐름(data flow) 에 기반을 둔 프로그래밍 패러다임이다. 데이터 흐름은 마치 강과 같아서 이를 관찰하거나 필터링하거나 다룰 수 있으며 새로운 사용자를 위한 새로운 흐름을 만들기 위해 다른 흐름과 병합할 수도 있다. 

>Reactive Programing은 기본적으로 모든 것을 스트림(stream)으로 본다. 이벤트, ajax call, 등 모든 데이터의 흐름을 시간순서에 의해 전달되어지는 스트림으로 처리한다. 즉, 스트림이란, 시간순서에 의해 전달되어진 값들의 collection 정도로 이해해 보자.

- Rx(ReactiveX)

  - RxJS, RxJava

  

### 심화 

>https://velog.io/@teo/functional-programming

>**함수형 프로그래밍에서는 부수효과와 가변된 상태를 멀리하고 순수함수로 프로그래밍을 하자**고 하지만 대부분의 프로그램의 목적은 부수효과에 있습니다. 서버에서 데이터를 조회하고 화면을 변경하고 로그를 남기고 파일을 읽고 쓰는 행위들을 하지 않는 프로그램은 의미가 없겠죠. 순수함수만 가지고는 우리가 만들고자 하는 응용프로그램이 되지 않습니다.
>
>그렇기에 잘못된 오해를 불러 일으키는 용어 대신 **함수형 프로그래밍은 프로그램은 크게 `액션`, `계산`, `데이터` 이 3가지로 나눠 구분하여 프로그래밍을 하는 것이라고 다시 정의를 해봅시다.** 그렇다면 조금 더 함수형 프로그래밍이 하고자 하는 방향성에 대해서 명쾌하게 이해를 할 수 있을 거라고 생각합니다.

=> 비교 

```html
<button id="button">0</button>

<script>
document.getElementById("button").onclick = function() {
	button.innerText++
}
</script>
```

vs

```js
// 함수형 프로그래밍 관점에서 분리해보자.
function App() {
  // 데이터
  const [count, setCount] = useState(0)
  // 계산 
  const increase = (value) => value + 1
  // 액션
  const onClick = () => setCount(increase(count))
  // 선언적 패턴
  return <button onClick={onClick}>{count}</button>
}
```

- 액션에서 계산을 분리했다는 점이 중요하다. 함수형 프로그래밍은 액션을 최소화하고 계산 함수를 많이 만들어 관리하는 것을 목표로 한다. 독립적인 계산함수는 언제든 재사용 가능하고, 테스트하기에도 용이하며 조립을 해도 언제나 같은 결과를 만들어낸다. 
- 즉, 계산은 순수함수이다 

vs

```js
// 잘못 분리된 계산함수
const increase = () => {
  ...
  setState(count + 5)
}

const onClick = () => {
  ...
  increase()
}
```



액션과 계산을 분리하면 ...

액션은 무엇을 하는 것인지 행동을 기반한 기획서에 가까운 코드가 만들어지며, 데이터 구조를 몰라도 되는 형태의 코드가 된다. (무엇을)

계산과 데이터에 가까워질수록 데이터 중심적인 코드를 작성하게 되고, 재사용성이 높고 테스트하기 좋은 테스트를 갖춘다. (어떻게)

이렇게 액션과 계산의 계층이 나뉘어지게 되면, 각 계층을 침범하지 않도록 코드가 작성되어 `추상화 벽` 이 만들어진다. 상위 액션 계층과 하위 계산 계층이 서로의 코드 변화에 영향을 받지 않는다. 

따라서 선언적 패턴을 통해 무엇과 어떻게를 구분하여 좋은 설계를 유지할 수 있다. 



> 함수형 프로그래밍을 외부환경에 영향을 주지 않는 계산 함수를 만들게 되면 언제든 재사용이 가능한 함수를 만들게 됩니다. 이러한 함수들을 만들다보면 반복적으로 만들어지는 코드 패턴들에 대응하는 유틸리티 함수들이 많이 만들어지게 됩니다.
>
> => 계층구조에서 한 계층이 전부 라이브러리화 된다.
>
> 그리하여 나온 것들은 함수형 프로그래밍 개념을 이용해서 만들어진 상태관리를 위한 Redux라던가 반응형 프로그래밍에 함수형 프로그래밍 개념을 엮어서 만든 rxjs, 불변성 관리를 위해서 만들어진 immutable.js, 날짜만 다루는 함수형 라이브러리 date-fns 등 특정 목적성을 가지고 여러가지 **라이브러리들이 함수형 패러다임을 적절히 결합하는 방식으로 발전**을 하고 있습니다.



### 관련 면접 질문!

#### 명령형? 선언형? 절차지향? 객체지향?

- 명령형 프로그래밍: 프로그래밍의 상태와 상태를 변경시키는 구문의 관점에서 연산을 설명하는 방식
  - 절차지향 프로그래밍: 수행되어야 할 연속적인 계산 과정을 포함하는 방식 (C, C++)
  - 객체지향 프로그래밍: 객체들의 집합으로 프로그램의 상호작용을 표현 (C++, Java, C#)
- 선언형 프로그래밍: 어떤 방법으로 해야 하는지(How)를 나타내기보다 무엇(What)과 같은지를 설명하는 방식 (SQL)
  - 함수형 프로그래밍: 순수 함수를 조합하고 소프트웨어를 만드는 방식 (클로저, 하스켈, 리스프)

절차형과 함수형 프로그래밍이 서로 비슷하다고 생각될 수 있는데, 함수형 프로그래밍에서는 상태를 변화시키지 않아 부수 효과를 일으키지 않는다. 

----

#### 고차 함수에 대해서 아나요?

고차 함수(Higher-Order Function, HOF)는 함수를 인수로 전달받거나 함수를 반환하는 함수를 말한다.

자바스크립트의 함수는 일급 객체이므로 함수를 값처럼 인수로 전달할 수 있으며 반환할 수도 있다.

고차 함수는 외부 상태의 변경이나 가변(mutable) 데이터를 피하고 불변성(immutability)을 지향하는 함수형 프로그래밍에 기반을 두고 있다.

함수형 프로그래밍은 순수 함수와 보조 함수의 조합을 통해 로직 내에 존재하는 조건문과 반복문을 제거하여 복잡성을 해결하고 변수의 사용을 억제하여 상태 변경을 피하려는 프로그래밍 패러다임이다.

함수형 프로그래밍은 순수 함수를 통해 부수 효과를 최대한 억제하여 오류를 피하고 프로그램의 안정성을 높이려는 노력의 일환이라고 할 수 있다.

```js
대부분의 고차 함수들은 파라미터로 콜백 함수를 받아 사용되기 때문에 원본 배열을 바탕으로 하는 새로운 결과값을 창조하는데 사용된다
Array.prototype.sort (원본 배열을 변경한다 - 부수효과 o)
Array.prototype.forEach
Array.prototype.map
Array.prototype.filter
Array.prototype.reduce
Array.prototype.some
Array.prototype.every
Array.prototype.find
```

----

#### 자바스크립트에서 함수가 일급 객체라면, 일급 객체로 뭘 할 수 있나요?

일급 객체로서 함수가 가지는 가장 큰 특징은 일반 객체와 같이 함수의 매개변수에 전달할 수 있으며, 함수의 반환값으로 사용할 수도 있다는 것이다. 이는 함수형 프로그래밍을 가능케 하는 자바스크립트의 장점 중 하나이다.

----


#### 꼬리 질문) 함수형 프로그래밍이 뭔가요?

외부 상태를 변경하지 않고 외부 상태에 의존하지도 않는 함수를 **순수 함수** 라 한다. **순수 함수를 통해 부수효과를 최대한 억제하여 오류를 피하고 프로그램의 안전성을 높이려는 프로그래밍 패러다임** 을 **함수형 프로그래밍** 이라 한다.

----


#### 꼬리 질문) 순수 함수가 뭔가요? 일반 함수와는 어떤 차이가 있죠?

1. 순수 함수: 어떤 외부 상태에 의존하지도 않고 변경하지도 않는, 즉 부수 효과가 없는 함수를 순수 함수라 한다.
2. 비순수 함수: 외부 상태에 의존하거나 외부 상태를 변경하는, 즉 부수 효과가 있는 함수를 비순수 함수라고 한다.

----

#### 자바스크립트는 객체지향 프로그래밍 언어인가요?

자바스크립트는 객체지향 프로그래밍 뿐만 아니라 명령형, 함수형 프로그래밍을 지원하는 멀티 패러다임 프로그래밍 언어입니다.

**클래스** 기반 객체지향 프로그래밍 언어와 달리 **프로토타입** 기반의 객체지향 프로그래밍입니다.

>javascript를 창시한 Brendan Erich는 언어를 개발할 당시 유행하던 객체지향에 한계를 느끼고 LISP, scheme등 함수형 프로그래밍에 관심을 가지고 있었기에 **함수형 프로그래밍의 형태로 언어를 만들고 싶어 했습니다.** 하지만 Netscape의 그의 상사는 당시 개발자들이 제일 많이 쓰던 **Java와 같은 문법**으로 만들기를 요구했기에 결국 둘의 혼종의 형태로 세상에 나오게 되었습니다. :)



----

#### 자바스크립트에서 상태의 불변성을 지키기 위한 방법에는 무엇이 있나요?



#### 리액트에서 상태의 불변성을 중요하게 여기는데, 왜 그런가요?





## etc 

#### 리액트에서 함수형 컴포넌트라고 부르지 않고 함수 컴포넌트라고 부르는 이유가 무엇인가요

(답변 출처 - 테오의 프론트엔드 인성님)

원래 리액트 측에서는 **함수형 컴포넌트** 라는 단어를 사용했습니다. 하지만 이러한 네이밍이 **함수형 프로그래밍** 과 비슷했고, 충분히 혼란을 야기할 수 있었습니다. 처음 리액트의 함수형 컴포넌트를 배우는 입장에서는 `'함수형 컴포넌트를 사용하면 함수형 프로그래밍이 가능해진다'`와 같은 혼란을 느낄 수 있었기 때문입니다.

그러나 우리가 리액트에서 사용하는 **함수 컴포넌트** 는 훅(hook)이 들어가고, 이 훅으로 **사이드 이펙트** 를 빈번히 일으키기 때문에 함수형 프로그래밍이라고 볼 수 없습니다. 함수형 프로그래밍은 순수 함수를 지향하는데, 사이드 이펙트를 빈번히 일으키는 리액트의 **함수 컴포넌트**가 **함수형 컴포넌트**로 보기는 어렵다는 것입니다.

2018년 이후 리액트 측에서도 **함수형 컴포넌트** 가 아닌 **함수 컴포넌트** 로 이름을 다시 정했습니다.



