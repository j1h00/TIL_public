# TIL : React Practice with NC 03

[ReactJS로 영화 웹 서비스 만들기](https://nomadcoders.co/react-for-beginners) 를 보고 React 를 복습하고 정리한 내용입니다.  

## 6.0 Effects Introduction 

```jsx
function App() {
  const [counter, setValue] = useState(0);
  const onClick = () => setValue((prev) => prev + 1);
  console.log("render")
  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}
```

- 위 코드의 경우, onClick 이벤트가 발생하여 state 가 업데이트 될 때마다, console 에 render 가 출력된다. 
  - 다시 말해, App function 이 재실행된다. 

```jsx
function App() {
  const [counter, setValue] = useState(0);
  const onClick = () => setValue((prev) => prev + 1);
  console.log("run all the time");
  const iRunOnlyOnce = () => {
    console.log("run only once");
  };
  useEffect(iRunOnlyOnce, []);
  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}
```

- `useEffect()` 를 위와 같이 사용시, 첫번째 렌더 시에만 `iRunOnlyOnce()` 를 실행한다. 

[Hook 정리](./2022-01-04-React_Hooks.md) 를 확인할 것!

```jsx
function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");

  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  console.log("run all the time");

  useEffect(() => {
    console.log("run only once");
  }, []);
  
  useEffect(() => {
    if (keyword !== "" && keyword.length > 2) {
      console.log("KEYWORD CHANGES: ", keyword);
    }
  }, [keyword]);

  useEffect(() => {
    console.log("COUNTER CHANGES");
  }, [counter]);

  useEffect(() => {
    console.log("KEYWORD & COUNTER CHANGES");
  }, [keyword, counter]);

  return (
    <div>
      <input onChange={onChange} type="text" placeholder="Search here..." />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}
```

- `useEffect()` 의 second parameter 를 통해, dependency 를 결정할 수 있다. 

Clean-up function  

```jsx
```

