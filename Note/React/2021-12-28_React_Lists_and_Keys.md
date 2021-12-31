# TIL : Lists and Keys

### 여러 개의 컴포넌트 렌더링하기

`map()` 함수를 이용해서, 배열을 엘리먼트 리스트로 만든다.

```react
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>
  <li>{number}</li>
);
```

`listItems` 배열을 `<ul>` 엘리먼트 안에 포함시켜 DOM 에 렌더링

```react
ReactDOM.render(
  <ul>{listItems}</ul>,
  document.getElementById('root')
);
```

### 기본 리스트 컴포넌트

일반적으로 컴포넌트 안에서 리스트를 렌더링한다. 

```react
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li>{number}</li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

- 위 코드를 실행하면, 리스트의 각 항목에 key 를 넣어야 한다는 경고가 표시된다. 
- "key" 는 엘리먼트 리스트를 만들 때 포함해야 하는 특수한 문자열 어트리뷰트이다.

```react
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li key={number.toString()}>
      {number}
    </li>
  );
  return (
    <ul>{listItems}</ul>
  );
}
```

### Key

Key 는 React 가 어떤 항목을 변경, 추가, 삭제할지 식별하는 것을 돕는다. key 는 배열 내부의 엘리먼트에 지정해야 한다. 

Key 는 해당 항목을 고유하게 식별할 수 있는 문자열이 좋다. 흔히 데이터의 ID 를 key 로 사용한다. 

```react
const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
);
```

혹은 최후의 수단으로 항목의 인덱스를 key 로 사용할 수 있다. 

```react
const todoItems = todos.map((todo, index) =>
  // Only do this if items have no stable IDs
  <li key={index}>
    {todo.text}
  </li>
);
```

- 항목의 순서가 바뀔 수 있는 경우 key 에 인덱스를 사용하는 것은 권장하지 않는다. 이로 인해 성능 저하 혹은 컴포넌트의 state 와 관련된 문제가 발생할 수 있다. 
- 명시적으로 key 를 지정하지 않는 경우 React 가 기본적으로 인덱스를 key 로 사용한다. 

### Key 로 컴포넌트 추출하기

Key 는 주변 배열의 context 에서만 의미가 있다. 

예를 들어, 아래에서는 `ListItem` 이라는 컴포넌트를 추출하였는데, 

이 경우엔 `<li>` 가 아니라 `<ListItem />` 엘리먼트가 key 를 가져야 한다. 

```react
function ListItem(props) {
  // 맞습니다! 여기에는 key를 지정할 필요가 없습니다.
  return <li>{props.value}</li>;
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // 맞습니다! 배열 안에 key를 지정해야 합니다.
    <ListItem key={number.toString()} value={number} />
  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}
```

- 보통 `map()` 함수 내부에 있는 엘리먼트에 key 를 넣어주면 맞다. 

### Key 는 형제 사이에서만 고유한 값이어야 한다. 

전체 범위에서 고유할 필요는 없다. 

React 에서 key 는 힌트를 제공할 뿐, 컴포넌트로 전달하지는 않는다. 컴포넌트에서 key 와 동일한 값이 필요한 경우엔 다른 이름의 prop 으로 전달한다. 

```react
const content = posts.map((post) =>
  <Post
    key={post.id}
    id={post.id}
    title={post.title} />
);
```

- 위의 경우 `POST` 컴포넌트는 `props.if` 는 읽을 수 있지만, `props.key` 는 읽지 못한다. 

### JSX 에 map() 포함시키기 

위 예시처럼 변도의 `listItems` 변수를 선언하고 이를 JSX 로 처리할 수도 있지만, 

중괄호 안에 모든 표현식을 포함하여 `map()` 함수의 결과를 인라인으로 처리할 수 있다. 

```react
function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) =>
        <ListItem key={number.toString()}
                  value={number} />
      )}
    </ul>
  );
}
```







