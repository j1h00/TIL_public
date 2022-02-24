# TIL : React Practice with NC 05

노마드코더의 [실전형 React Hooks 10개 ](https://nomadcoders.co/react-hooks-introduction) 를 보고 정리한 내용입니다.  

자주 사용되는 React Hook 을 작성하고, npm package publish 에 도전해보자!

create-react-app 으로 프로젝트를 생성하는 대신에, [CodeSandBox](https://codesandbox.io/) 를 이용하여 작성. 

## #1.0 introduction to useState

```react
class AppUgly extends React.Component {
  state = {
    item: 1
  };

  render() {
    const { item } = this.state;
    return (
      <div className="App">
        <h1>Hello {item}</h1>
        <h2>Start editing to see some magic happen!</h2>
        <button onClick={this.incrementItem}>Increment</button>
        <button onClick={this.decrementItem}>decrement</button>
      </div>
    );
  }

  incrementItem = () => {
    this.setState((state) => {
      return {
        item: state.item + 1
      };
    });
  };

  incrementItem = () => {
    this.setState((state) => {
      return {
        item: state.item - 1
      };
    });
  };
}
```

```react
export default function App() {
  const [item, setItem] = useState(1);

  const incrementItem = () => setItem(item + 1);
  const decrementItem = () => setItem(item - 1);

  return (
    <div className="App">
      <h1>Hello {item}</h1>
      <h2>Start editing to see some magic happen!</h2>
      <button onClick={incrementItem}>Increment</button>
      <button onClick={decrementItem}>decrement</button>
    </div>
  );
}
```

- class component 로 작성하는 것 보다 코드량도 줄고 쉽고 간편하다!

## #1.1 useInput part one

```react
const useInput = (initialValue) => {
  const [value, setValue] = useState(initialValue);
  const onChange = (event) => {
    const {
        target: {value}
    } = event;
    setValue(value);
  };
  return { value };
};

export default function App() {
  const name = useInput("Mr.");
  return (
    <div className="App">
      <h1>Hello </h1>
      {/* <input placeholder="Name" value={name.value} onChange={name.onChange} /> */}
      <input placeholder="Name" {...name} />
    </div>
  );
}
```

- App component 와 완전히 분리된 useInput 함수에서 이벤트를 처리하는 것이 가능하다.  

## #1.2 useInput part two

```react
import { useState } from "react";

const useInput = (initialValue, validator) => {
  const [value, setValue] = useState(initialValue);
  const onChange = (event) => {
    const {
      target: { value }
    } = event;
    let willUpdate = true;
    if (typeof validator === "function") {
      willUpdate = validator(value);
    }
    if (willUpdate) {
      setValue(value);
    }
  };
  return { value, onChange };
};

export default function App() {
  const restrict = (value) => !value.includes("@");
  const maxLen = (value) => value.length() <= 10;
  const name = useInput("Mr.", maxLen);
  return (
    <div className="App">
      <h1>Hello </h1>
      {/* <input placeholder="Name" value={name.value} onChange={name.onChange} /> */}
      <input placeholder="Name" {...name} />
    </div>
  );
}

```

- validator 함수가 false 를 return 하는 경우엔, `willUpdate` 가 false 가 되어 `setValue` 가 동작하지 않는다. 



## #1.3 useTabs 

```react
import { useState } from "react";

const content = [
  {
    tab: "Section 1",
    content: "I'm the content of the Section 1",
  },
  {
    tab: "Section 2",
    content: "I'm the content of the Section 2",
  },
];

const useTabs = (initialTab, allTabs) => {
  const [currentIndex, setCurrentIndex] = useState(initialTab);
  if (!allTabs || !Array.isArray(allTabs)) {
    return;
  }
  return {
    currentItem: allTabs[currentIndex],
    changeItem: setCurrentIndex,
  };
};

export default function App() {
  const { currentItem, changeItem } = useTabs(0, content);
  return (
    <div className="App">
      <h1>Hello </h1>
      {content.map((section, index) => (
        <button onClick={() => changeItem(index)}>{section.tab}</button>
      ))}
      <div>{currentItem.content}</div>
    </div>
  );
}
```

- 버튼 클릭으로 currentItem 을 변경하여 Tab 을 변경한 것과 같은 효과를 준다.  



## #2.0 Introduction to useEffect

```react
import { useEffect, useState } from "react";

export default function App() {
  const sayHello = () => console.log("hello");
  const [number, setNumber] = useState(0);
  const [anumber, setANumber] = useState(0);
  // 1. 
  // useEffect(sayHello);
    
  // 2.   
  // useEffect(sayHello, [number]);
    
  // 3. 
  // useEffect(sayHello, []);
  return (
    <div className="App">
      <h1>Hello </h1>
      <button onClick={() => setNumber(number + 1)}>{number}</button>
      <button onClick={() => setANumber(anumber + 1)}>{anumber}</button>
    </div>
  );
}
```

- 위의 `1.` 에서 `sayHello()` 는 새로고침 시, 그리고 state 가 변경될 때 마다 실행된다. 
- 다시 말해 `useEffect` 는 `componentDidMount`, `componentDidUpdate` 의 역할을 모두 수행한다. 
- 첫번째 인자로 `function(effect)`, 두번째 인자로 `dependencies(deps)` 을 받는다. 

- `2.` 에서는 `anumber` 의 변경 시에는 `sayHello` 가 실행되지 않는다. 
- `3.` 에서는 `componentDidMount` 와 같은 기능을 한다. 
- 마지막으로, useEffect 는 함수를 리턴하는데, 이 때 `compontnwillUnmount` 와 같은 기능을 한다. 

## #2.1 useTitle 

```react
import { useEffect, useState } from "react";

const useTitle = (initialTitle) => {
  const [title, setTitle] = useState(initialTitle);

  const updateTitle = () => {
    const htmlTitle = document.querySelector("title");
    htmlTitle.innerText = title;
  };
  useEffect(updateTitle, [title]);
  return setTitle;
};

export default function App() {
  const titleUpdater = useTitle("Loading...");
  setTimeout(() => titleUpdater("Home"), 5000);
  return (
    <div className="App">
      <h1>Hello </h1>
    </div>
  );
}
```

- title 이 5초 후에 Home 으로 업데이트 된다. 

## #2.2 useClick

`useRef` 에 대해 알아보자!

```react
import { useRef } from "react";

export default function App() {
  const potato = useRef();
  setTimeout(() => potato.current.focus(), 5000);
  return (
    <div className="App">
      <h1>Hello </h1>
      <input ref={potato} placeholeder="la" />
    </div>
  );
}
```

- React component 의 특정 부분, html element 를 을 선택할 수 있다. 
- `getElementById()` 와 같다!

```react
import { useEffect, useRef } from "react";

const useClick = (onClick) => {
  const element = useRef();
  useEffect(() => {
    if (typeof onClick !== "function") {
      return;
    }
    if (element.current) {
      element.current.addEventListener("click", onClick);
    }
    return () => {
      if (element.current) {
        element.current.removeEventListener("click", onClick);
      }
    };
  }, []);
  return typeof onClick !== "function" ? element : undefined;
};

export default function App() {
  const sayHello = () => console.log("say hello");
  const title = useClick(sayHello);
  return (
    <div className="App">
      <h1 ref={title}>Hello </h1>
    </div>
  );
}
```

- useEffect  를 이용하여 title ref 에 eventListener 를 추가하자.  

## # 2.3 useConfirm & usePreventLeave 

useState, useEffect 없이 사용 가능한 유사 hook 을 만들어보자 

```react
const useConfirm = (message = "", onConfirm, onCancel) => {
  if (typeof onConfirm !== "function") {
    return;
  }
  // onCancle 은 필수 인자가 아니므로 다음과 같이 쓴다. 
  if (onCancel && typeof onCancel !== "function") {
    return;
  }

  const confirmAction = () => {
    if (window.confirm(message)) {
      onConfirm();
    } else {
      onCancel();
    }
  };
  return confirmAction;
};

export default function App() {
  const deleteWorld = () => console.log("Deleting the world");
  const abort = () => console.log("Aborted");
  const confirmDelete = useConfirm("Are you sure", deleteWorld, abort);

  return (
    <div className="App">
      <button onClick={confirmDelete}>Delete the world</button>
    </div>
  );
}
```

- window confirm 창의 confirm, cancel 선택 여부에 따라 각각 다른 동작을 할 수 있도록 해주는 hook 이다.

```react
const usePreventLeave = () => {
  const listener = (event) => {
    event.preventDefault();
    event.returnValue = "";
  };
  const enablePrevent = () => window.addEventListener("beforeunload", listener);
  const disablePrevent = () =>
    window.removeEventListener("beforeunload", listener);

  return { enablePrevent, disablePrevent };
};

export default function App() {
  const { enablePrevent, disablePrevent } = usePreventLeave();

  return (
    <div className="App">
      <button onClick={enablePrevent}>Protect</button>
      <button onClick={disablePrevent}>Unprotect</button>
    </div>
  );
}
```

- protect 버튼 클릭 시 `enablePrevent` 가 작동하여 이벤트 리스너를 등록한다. 
- `beforeunload`, 즉 창을 닫을 시에 `listener` 가 작동하여, "사이트에서 나가시겠습니까?" confirm 창이 나타난다. 

## #2.4 useBeforeLeave

```react
import { useEffect } from "react";

const useBeforeLeave = (onBefore) => {
  if (typeof onBefore !== "function") {
    return;
  }
  const handle = (event) => {
    const { clientY } = event;
    if (clientY <= 0) {
      onBefore();
    }
  };

  useEffect(() => {
    document.addEventListener("mouseleave", handle);
    return () => document.removeEventListener("mouseleave", handle);
  }, []);
};

export default function App() {
  const begForLife = () => console.log("Pls dont leave");
  useBeforeLeave(begForLife);
  return (
    <div className="App">
      <h1>Hello</h1>
    </div>
  );
}
```

- 사용자가 마우스를 위쪽으로 이동시켜 document 를 벗어나는 경우 발생한다. 
- 실용적인 hook 인지는 잘 모르겠다.. 

## #2.5 useFadeIn & useNetwork

```react
import { useEffect, useRef } from "react";

const useFadeIn = (duration = 1, delay = 0) => {
  if (typeof duration !== "number" || typeof delay !== "number") {
    return;
  }
  const element = useRef();
  useEffect(() => {
    if (element.current) {
      const { current } = element;
      current.style.transition = `opacity ${duration}s ease-in-out ${delay}s`;
      current.style.opacity = 1;
    }
  }, []);
  return { ref: element, style: { opacity: 0 } };
};

export default function App() {
  const fadeInH1 = useFadeIn(1, 2);
  const fadeInP = useFadeIn(2, 4);
  return (
    <div className="App">
      <h1 {...fadeInH1}>Hello</h1>
      <p {...fadeInP}> lorem ipsum lalalala</p>
    </div>
  );
}
```

- `useRef()` 로 등록된 h1, p tag element 의 fade in 효과를 지정할 수 있다. 

```react
 import { useEffect, useState } from "react";

const useNetwork = (onChange) => {
  const [status, setStatus] = useState(navigator.onLine);
  const handleChange = () => {
    if (typeof onChange === "function") {
      onChange(navigator.onLine);
    }
    setStatus(navigator.onLine);
  };
  useEffect(() => {
    window.addEventListener("online", handleChange);
    window.addEventListener("offline", handleChange);
    return () => {
      window.removeEventListener("online", handleChange);
      window.removeEventListener("offline", handleChange);
    };
  }, []);
  return status;
};

export default function App() {
  const handleNetworkChange = (onLine) => {
    console.log(onLine ? "We just went online" : "We are Online");
  };

  const onLine = useNetwork(handleNetworkChange);
  return (
    <div className="App">
      <h1>{onLine ? "Online" : "OffLine"}</h1>
    </div>
  );
}
```

- `navigator.onLine` 은 웹사이트 네트워크의 온라인, 오프라인 상태를 반환한다. 
- network 상태가 offline <==> online 으로 변경 될 때마다, `onLine` state 가 변경되고, `handleNetworkChange` 가 실행된다. 
