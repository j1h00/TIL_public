# TIL : Element Rendering

### *Element ?*

- Element 엘리먼트는 React 앱의 가장 작은 단위입니다. 
- 엘리먼트는 화면에 표시할 내용을 기술한다. 

```react
const element = <h1>Hello, world</h1>;
```

- vs 브라우저 DOM 엘리먼트 
  - React 엘리먼트는 일반 객체이며 (plain object), 쉽게 생성할 수 있다. 
  - React DOM 은 React 엘리먼트와 일치하도록 DOM 을 업데이트한다. 
- vs 컴포넌트
  - 엘리먼트는 컴포넌트의 "구성 요소" 이다. (자세한 설명은 다음 장에!)

### DOM 에 (into) 엘리먼트 렌더링하기 

HTML 파일 어딘가에 `<div>` 가 있다고 가정해보자!

```react
<div id="root"></div>
```

이 안에 들어가는 모든 엘리먼트를 React DOM 에서 관리한다고 한다면, 우리는 이를 "root" DOM 노드라고 부를 수 있다. 

React 로 구현된 어플리케이션은 보통 하나의 root DOM node 를 가진다.

React 엘리먼트를 root DOM 노트에 렌더링 하려면, `ReactDOM.render()` 를 통해 전달하면 된다 .

```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

### 렌더링 된 엘리먼트 업데이트하기 

React 엘리먼트는 **불변객체** (Immutable Object) 이다. 엘리먼트 생성 이후에는, 해당 엘리먼트의 자식이나 속성을 변경할 수 없다. 엘리먼트는 영화에서 하나의 프레임과 같이 특정 시점의 UI 를 보여준다. 

지금까지 설명한 내용으로는, UI 를 업데이트하는 유일한 방법은, 새로운 엘리먼트를 생성하고 `ReactDOM.render()` 로 전달하는 것이다. 

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));}

setInterval(tick, 1000);
```

- `serInterval()` 콜백을 이용해 초마다 `ReactDom.render()` 를 호출!

- 그러나 대부분의 React 앱은 `ReactDom.render()` 를 한번만 호출!

### 변경된 부분만 업데이트하기 

React DOM 은 해당 엘리먼트와 자식 엘리먼트를 이전의 엘리먼트와 비교하고, 필요한 경우에만 DOM 을 업데이트한다. 

위의 시계 예시에서도, 실제로 변경되는 React DOM 은 텍스트로 변경된 Date 부분만이다. 

