# TIL : Forms

HTML 폼 엘리먼트는 자체적으로 내부 state 를 가지기 때문에, React 의 다른 DOM 엘리먼트와 다르게 동작한다. 

```react
<form>
  <label>
    Name:
    <input type="text" name="name" />
  </label>
  <input type="submit" value="Submit" />
</form>
```

- 위와 같은 폼은 , 폼을 제출할 경우 새로운 페이지로 이동하는 기본 HTML 폼 동작을 수행한다. 
- 대부분의 경우, React 에서는 위와 동일한 동작을 수행하는 것 보다는
  -  JavaScript 함수로 폼의 제출을 처리하고 사용자가 폼에 입력한 데이터에 접근하도록 하는 것이 편리하다. 
- 이를 제어 컴포넌트 (controlled components) 라 한다. 

### 제어 컴포넌트 (Controlled Component)

HTML 의 `<input>`, `<textarea>`, `<select>` 와 같은 폼 엘리먼트는 일반적으로 사용자의 입력을 기반으로 자신의 state 를 관리하고 업데이트한다. React 에선 변경할 수 있는 state 가 일반적으로 컴포넌트의 state 속성에 유지되며, `setState()` 에 의해 업데이트 된다. 

React state 를 "single source of truth" 로 만들어 위의 두 요소를 결합할 수 있다. 이 때, 폼을 렌더링하는 React 컴포넌트는 폼에 발생하는 사용자 입력값을 제어한다. 이 방식으로 REact 에 의해 값이 제어되는 폼 엘리먼트를 "Controlled Component" 라고 한다. 

예를 들어, 

```react
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

폼 엘리먼트에 설정된 `value` 속성에 의해, 표시되는 값은 항상 `this.state.value` 가 되고, React state 는 single source of truth 가 된다. React state 를 업데이트하기 위해 모든 키 입력에서 `handleChange` 가 동작하기 때문에 사용자가 입력할 때마다 보여지는 값이 업데이트 된다. 

=> Vue 의 v-model 과 같은 결과를 낳는다. 

제어 컴포넌트로 사용하면, input 의 값은 React state 에 의해 결정된다. 이 경우, 다른 UI 엘리먼트에 input 의 값을 전달하거나 다른 이벤트 핸들러에서 값을 재설정 하는 것도 가능하다. 

### textarea 태그 

```react
<textarea>
  Hello there, this is some text in a text area
</textarea>
```

위의 HTML 에서의 `<textarea>` 태그와는 다르게  React 에서 `<textarea>` 는 `value` 속성을 대신 사용한다. 

```react
class EssayForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Please write an essay about your favorite DOM element.'
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('An essay was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Essay:
          <textarea value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

### select 태크

HTML 에서 `<select>`는 드롭다운 목록을 만든다. 

```react
<select>
  <option value="grapefruit">Grapefruit</option>
  <option value="lime">Lime</option>
  <option selected value="coconut">Coconut</option>
  <option value="mango">Mango</option>
</select>
```

React 에서는 `selected` 속성을 사용하는 대신 최상단 `select` 태그에 `value` 속성을 사용한다. 

```react
class FlavorForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: 'coconut'};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('Your favorite flavor is: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Pick your favorite flavor:
          <select value={this.state.value} onChange={this.handleChange}>
            <option value="grapefruit">Grapefruit</option>
            <option value="lime">Lime</option>
            <option value="coconut">Coconut</option>
            <option value="mango">Mango</option>
          </select>
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

- 또한 `select` 태그에 multiple 옵션을 허용하면, `value` 속성값으로 배열을 전달할 수 있다. 

### 다중 입력 제어하기

여러 `input` 엘리먼트 제어 시, 

엘리먼트에 `name` 속성을 추가하여, `event.target.name` 값을 통해 핸들러에게 넘겨준다. 

```react
class Reservation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isGoing: true,
      numberOfGuests: 2
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  render() {
    return (
      <form>
        <label>
          Is going:
          <input
            name="isGoing"
            type="checkbox"
            checked={this.state.isGoing}
            onChange={this.handleInputChange} />
        </label>
        <br />
        <label>
          Number of guests:
          <input
            name="numberOfGuests"
            type="number"
            value={this.state.numberOfGuests}
            onChange={this.handleInputChange} />
        </label>
      </form>
    );
  }
}
```

### 제어 컴포넌트의 대안

모든 데이터 변경에 대해 이벤트 핸들러를 작성하고 입력 상태를 연결해야 하므로 귀찮을 수 있다..

1. 비제어 컴포넌트 (https://ko.reactjs.org/docs/uncontrolled-components.html)
2. Formik (https://formik.org/)

