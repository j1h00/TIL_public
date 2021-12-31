# TIL : Components & Props

### Components

컴포넌트를 통해 UI 를 재사용 가능한 개별적인 여러 조각으로 나누고, 각 조각을 개별적으로 관리할 수 있다. 

컴포넌트 API => https://ko.reactjs.org/docs/react-component.html

개념적으로 컴포넌트는 JavaScript 함수와 유사하다. props 라고 하는 임의의 인자를 받은 후, 화면에 render 되는 React 엘리먼트를 반환한다. 

### 함수 컴포넌트와 클래스 컴포넌트 

**함수 컴포넌트** == JavaScript 함수 

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

**클래스 컴포넌트**

- ES6 class 를 사용하여 컴포넌트를 정의할 수 있다. 

```react
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

- React 관점에서 위 두 컴포넌트는 동일하다 

### 컴포넌트 렌더링

기존에는 DOM 태그만을 사용해 엘리먼트를 나타냈다. 

```react
const element = <div />;
```

이젠, 사용자 정의 컴포넌트로 엘리먼트를 나타낼 수 있다. 

```react
const element = <Welcome name="Sara" />;
```

React 가 사용자 정의 컴포넌트로 작성한 엘리먼트를 발견하면, JSX 속성과 자식을 해당 컴포넌트에 단일 객체로 전달한다. 이 객체를 ***props*** 라고 한다.

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

- 위 결과로 페이지에 "Hello, Sara" 가 렌더링 된다. 

1. `<Welcome name="Sara" />` 엘리먼트로 `ReactDOM.render()` 를 호출
2. React 는 `{name: 'Sara'}` 를 props 로 하여 `Welcome` 컴포넌트를 호출
3. `Welcome` 컴포넌트는 `<h1>Hello, Sara<h1>` 엘리먼트를 반환
4. React DOM 은 `Welcome` 이 반환한 엘리먼트와 일치하도록 DOM 을 업데이트

- 컴포넌트 이름은항상 대문자로 시작한다. (React 는 소문자로 시작하는 컴포넌트는 DOM 태그로 처리)

### 컴포넌트 합성 

컴포넌트는 자신의 출력(return) 에 다른 컴포넌트를 참조할 수 있다. 

React 앱에서는 버튼, 폼, 다이얼로그, 화면 등 의 모든 것들이 흔히 컴포넌트로 표현된다. 

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

- 일반적으로 새 React 앱은 최상위에 단일 `App` 컴포넌트를 가지고 있다. 그러나 기존 앱에 React 를 통합하는 경우엔, `Button` 과 같은 작은 컴포넌트부터 시작해서 뷰 계층의 상단으로 올라가면서 점진적으로 작업해야 한다. 

### 컴포넌트 추출

컴포넌트를 여러 개의 작은 컴포넌트로 나누어보자!

```react
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <img className="Avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

- `Comment` 는 props 로 `author`, `text`, `date` 를 받은 후 SNS 웹사이트의 댓글을 표시한다. 
- 이 컴포넌트에서 몇가지 컴포넌트를 추출해보자 

**1. Avatar 추출**

- `Avatar` 는 자신이 `Comment` 내에서 렌더링 된다는 것을 알 필요가 없으므로, `author` 대신 일반화된 `user` 를 사용할 수 있다.  

```react
function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```

**2. UserInfo 추출**

```react
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
      </div>
    </div>
  );
}
```

**3. 결과**

```react
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

이 같은 컴포넌트 추출 작업은 더 큰 앱에서의 재사용성 측면에서 두각을 나타낸다. 

### props 는 읽기 전용!

함수 컴포넌트와 클래스 컴포넌트 모두 컴포넌트의 자체 props 를 수정해서는 안된다. 

```react
function sum(a, b) {
  return a + b;
}
```

- 위와 같은 함수를 **순수 함수**라고 한다. 
  - 입력값을 바꾸려 하지 않고, 항상 동일한 입력값에 대해서는 동일한 결과를 반환

반면에 다음 함수는 자신의 입력값을 변경하므로 순수 함수가 아니다. 

```react
function withdraw(account, amount) {
  account.total -= amount;
}
```

***모든 React 컴포넌트는 자신의 props 를 다룰 때 반드시 순수 함수처럼 동작해야 한다.***

- React 는 state 를 통해 위 규칙을 위반하지 않고, 동적이며 시간에 따라 변화하는 애플리케이션 UI 를 구성할 수 있다. 



















