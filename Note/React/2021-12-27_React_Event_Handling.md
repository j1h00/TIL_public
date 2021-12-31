# TIL : Handling Events

React 의 Event Handling 은 DOM 엘리먼트의 방식과 매우 유사하다. 다만,

- React 의 이벤트는 소문자 대신 camelCase 를 사용

- JSX 를 사용하여 문자열이 아닌 함수로 이벤트 핸들러를 전달

    HTML 의 경우 

    ```react
    <button onclick="activateLasers()">
      Activate Lasers
    </button>
    ```

    React 의 경우 

    ```react
    <button onClick={activateLasers}>
      Activate Lasers
    </button>
    ```

- 또한, React 는 `false` 를 반환해도 기본 동작을 방지할 수 없다. 반드시 `preventDefault` 를 명시적으로 호출해야 한다. 

    HTML 의 경우 

    ```react
    <form onsubmit="console.log('You clicked submit.'); return false">
      <button type="submit">Submit</button>
    </form>
    ```

    React 의 경우 

    ```react
    function Form() {
      function handleSubmit(e) {
        e.preventDefault();
        console.log('You clicked submit.');
      }
    
      return (
        <form onSubmit={handleSubmit}>
          <button type="submit">Submit</button>
        </form>
      );
    }
    ```

    - 여기서 `e` 는 synthetic event[(합성 이벤트)](https://ko.reactjs.org/docs/events.html)이다.

React 사용 시, 리스너를 추가하기 위해 DOM 엘리먼트 생성 후 `addEventListener` 를 호출할 필요가 없다. 대신 엘리먼트가 처음 렌더링 될 때 리스너를 제공하면 된다. 

ES6 class 를 사용하여 컴포넌트 정의 시, 일반적으로 이벤트 핸들러를 클래스의 메서드로 만든다. 

예를 들어, 

```react
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // 콜백에서 `this`가 작동하려면 아래와 같이 바인딩 해주어야 합니다.
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

- Toggle 컴포넌트 내에 `handleClick()` 라는 클래스 메서드를 정의하여 사용한다. 

- JSX 콜백 안에서 `this` 는 어떤 의미를 갖는가?
  - JavaScript 에서 클래스 메서드는 기본적으로 [바인딩](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) 되어 있지 않다. 
  - 위에서 바인딩 없이 `onClick` 에 전달 시, 함수가 실제 호출되면 `this` 는 `undefined` 가 된다.
  - 이는 JavaScript 에서 함수가 작동하는 방식의 일부이며, `onClick={this.handleClick}` 과 같이 뒤에 `()` 를 사용하지 않고 메서드를 참조할 경우, 해당 메서드를 바인딩해야 한다. 

- bind 호출이 불편하다면? 
  - 퍼블릭 클래스 필드를 사용하는 경우엔 올바르게 바인딩된다.

    ```react
    class LoggingButton extends React.Component {
      // 이 문법은 `this`가 handleClick 내에서 바인딩되도록 합니다.
      // 주의: 이 문법은 *실험적인* 문법입니다.
      handleClick = () => {
        console.log('this is:', this);
      }
    
      render() {
        return (
          <button onClick={this.handleClick}>
            Click me
          </button>
        );
      }
    }
    ```

  - 혹은 콜백에 화살표 함수 사용

    ```react
    class LoggingButton extends React.Component {
      handleClick() {
        console.log('this is:', this);
      }
    
      render() {
        // 이 문법은 `this`가 handleClick 내에서 바인딩되도록 합니다.
        return (
          <button onClick={() => this.handleClick()}>
            Click me
          </button>
        );
      }
    }
    ```

    - 그러나 이 경우 `LoggingButton` 이 렌더링 될 때마다 다른 콜백이 생성된다. 만약 콜백이 하위 컴포넌트에 props 로 전달되는 경우 추가로 렌더링을 수행하게 되어 성능 문제를 발생시킨다. 

### 이벤트 핸들러에 인자 전달하기

일반적으로 루프 내부에서는 추가적인 매개변수를 전달한다. 아래 두 코드가 모두 작동한다. 

```react
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

