# TIL : Composition vs Inheritance

React 는 상속 대신 합성을 사용하여 컴포넌트 간에 코드를 재사용하는 것이 좋다!!

### Containment : 컴포넌트에서 다른 컴포넌트를 담기

어떤 컴포넌트들은 어떤 자식 엘리먼트가 들어올 지 미리 예상할 수 없는 경우가 있다. 

범용적인 '박스' 역할을 하는 Sidebar 혹은 Dialog 와 같은 컴포넌트에서 자주 보인다. 

이 때는 특수한 `children` prop 을 사용하여 자식 엘리먼트를 출력에 그대로 전달할 수 있다. 

```react
function FancyBorder(props) {
  return (
    <div className={'FancyBorder FancyBorder-' + props.color}>
      {props.children}
    </div>
  );
}
```

```react
function WelcomeDialog() {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        Welcome
      </h1>
      <p className="Dialog-message">
        Thank you for visiting our spacecraft!
      </p>
    </FancyBorder>
  );
}
```

- JSX 를 중첩하여 임의의 자식을 전달!
- `<FancyBorder>` JSX 태그 안에 있는 자식들이 `children` prop 으로 전달 

종종 컴포넌트에 여러 'hole' 이 필요한 경우 `children` 대신 자신만의 방식을 적용 가능

```react
function SplitPane(props) {
  return (
    <div className="SplitPane">
      <div className="SplitPane-left">
        {props.left}
      </div>
      <div className="SplitPane-right">
        {props.right}
      </div>
    </div>
  );
}

function App() {
  return (
    <SplitPane
      left={
        <Contacts />
      }
      right={
        <Chat />
      } />
  );
}
```

`<Contacts />`, `<Chat />` 같은 React 엘리먼트 역시 객체이므로, 다른 데이터처럼 prop으로 전달 가능하다. 

### Specialization : 특수화

어떤 컴포넌트의 "특수한 경우" 의 컴포넌트를 고려해야 할 때, 합성을 통해 해결할 수 있다. 

더 "구체적인" 컴포넌트가 "일반적인" 컴포넌트를 렌더링하고 props 를 통해 내용을 구성

```react
function Dialog(props) {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
    </FancyBorder>
  );
}

function WelcomeDialog() {
  return (
    <Dialog
      title="Welcome"
      message="Thank you for visiting our spacecraft!" />
  );
}
```

- Wow !! 

아래 처럼 클래스 컴포넌트에서도 동일하게 적용된다.

```react
function Dialog(props) {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
      {props.children}
    </FancyBorder>
  );
}

class SignUpDialog extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSignUp = this.handleSignUp.bind(this);
    this.state = {login: ''};
  }

  render() {
    return (
      <Dialog title="Mars Exploration Program"
              message="How should we refer to you?">
        <input value={this.state.login}
               onChange={this.handleChange} />
        <button onClick={this.handleSignUp}>
          Sign Me Up!
        </button>
      </Dialog>
    );
  }

  handleChange(e) {
    this.setState({login: e.target.value});
  }

  handleSignUp() {
    alert(`Welcome aboard, ${this.state.login}!`);
  }
}
```







