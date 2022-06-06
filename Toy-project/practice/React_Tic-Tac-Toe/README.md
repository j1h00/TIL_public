# TIL : React 로 만드는 Tic Tac Toe

## 1. INTRO 

## ***React ?***

https://ko.reactjs.org/

>#### A JavaScript library for building user interfaces
>
>##### Declarative
>
>React makes it painless to create interactive UIs. Design simple views for each state in your application, and React will efficiently update and render just the right components when your data changes.
>
>Declarative views make your code more predictable and easier to debug.
>
>****
>
>##### Component-Based
>
>Build encapsulated components that manage their own state, then compose them to make complex UIs.
>
>Since component logic is written in JavaScript instead of templates, you can easily pass rich data through your app and keep state out of the DOM.
>
>****
>
>##### Learn Once, Write Anywhere
>
>We don’t make assumptions about the rest of your technology stack, so you can develop new features in React without rewriting existing code.
>
>React can also render on the server using Node and power mobile apps using [React Native](https://reactnative.dev/).

- vs ***Vue*** : 
  - Vue 는 프레임워크, React 는 라이브러리 !
    - 라이브러리는 사용자가 필요할 때에 가져다 썻다가 뺏다가 할 수 있고, 부분적으로 사용이 가능하다. 
    - 프레임워크는 부분적 사용이 불가능 하고, 프레임워크 안으로 들어가서 프레임워크가 지원해주는 문법에 따라서 작성해줘야 제대로 동작한다. 
  - 흔히, 리액트는 비교적 자유도가 높고, 뷰는 기능이 이미 다 정해져 있다고 한다. 
    - ex) Vue 는 오직 v-if 를 통해 렌더링 여부를 제어할 수 있었지만, React 는 개발자의 재량에 따라 자바스크립트 문법으로 구현할 수 있다. 
  - 컴포넌트 분리와 재사용 측면에서 효율적!
    - Vue 에서 새로운 컴포넌트를 분리하기 위해선, 새로운 파일을 하나 더 생성하고, 그에 따라 script style 도 작성해야 한다. 또한 props 전달하는 과정도 2개의 컴포넌트를 오가야 한다. 
    - React 는 조금 다르다!
  - Vue 도 장점이 있다 => https://kr.vuejs.org/v2/guide/comparison.html#React

## 2. React Tutorial

https://ko.reactjs.org/tutorial/tutorial.html

- 공식 튜토리얼을 통해 react 학습

### 환경설정 

**1. Node.js 설치 확인**

- Node 14.0.0, npm 5.6 상위 버전 필요 

**2. Create React App **

- Create React App는 Babel이나 webpack같은 build 도구를 사용하나, 설정 없이도 동작
- 프로덕션을 배포할 준비가 되었을 때, npm run build 를 실행하면 build 폴더 안에 제작한 앱의 최적화된 Build를 생성합니다
- npx : npm 5.2+ 버전의 패키지 실행 도구.

```bash
npx create-react-app my-app
```

**3. 새로운 프로젝트의 src/ 폴더에 있는 파일을 삭제**

```bash
cd my-app
cd src
rm -f *
cd ..
```

**4. src/ index.css, index.js 생성**

- index.css : https://codepen.io/gaearon/pen/oWWQNa?editors=0100

- index.js : https://codepen.io/gaearon/pen/oWWQNa?editors=0010
  - 아래 코드 추가

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
```

**5. 생성한 프로젝트를 브라우저에서 확인**

```bash
npm start
```

### 개요 

#### React 란?

> React는 사용자 인터페이스를 구축하기 위한 선언적이고 효율적이며 유연한 JavaScript 라이브러리입니다. “컴포넌트”라고 불리는 작고 고립된 코드의 파편을 이용하여 복잡한 UI를 구성하도록 돕습니다.

**React.Component 의 하위 클래스를 사용해보자**

```react
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// 사용 예제: <ShoppingList name="Mark" />
```

- XML 과 유사한 태그를 사용. 
- 컴포넌트를 사용하여 React 에세 화면에 표현하고 싶은 것이 무엇인지 알려준다. 
- 데이터가 변경되면, React 가 컴포넌트를 업데이트하고 다시 렌더링한다. 
- ShoppingList 는 React 컴포넌트 클래스 혹은 React 컴포넌트 타입으로, 
  - 개별 컴포넌트는 `props` 라는 매개변수를 받아오고, `render()` 함수를 통해 표시할 뷰 계층 구조를 반환한다. 
  - 컴포넌트는 캡슐화되어 독립적으로 동작 가능하며, 단순 컴포넌트를 조합하여 복잡한 UI 구현 가능하다. 

**render**

- render 함수는 화면에서 보고자 하는 내용을 반환.
- React 는 설명을 전달받고 결과를 표시 
- 특히, render 는 렌더링할 내용을 경량화할 **React 엘리먼트**를 반환
- 다수의 React 개발자는 "**JSX**" 라는 특수문법을 사용하여 React 구조를 보다 쉽게 작성

- 위의 코드는 빌드하는 시점에서 아래와 같이 변화한다. 

```react
return React.createElement('div', {className: 'shopping-list'},
  React.createElement('h1', /* ... h1 children ... */),
  React.createElement('ul', /* ... ul children ... */)
  //...
);
```

**JSX**

- JavaScript 의 강력한 기능을 가지고 있다. 
- JSX 내부의 중괄호 안에 어떤 JavaScript 표현식도 사용 가능
- React 엘리먼트는 JavaScript 객체이며 변수에 저장하거나 프로그램 여기 저기에 전달 가능

#### 초기 코드 살펴보기

**index.js** 

- 3 React Components 
  - Square : `<button>` 렌더링
  - Board : 9 Square 
  - Game 

#### Props 를 통해 데이터 전달하기 

**Board 컴포넌트에서 Square 컴포넌트로 데이터를 전달해보자**

- Board 의 `renderSquare` 함수 코드 수정

```react
class Board extends React.Component {
  renderSquare(i) {
    return <Square value={i} />;
  }
}
```

- 값을 표시하기 위해 Square 의 `render` 함수 수정

```react
class Square extends React.Component {
  render() {
    return (
      <button className="square">
        {this.props.value}
      </button>
    );
  }
}
```

#### 사용자와 상호작용하는 컴포넌트 만들기 

- Square 컴포넌트 클릭 시 'X' 가 클릭되도록 해보자 

```react
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={function() { console.log('click'); }}>
        {this.props.value}
      </button>
    );
  }
}
```

- 화살표 함수 이용!
  - onClick 이 prop 으로 함수를 전달하는 구조임을 알 수 있다. 

```react
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={() => console.log('click')}>
        {this.props.value}
      </button>
    );
  }
}
```

- **state** 를 사용하여 클릭한 것을 기억하도록 해보자 
  - React 컴포넌트는 생성자에 `this.state` 를 설정하여 state 를 가질 수 있다. 
  - `this.state` 는 정의된 React 컴포넌트에 대해 비공개로 간주해야 한다. 
  - 일단 생성자를 추가하여 state 를 초기화하자!
    - JavaScript 클래스와 같이, 하위 클래스의 생성자를 정의할 항상 super 를 호출해야 한다. 
    - React 컴포넌트 클래스는 생성자를 가질 때, `super(props)` 호출 구문부터 작성해야 한다. 

```react
class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }
  
  render() {
    return (
      <button className="square" onClick={() => console.log('click')}>
        {this.props.value}
      </button>
    );
  }
}
```

- Square 를 클릭할 때, 현재 state 값을 표시해보자 
  - click 시 state 값 변경, props value 대신 state value 렌더
  - render 함수 내부에서 onClick 핸들러를 통해 this.setState 를 호출하면, button 클릭 시 Square 가 다시 렌더링 되어야 함을 알릴 수 있다!
  - 여기선, click 시에 value 가 무조건 'X' 가 된다. 

```react
  render() {
    return (
      <button 
        className="square" 
        onClick={() => this.setState({value: 'X'})}
      >
        {this.state.value}
      </button>
    );
  }
```

#### 개발자 도구 

- [크롬 리액트 개발자 도구](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
- React Devtools 확장 프로그램을 통해 React 컴포넌트 트리를 검사할 수 잇다. 
- props 와 state 도 확인 간으!

****

### 게임 완성하기 

#### State 끌어올리기 

- 현재 게임의 state 를 각각의 Square 컴포넌트에서 유지하고 있다. 
- 승자를 확인하기 위해선 9 개 state 를 한 곳에 유지해야 한다. 

- 그렇다면 Board 가 state 를 요청해야 하는가? 
  - 이 방식은 코드를 이해하기 어렵고 버그에 취약하며 리팩토링이 어렵다!!!
- 각 Square 가 아닌 부모 Board 컴포넌트에 state 를 저장하는 것이 가장 좋은 방법이다. 

**여러 개의 자식으로부터 데이터를 모으거나, 두 개의 자식 컴포넌트들이 서로 통신하게 하려면**

- 부모 컴포넌트에 공유 state 를 정의해야 한다. 
- 부모는 다시 props 를 통해 자식 컴포넌트에 state 를 전달한다. 
- 이를 통해 자식이 서로 또는 부모와 동기화 하도록 만든다. 

- Vue 와 비슷한 것 같다~

****

- Board 에 초기 state 설정 

```react
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
    };
  }
    // ...
}
```

- 각 Square 가 현재 값('X', 'O', null) 을 표현하도록 renderSquare 수정

```react
  renderSquare(i) {
    return <Square value={this.state.squares[i]} />;
  }
```

- square 클릭 시 Board 를 변경할 방법이 필요.
  - 컴포넌트는 자신이 정의한 state 에만 접근할 수 있으므로 Square 에서 Board 를 직접 변경 불가
  - 대신에 Board 에서 Square 로 함수를 전달!
  - Board 에서 Square 로 value 와 onClick 두 개의 props 를 전달 

```react
  renderSquare(i) {
    return (
      <Square 
        value={this.state.squares[i]} 
        onClick={() => this.handleClick(i)}
      />
    );
  }
```

- Square 변경
  - constructor, setState 제거 
  - `this.props.value` 를 렌더, 

```react
class Square extends React.Component {
  render() {
    return (
      <button 
        className="square" 
        onClick={() => this.props.onClick()}
      >
        {this.props.value}
      </button>
    );
  }
}
```

- **Square 클릭 시 Board 에서 넘겨 받은 onClick 함수가 호출, 이 때 ** 
  1. 내장된 DOM `<button>` 컴포넌트에 있는 `onClick` prop 은 React 에게 클릭 이벤트 리스너를 설정하라고 알려줌
  2. 버튼 클릭 시 React 는 Square `render()` 에 정의된 `onClick` 이벤트 핸들러를 호출
  3. 이벤트 핸들러가 `this.props.onClick()` 을 호출
  4. Board 에서 전달한 `onCLick` 에 의해, Square 클릭 시 Board 의 `handleClick(i)` 를 호출
  5. 아직은 `handleClick()` 을 정의하지 않아서 에러!

- Board 에 `handleClick()` 추가 

```react
  handleClick(i) {
    const squares = this.state.squares.slice();
    squares[i] = 'X';
    this.setState({squares: squares});
  }
```

#### 정리

- 이전과 마찬가지로 Square 클릭으로 사각형을 채울 수 있다. 
- 그러나 이제는 state 가 Square 에 저장되는 것이 아니라, Board 에 저장된다. 
  - Square 컴포넌트는 Board 컴포넌트에서 값을 받아 클릭될 때, Board 컴포넌트로 정보를 전달한다. 
  - 이런 경우에, React 에선 Square 컴포넌트를 '제어되는 컴포넌트' 라 부른다. 
- `handleClick()` 은 `.slice()` 를 이용하여 기존 배열이 아니라, 복사본을 수정한다. 

#### 불변성의 중요성

**데이터 변경의 두 가지 방법**

- 객체 변경을 통해 데이터 수정하기 

```react
var player = {score: 1, name: 'Jeff'};
player.score = 2;
// now => player = {score: 2, name: 'Jeff'}
```

- 객체 변경 없이 데이터 수정하기

```react
var player = {score: 1, name: 'Jeff'};

var newPlayer = Object.assign({}, player, {score: 2});
// 이제 player는 변하지 않았지만 newPlayer는 {score: 2, name: 'Jeff'}입니다.

// 객체 spread 구문을 사용한다면 이렇게 쓸 수 있습니다.
// var newPlayer = {...player, score: 2};
```

**불변성의 장점**

- 복잡한 특징을 단순하게 만든다. 
  - ex) 틱택토에서 "시간 여행" 기능을 구현하여, 게임의 이력을 확인하고 이전 동작으로 되돌아가는 경우. 특정 행동을 취소하고 다시 실행하는 것이 유용하다.
  - 직접적인 데이터 변이를 피해 이전 버전의 이력을 유지하고 재사용 가능하게 함
- 변화를 감지 
  - 객체가 직접적으로 수정되기 때문에, 복제가 가능한 객체에서 변화를 감지하는 것이 어렵다. 
  - 불변 하는 객체는 이전 객체와 다른 것을 포착하여 변화를 감지하기 쉽가. 
- React 에서 다시 렌더링 하는 시기를 결정함
  - React 에서 순수 컴포넌트를 만드는 데 도움을 준다. 
  - 변하지 않는 데이터는 변경이 이루어졌는지 쉽게 판단이 가능하여, 이를 바탕으로 다시 렌더링 할 지 여부를 결정한다. 

#### 함수 컴포넌트

- Square 를 함수 컴포넌트로 바꾸자
- 함수 컴포넌트는 state 없이 render 함수만을 가진다. 
- React.Component 를 확장하는 클래스를 정의하는 대신 props 를 입력받아서 렌더링할 대상을 반환하는 함수를 작성할 수 있다. => 클래스 작성 보다 빠르다!

```react
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
```

- `this.props.value` => `props.value` 		& `onClick()` => `onClick`

#### 순서 만들기 

- "O" 가 표시되도록 하자 
- 첫번째 차례를 "X" 로 시작, 초기 state 를 수정

```react
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true,
    };
  }
```

- 플레이어가 수를 둘 때 마다 `xIsNext` 를 뒤집자 

```react
  handleClick(i) {
    const squares = this.state.squares.slice();
    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      squares: squares,
      xIsNext: !this.state.xIsNext,
    });
  }
```

- Board render 수정

```react
  render() {
    const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    //...
  }
```

#### 승자 결정하기

- `calculateWinner` 작성

```react
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```

- Board render 에서 `calculateWinner(squares)` 호출

```react
  render() {
    const winner = calculateWinner(this.state.squares);
    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }
    // ...
  }
```

- 승리 혹은 자리 없을 시 handleClick 무시 

```react
  handleClick(i) {
	// ...
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    // ... 
  }
```

### 시간 여행 추가하기 

- 이전 차례로 시간 되돌리기

#### 동작에 대한 기록 저장하기 

- 불변 객체를 이용해, 과거의 squares 배열의 모든 버전을 저장하고 지나간 차례 탐색 가능 

- 과거의 squares 배열들을 history 배열에 저장해보자 

  - 다음과 같은 형태일 것 

  ```react
  history = [
    // 첫 동작이 발생하기 전
    {
      squares: [
        null, null, null,
        null, null, null,
        null, null, null,
      ]
    },
    // 첫 동작이 발생한 이후
    {
      squares: [
        null, null, null,
        null, 'X', null,
        null, null, null,
      ]
    },
    // 두 번째 동작이 발생한 이후
    {
      squares: [
        null, null, null,
        null, 'X', null,
        null, null, 'O',
      ]
    },
    // ...
  ]
  ```

#### 다시 State 끌어올리기 

- 이전 동작에 대한 리스트를 보여주기 위해, 최상위 단계의 Game 컴포넌트가 필요 
- history state 를 Game 컴포넌트에 생성하자. 
  - 이 때, Board 에서 squares state 를 더 이상 사용하지 않아도 된다. 

```react
class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      history: [{
        squares: Array(9).fill(null),
      }],
      XIsNext: true,
    };
  }
  //...
}
```

- Game ==> Board 로 squares, onClick props 전달 
  - Board 의 constructor 제거
  - `this.state.squares[i]` ==> ` this.props.squares[i]`
  - `this.handleClick(i)` ==> `this.props.onClick(i)`
-  Game render 수정

```react
  render() {
    const history = this.state.history;
    const current = history[history.length - 1];
    const winner = calculateWinner(current.squares);
    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }

    return (
      <div className="game">
        <div className="game-board">
          <Board 
            squares={current.squares}
            onClick={(i) => this.handleClick(i)}
          />
        </div>
        <div className="game-info">
          <div>{ status }</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
```

- Board render 에서 중복되는 코드 제거 

- Game 에 handleClick 생성
  - `push()` 와 달리, `concat()` 은 기존 배열을 변경하지 않기 때문에 이를 권장

```react
  handleClick(i) {
    const history = this.state.history;
    const current = history[history.length - 1];
    const squares = current.squares.slice();

    if (calculateWinner(squares) || squares[i]) {
      return;
    }

    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      history: history.concat([{
        squares:squares,
      }]),
      xIsNext: !this.state.xIsNext,
    });
  }
```

#### 과거의 이동 표시하기

- map 을 이용하자 

  - ex) 

  ```js
  const numbers = [1, 2, 3];
  const doubled = numbers.map(x => x * 2); // [2, 4, 6]
  ```

- map 을 이용하여 이동 기록은 화면에 표시되는 React 버튼 엘리먼트로 매핑하고, 과거의 이동으로 돌아가는 버튼 목록을 표시할 수 있다. 
- Game render 에서 history 를 map!
  - step : 현재 history 요소의 값 참조
  - move : 현재 history 요소의 인덱스 참조

```react
render() {
    //...
    const moves = history.map((step, move) => {
      const desc = move ?
        'Go to move #' + move :
        'Go to game start';
      return (
        <li>
          <button onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      );
    });
    // ... 
}
```

#### Key 선택하기

**경고 배열이나 이터레이터의 자식들은 고유의 “key” prop을 가지고 있어야 합니다. “Game”의 render 함수를 확인해주세요.**

- 리스트를 렌더링할 때 React 는 렌더링하는 리스트 아이템에 대한 정보를 저장하고, 리스트를 업데이트 할 때 React 는 무엇이 변했는지 결정해야 한다. 

- ex) 

  ```react
  <li>Alexa: 7 tasks left</li>
  <li>Ben: 5 tasks left</li>
  ```

  위 코드가 아래와 같이 변경

  ```react
  <li>Ben: 9 tasks left</li>
  <li>Claudia: 8 tasks left</li>
  <li>Alexa: 5 tasks left</li>
  ```

  -  key prop 을 지정하여 각 아이템이 다른 아이템들과 다르다는 것을 React 에 알려준다.

  ```react
  <li key={user.id}>{user.name}: {user.taskCount} tasks left</li>
  ```

  - React 가 각 리스트 아이템의 키를 비교하여 일치/불일치 키를 탐색한다. 

- React 는 엘리먼트가 생성되면 key 속성을 추출하여, 반환되는 엘리먼트에 직접 키를 저장

- 그러나 this.props.key 로 참조가 불가능

**동적인 리스트를 만들 때마다 적절한 키를 할당해라!**

- 키가 지정되지 않는 경우엔, 배열의 인덱스를 기본 키로 사용한다. 
- 그러나 이는, 리스트 아이템 순서가 바뀌거나 추가 제거 시 문제가 발생한다!

#### 시간 여행 구현하기 

- 틱택토 게임에선, 과거의 이동이 고유한 숫자 ID 를 가지기 때문에, 이를 키로 사용해도 안전

- Game render 내에서 key 를 추가하자 

```react
      // ... 
	  return (
        <li key={move}>
          <button onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      );
```

- `jumpTo()` 구현 및 `stepNumber` 추가 
  - Game constructor state 에 `stepNumber` 추가 
  - stepNumber 가 짝수일 때마다, xIsNext 를 true 로 설정

```react
  jumpTo(step) {
    this.setState({
      stepNumber: step,
      xIsNext: (step % 2) === 0,
    });
  }
```

- 위의 경우엔, history 는 업데이트 되지 않는다! (언급된 속성만 업데이트하는 `setState()` 의 특성)
- `handleClick` 수정

```react
    handleClick(i) {
        const history = this.state.history.slice(0, this.state.stepNumber + 1);
        // ..
		this.setState({
            //...
            stepNumber: history.length,
        })
    }
```

- 마지막으로 stepNumber 에 맞는 현재 선택된 이동을 렌더링!!!
  - 차례를 선택할 시 게임판을 즉시 업데이트!

```react
    render() {
        //...
        const current = history[this.state.stepNumber];
        //...
    }
```

## 끝!











