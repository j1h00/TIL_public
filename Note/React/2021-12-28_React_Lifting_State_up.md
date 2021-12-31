# TIL : Lifting State up 

가장 가까운 공통 조상으로 state 끌어올리기!

- 동일한 데이터에 대한 변경사항을 여러 컴포넌트에 반영해야 할 필요가 있을 때!

온도 계산기를 만드는 과정을 진행해보자!

```react
function BoilingVerdict(props) {
  if (props.celsius >= 100) {
    return <p>The water would boil.</p>;
  }
  return <p>The water would not boil.</p>;
}
```

- `BoilingVerdict` 컴포넌트는 `celsius` prop 을 받아서 물이 끓기 충분한지 여부를 출력

```react
class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {temperature: ''};
  }

  handleChange(e) {
    this.setState({temperature: e.target.value});
  }

  render() {
    const temperature = this.state.temperature;
    return (
      <fieldset>
        <legend>Enter temperature in Celsius:</legend>
        <input
          value={temperature}
          onChange={this.handleChange} />
        <BoilingVerdict
          celsius={parseFloat(temperature)} />
      </fieldset>
    );
  }
}
```

- `Calculator` 컴포넌트는 온도를 입력할 수 있는 `<input>` 을 렌더링하고, `this.state.temperature` 에 저장

### 두번째 input 추가하기

섭씨 뿐만 아니라 화씨 입력 필드도 추가해보자!

이를 위해 `Calculator` 에서 `TemperatureInput` 컴포넌트를 빼내보자.

```react
const scaleNames = {
  c: 'Celsius',
  f: 'Fahrenheit'
};

class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {temperature: ''};
  }

  handleChange(e) {
    this.setState({temperature: e.target.value});
  }

  render() {
    const temperature = this.state.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature}
               onChange={this.handleChange} />
      </fieldset>
    );
  }
}
```

- `TemperatureInput` 은 `scale` prop 을 받아 `"c"` 또는 `"f"` 를 구분할 수 있도록 하자.

최종적으로 `Calculator` 는 분리된 두개의 `TemperatureInput` 을 통해, 두 개의 온도 입력 필드를 렌더링 할 수 있다. 

```react
class Calculator extends React.Component {
  render() {
    return (
      <div>
        <TemperatureInput scale="c" />
        <TemperatureInput scale="f" />
      </div>
    );
  }
}
```

- 그러나 이 상태에선, 둘 중 하나에 온도를 입력하더라도 다른 하나가 갱신되지 않는다. (동기화가 안됨!)

- 또한 `Calculator`가  temperature 를 가지고 있지 않으므로,  `BoilingVerdict` 도 보여줄 수 없다. 

### 변환 함수 작성하기

일단 섭씨 화씨 변환함수 작성

```react
function toCelsius(fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
  return (celsius * 9 / 5) + 32;
}
```

- 위 두 함수를 이용해서, 한 입력값에 기반해 나머지 입력값을 계산하는 용도로 사용하자 

```react
function tryConvert(temperature, convert) {
  const input = parseFloat(temperature);
  if (Number.isNaN(input)) {
    return '';
  }
  const output = convert(input);
  const rounded = Math.round(output * 1000) / 1000;
  return rounded.toString();
}
```

- 위 함수는 올바르지 않은 `temperature` 값에 대해 빈 문자열 반환한다. 올바른 경우엔 반올림하여 출력

### State 끌어올리기

현재는 두 `TemperatureInput` 컴포넌트가 각각의 입력값을 각자의 state 에 독립적으로 저장하고 있다.

이제, `TemperatureInput` 이 개별적으로 가지고 있던 local state 를 `Calculator` 로 끌어올리자

`Calculator` 가 공유될 state 를 지니고 있으면 이는 두 컴포넌트의 현재 온도에 대한 "source of truth" 가 된다. 

우선, `TemperatureInput` 에서 `this.state.temperature` 를 `this.props.temperature` 로 대체 

```react
  render() {
    // Before: const temperature = this.state.temperature;
    const temperature = this.props.temperature;
    // ...
```

- `temperature` 는 이제 prop, 즉 읽기 전용이므로, `TemperatureInput` 이 제어하지 못한다. 
- 이 경우, React 에서는 컴포넌트를 "제어" 가능하게 만들 수 있는데, 
  - `Calculator` 가 prop 으로 `temperature` 와 더불어, `onTemperatureChange` 를 건네줄 수 있다. 
  - 이는 DOM `<input>` 이 `value` 와 `onChange` prop 을 건네받는 것과 비슷한 방식이다. 

```react
  handleChange(e) {
    // Before: this.setState({temperature: e.target.value});
    this.props.onTemperatureChange(e.target.value);
    // ...
```

- `Temperature` 에서 온도를 갱신하고 싶으면, `this.props.onTemperatureChange` 를 호출하면 된다. 

`Caculator` 가 `onTemperatureChange` 를 이용해 자신의 지역 state 를 수정해서 변경사항을 처리하면, 변경된 새 값을 받은 두 입력 필드가 모두 리렌더링 된다.

변경된 `TemperatureInput` 최종

```react
class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.props.onTemperatureChange(e.target.value);
  }

  render() {
    const temperature = this.props.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature}
               onChange={this.handleChange} />
      </fieldset>
    );
  }
}
```

`Calculator` 는 다음과 같다.

```react
class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.handleCelsiusChange = this.handleCelsiusChange.bind(this);
    this.handleFahrenheitChange = this.handleFahrenheitChange.bind(this);
    this.state = {temperature: '', scale: 'c'};
  }

  handleCelsiusChange(temperature) {
    this.setState({scale: 'c', temperature});
  }

  handleFahrenheitChange(temperature) {
    this.setState({scale: 'f', temperature});
  }

  render() {
    const scale = this.state.scale;
    const temperature = this.state.temperature;
    const celsius = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
      <div>
        <TemperatureInput
          scale="c"
          temperature={celsius}
          onTemperatureChange={this.handleCelsiusChange} />
        <TemperatureInput
          scale="f"
          temperature={fahrenheit}
          onTemperatureChange={this.handleFahrenheitChange} />
        <BoilingVerdict
          celsius={parseFloat(celsius)} />
      </div>
    );
  }
}
```

### 정리

1. 입력값이 변경되면!
2. React 는 DOM `<input>` 의 `onChange` 에 지정된 함수를 호출함. (`TemperatureInput` 의 `handleChange` 메서드)
3. `handleChange` 메서드는 새로 입력된 값과 함께 `this.props.onTemperatureChange()` 를 호출 
3. 렌더링 단계에서, `Calculator`  는 `TemperatureInput` 의 `onTemperatureChange` 를 `handleCelciusChange` 와 `handleFahrenheitChange` 메서드로 지정해놓았으므로, 둘 중 하나가 호출된다. 
3. 이 두 메서드는 내부적으로 현재 수정한 입력 필드와 함께 `this.setState()` 를 호출하여 React 에게 자신을 다시 렌더링 하도록 요청
3. React 는 UI 가 어떻게 보여야 하는지 알아내기 위해 `Calculator` 컴포넌트의 `render` 메서드를 호출. 이 때 두 입력 필드의 value 는 현재 온도의 단위를 기반으로 재계산됨
3. React 는 `Calculator` 가 전달한 새 props 온도와 함께 `TemperatureInput` 의 `render` 메서드를 호출
3. React 는 `BoilingVerdict` 에게도 props 를 건네면서 컴포넌트의 `render` 메서드를 호출 

### 교훈

React 내에서는, 변경이 일어나는 데이터에 대해서는 "single source of truth" 를 유지해야 한다. 

보통 state 는 렌더링에 그 값을 필요로 하는 컴포넌트에 먼저 추가되는데, 그 후에 다른 컴포넌트도 그 값이 필요하게 되면 공통 조상으로 끌어올려야 한다. 다른 컴포넌트 간에 존재하는 state 를 동기화하려고 노력하는 대신 하향식 데이터 흐름을 유지하는 것을 추천!!
