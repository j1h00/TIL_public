# TIL : Conditional Rendering

원하는 동작은 캡슐화하는 컴포넌트를 만들 수 있다! 

React 에서 조건부 렌더링은 JavaScript 에서의 조건 처리와 동일하다. 

```react
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

ReactDOM.render(
  // Try changing to isLoggedIn={true}:
  <Greeting isLoggedIn={false} />,
  document.getElementById('root')
);
```

### 엘리먼트 변수 

엘리먼트를 저장하기 위해 변수를 사용할 수 있다. 이를 통해 컴포넌트 일부를 조건부로 렌더링한다. 

로그인, 로그아웃 버튼을 예로 들자. 아래 두 컴포넌트가 있을 때, 

```react
function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}
```

`LoginControl` 컴포넌트를 다음과 같이 정의할 수 있다. 

```react
class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}

ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);
```

### 논리 && 연산자로 인라인 If 표현하기

더 짧은 구문을 사용하고 싶을 때, JSX 안에서 인라인으로 처리해보자 

JSX 안 중괄호 표현식에, JavaScript 논리연산자 && 을 사용하자

```react
function Mailbox(props) {
  const unreadMessages = props.unreadMessages;
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&
        <h2>
          You have {unreadMessages.length} unread messages.
        </h2>
      }
    </div>
  );
}

const messages = ['React', 'Re: React', 'Re:Re: React'];
ReactDOM.render(
  <Mailbox unreadMessages={messages} />,
  document.getElementById('root')
);
```

- true && expression 은 항상 expression 으로 평가되고, false && expression 은 항상 false 로 평가되므로, && 뒤의 엘리먼트는 항상 조건이 true 인 경우에만 출력된다. 

- 그러나 false && expression 에서, && 뒤의 expression 은 건너뛰지만, 결과적으로 false 표현식이 반환되는 것에 주의해야 한다. 

  ```react
  render() {
    const count = 0;
    return (
      <div>
        { count && <h1>Messages: {count}</h1>}
      </div>
    );
  }
  ```

  - 이 경우 `<div>0</div>` 가 출력된다. 

### 조건부 연산자로 If-Else 구문 인라인으로 표현하기

`condition ? true : false` 구문을 사용하는 방법도 있다. 

 ```react
 render() {
   const isLoggedIn = this.state.isLoggedIn;
   return (
     <div>
       The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
     </div>
   );
 }
 ```

```react
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
      {isLoggedIn
        ? <LogoutButton onClick={this.handleLogoutClick} />
        : <LoginButton onClick={this.handleLoginClick} />
      }
    </div>
  );
}
```

- 가독성이 좋다고 생각하는 방식을 택하면 된다. 

### 컴포넌트가 렌더링 하는 것을 막기

가끔 다른 컴포넌트에 의해 렌더링될 때 컴포넌트 자체를 숨기고 싶을 수 있다. 

이 때는 렌더링 결과를 반환하는 대신, `null` 을 반환하면 해결할 수 있다. 

아래 예시에서는, `<WarningBanner />` 가 `warn` prop 값에 의해서 렌더링 된다. 

```react
function WarningBanner(props) {
  if (!props.warn) {
    return null;
  }

  return (
    <div className="warning">
      Warning!
    </div>
  );
}

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {showWarning: true};
    this.handleToggleClick = this.handleToggleClick.bind(this);
  }

  handleToggleClick() {
    this.setState(state => ({
      showWarning: !state.showWarning
    }));
  }

  render() {
    return (
      <div>
        <WarningBanner warn={this.state.showWarning} />
        <button onClick={this.handleToggleClick}>
          {this.state.showWarning ? 'Hide' : 'Show'}
        </button>
      </div>
    );
  }
}

ReactDOM.render(
  <Page />,
  document.getElementById('root')
);
```
