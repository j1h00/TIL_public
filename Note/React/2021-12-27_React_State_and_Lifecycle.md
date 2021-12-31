# TIL : State and Lifecycle

엘리먼트 렌더링에서 다루어본 시계 예시를 다시 살펴보자.

이 때, UI 를 업데이트 (렌더링 된 출력값을 변경) 하기 위해서는 `ReactDOM.render()` 를 호출했었다. 

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

**Clock 컴포넌트 추출**

- 시계의 모양에 따라 캡슐화 

```react
function Clock(props) {
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {props.date.toLocaleTimeString()}.</h2>
    </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

- `Clock` 스스로 타이머를 설정하고, 매초 UI 를 업데이트 하도록 해보자 

```react
ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

- 이를 위해선 `Clock` 컴포넌트에 **state** 를 추가해야 한다. 
- State 는 props 와 유사하지만, 비공개이며 컴포넌트에 의해 완전히 제어된다.

### 함수에서 클래스로 변환하기

함수 컴포넌트인 `Clock` 을 클래스로 변환하기 

1. `React.Component` 를 확장하는 동일한 이름의 ES6 class 를 생성
2. `render()` 라고 불리는 빈 메서드를 추가 
3. 함수의 내용을 `render()` 메서드 안으로 이동
4. `render()` 내용 안에 있는 `props` 를 `this.props` 로 변경
5. 남아있는 빈 함수 선언 삭제

```react
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

- `render` 메서드는 업데이트가 발생할 때마다 호출되지만, 같은 DOM 노드로 `<Clock />` 을 렌더링 하는 경우, `Clock` 클래스의 단일 인스턴스만 사용된다. 이를 통해 local state 와 lifecycle method 와 같은 기능이 사용 가능하다. 

### 클래스에 로컬 State 추가하기 

`date` 를 props 에서 state 로 변경해보자!

1. `render()` 메서드 안에 있는 `this.props.date` 를 `this.state.date` 로 변경
2. 초기 `this.state` 를 지정하는 class constructor 추가
   - 클래스 컴포넌트는 항상 `props` 로 기본 constructor 를 호출해야 한다. 
3. `<Clock /> ` 요소에서 `date` prop 삭제

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

### Lifecycle 메서드를 클래스에 추가하기 

`Clock` 이 스스로 타이머를 설정하고 매초 스스로 업데이트 하도록 만들어 보자!

- 마운팅 : `Clock`이 [ 처음 DOM 에 렌더링 될 때 ] 마다 타이머를 설정
- 언마운팅 : `Clock` 에 의해 [ 생성된 DOM 이 삭제될 때 ]마다 타이머를 해제

컴포넌트 클래스에서 특별한 메서드를 선언하면, 마운트 혹은 언마운트 될 때 코드 작동 가능 

```react
class Clock extends React.Component {
    // ...
    componentDidMount() {
 	}

  	componentWillUnmount() {
  	}
}
```

이러한 메서드들을 Lifecycle method 라 부른다. 

`componentDidMoung()` 메서드는 컴포넌트 출력물이 DOM 에 렌더링 된 후에 실행된다. 

```react
  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000);
  }
```

`timerID` 와 같이 데이터 흐름 안에 포함되지 않는 어떤 항목을 보관할 필요가 있다면, 클래스에 수동으로 부가적인 필드를 추가해도 된다. 

`componentWillUnmount()` 내에 있는 타이머를 분해해보자 

```react
  componentWillUnmount() {
    clearInterval(this.timerID);
  }
```

`Clock` 컴포넌트가 매초 작동하도록 하는 `tick()` 메서드를 구현해보자 

```react
  tick() {
    this.setState({
      date: new Date()
    });
  }
```

- `Clock` 컴포넌트의 로컬 state 를 업데이트 하기 위해 `this.setState()` 를 사용한다. 

**메서드 호출 순서 정리**

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }
    
  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

>1. `<Clock />`가 `ReactDOM.render()`로 전달되었을 때 React는 `Clock` 컴포넌트의 constructor를 호출합니다. `Clock`이 현재 시각을 표시해야 하기 때문에 현재 시각이 포함된 객체로 `this.state`를 초기화합니다. 나중에 이 state를 업데이트할 것입니다.
>2. React는 `Clock` 컴포넌트의 `render()` 메서드를 호출합니다. 이를 통해 React는 화면에 표시되어야 할 내용을 알게 됩니다. 그 다음 React는 `Clock`의 렌더링 출력값을 일치시키기 위해 DOM을 업데이트합니다.
>3. `Clock` 출력값이 DOM에 삽입되면, React는 `componentDidMount()` 생명주기 메서드를 호출합니다. 그 안에서 `Clock` 컴포넌트는 매초 컴포넌트의 `tick()` 메서드를 호출하기 위한 타이머를 설정하도록 브라우저에 요청합니다.
>4. 매초 브라우저가 `tick()` 메서드를 호출합니다. 그 안에서 `Clock` 컴포넌트는 `setState()`에 현재 시각을 포함하는 객체를 호출하면서 UI 업데이트를 진행합니다. `setState()` 호출 덕분에 React는 state가 변경된 것을 인지하고 화면에 표시될 내용을 알아내기 위해 `render()` 메서드를 다시 호출합니다. 이 때 `render()` 메서드 안의 `this.state.date`가 달라지고 렌더링 출력값은 업데이트된 시각을 포함합니다. React는 이에 따라 DOM을 업데이트합니다.
>5. `Clock` 컴포넌트가 DOM으로부터 한 번이라도 삭제된 적이 있다면 React는 타이머를 멈추기 위해 `componentWillUnmount()` 생명주기 메서드를 호출합니다.



### State 올바르게 사용하기 

#### 1. 직접 State 를 수정해서는 안된다. 

다음과 같은 코드는 컴포넌트를 다시 렌더링 하지 않는다. 

```react
// Wrong
this.state.comment = 'Hello';
```

대신에 `setState()` 를 사용하자 

```react
// Correct
this.setState({comment: 'Hello'});
```

`this.state` 를 지정할 수 있는 유일한 공간은 contructor 이다. 

#### 2. State 업데이트는 비동기적일 수도 있다. 

React 는 성능을 위해 여러 `setState()` 호출을 단일 업데이트로 한번에 처리할 수 있따. 

`this.props` 와 `this.state` 가 비동기적으로 업데이트 될 수 있기 때문에, state 를 계산할 때, 다른 state 값에 의존해서는 안된다. 

예를 들어,

```react
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});
```

이러한 경우엔, 객체보다는 함수를 인자로 사용하는 다른 형태의 `setState()` 를 사용한다. 이 함수는 이전 state 를 첫 번째 인자로, 업데이트가 적용된 시점의 props 를 두 번째 인자로 받는다. 

```react
// Correct
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

#### 3. State 업데이트는 병합된다. 

`setState()` 를 호출할 때 React 는 제공한 객체를 현재 state 로 병합한다.

예를 들어, 다양한 독립적인 변수가 포함된 경우

```react
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      comments: []
    };
  }
```

별도의 `setState()` 호출로 변수를 독립적으로 업데이트 가능

```react
  componentDidMount() {
    fetchPosts().then(response => {
      this.setState({
        posts: response.posts
      });
    });

    fetchComments().then(response => {
      this.setState({
        comments: response.comments
      });
    });
  }
```

- 병합은 shallow 하게 이루어지기 때문에, `this.setState({comments})` 는 `this.state.posts`에 영향을 주지 않고, `this.state.comments` 는 완전히 대체한다. 

****

### 데이터는 아래로 흐른다 !

부모 자식 컴포넌트 모두, 특정 컴포넌트가 유상태(stateful) 인지 무상태(stateless) 인지 알 필요가 없으며, 함수 혹은 클래스로 정의되었는지 관심 가질 필요가 없다. 

때문에, state 는 local 혹은 encapsulated 라고 불린다. state 를 소유하고 설정한 컴포넌트 이외에 다른 어떤 컴포넌트에서 접근할 수 없다. 

컴포넌트는 자신의 state 를 자식 컴포넌트에 props 로 전달한다. 

```react
<FormattedDate date={this.state.date} />
```

그러나 `FormattedDate` 컴포넌트는 자신이 props 로 받은 데이터가 `Clock` 의 어떤 데이터로부터 왔는지 알 수 없다!

이를 일반적으로 “top-down” 혹은 “unidirectional” 데이터 흐름 이라고 한다. 컴포넌트가 소유한 state 로부터 파생된 UI 또는 데이터는 오직 트리 구조에서 자신의 아래에 있는 컴포넌트에만 영향을 미친다!

예를 들어, 아래의 각 Clock 은 자신만의 타이머를 설정하고 독립적으로 업데이트 한다. 

```react
function App() {
  return (
    <div>
      <Clock />
      <Clock />
      <Clock />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```











