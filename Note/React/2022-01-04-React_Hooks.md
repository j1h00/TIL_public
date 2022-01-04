# TIL : React Hook

참고 

- [useState() 와 useEffect() 로 상탯값과 생명주기 사용하기](https://velog.io/@kwonh/ReactHook-useState-%EC%99%80-useEffect-%EB%A1%9C-%EC%83%81%ED%83%AF%EA%B0%92%EA%B3%BC-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
- https://ko.reactjs.org/docs/hooks-intro.html

## Hook 개요 

Hook 을 이용하여 기존 Class 바탕의 코드를 작성할 필요 없이, 상태 값(state) 과 여러 React 기능을 사용할 수 있다. 

Hook 을 사용하는 이유!

> [Motivation](https://ko.reactjs.org/docs/hooks-intro.html#motivation)
>
> - 컴포넌트 사이에서 상태 로직을 재사용하기 어렵습니다.
> - 복잡한 컴포넌트들은 이해하기 어렵습니다.
>   - 고차컴포넌트, 렌더속성값 패턴은 리액트 요소 트리를 깊게만든다. 따라서 성능에 부정적인영향과 개발 시 디버깅이 힘들어지는 문제점이 발생한다.
> - Class은 사람과 기계를 혼동시킵니다.
>   - JS의 클래스문법, this 에 대한 이해가 필요해, React의 진입장벽을 높힌다.

## State Hook 

#### `useState` 

- 기본구조 : `const [state, setState] = useState(initialState);`

```react
import React, { useState } from 'react';

function Example() {
  // "count"라는 새 상태 변수를 선언합니다
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

- `useState` 는 현재의 `state` 값과 이 값을 업데이트 하는 함수를 쌍으로 제공한다. 
- 이는 class 의 `this.setState` 와 거의 유사하지만, 이전 state 와 새로운 state 를 합치지 않는다는 차이점이 있다. 
  - 함수형 컴포넌트는 이전 상탯값을 지우므로,  Spread Syntax 를 이용해 명시적으로 `...state` 를 사용해 펼쳐 넣어줘야 한다. 

다음과 같이 여러 state 변수 선언도 가능하다. 

```react
function ExampleWithManyStates() {
  // 상태 변수를 여러 개 선언했습니다!
  const [age, setAge] = useState(42);
  const [fruit, setFruit] = useState('banana');
  const [todos, setTodos] = useState([{ text: 'Learn Hooks' }]);
  // ...
}
```

****

#### `useEffect(fn)`

명령형 함수, 타이머, 로깅, 변형, side effects 등을 발생시키고 싶을 때 사용한다. 

- side effect : React 컴포넌트 안에서 데이터를 가져오거나 구독하고, DOM 을 직접 조작하는 작업. 이는 다른 컴포넌트에 영향을 줄 수도 있고, 렌더링 과정에서는 구현할 수 없는 작업이다.

- React class 의 `componentDidMount`, `componentDidUpdate` 와 같은 목적으로 제공되지만, 하나의 API 로 통합되었다. 

`useEffect` 로 전달된 함수는 레이아웃 배치, 화면 그리기를 완료한 후 발생한다. 

```react
import React, { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  // componentDidMount, componentDidUpdate와 비슷합니다
  useEffect(() => {
    // 브라우저 API를 이용해 문서의 타이틀을 업데이트합니다
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

- React 가 DOM 을 업데이트 한 뒤에, effect 함수를 실행하여  문서의 타이틀을 바꾼다. 
- 기본적으로 React 는 매 렌더링 이후에 effects 를 실행한다. 

아래와 같이 clean-up 이 필요한 effect 의 경우엔? (주로 이벤트 처리의 경우가 등록과 해제 필수)

effect 가 clean-up 을 위한 함수를 리턴하면, React 는 그 함수를 정리해야할 때에 이를 실행할 것!

```react
import React, { useState, useEffect } from 'react';

function FriendStatus(props) {
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }
    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    // effect 이후에 어떻게 정리(clean-up)할 것인지 표시합니다.
    return function cleanup() {
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  });

  if (isOnline === null) {
    return 'Loading...';
  }
  return isOnline ? 'Online' : 'Offline';
}
```

- 이를 통해 subscription 의 추가와 제거를 위한 로직을 가까이 묶어둘 수 있다. 
- 관심사를 분리하려고 한다면 단순히 multiple effect 를 사용하면 된다!

`useEffect()` 는 두 번째 인자로 의존성 배열을 가진다. 

```react
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]); // count가 바뀔 때만 effect를 재실행합니다.
```

- 컴포넌트가 리렌더링된 후에도 count 의 값에 변화가 없으면, React 는 effect 를 건너뛴다. 

