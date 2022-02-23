# TIL : React Practice with NC 04

[초보자를 위한 리덕스 101](https://nomadcoders.co/redux-for-beginners/) 를 보고 React 를 복습하고 정리한 내용입니다.  

## Pure Redux

### Vanilla Todo 

```js
// index.js
import { createStore } from "redux";

const form = document.querySelector("form");
const input = document.querySelector("input");
const ul = document.querySelector("ul");

const ADD_TODO = "ADD_TODO";
const DELETE_TODO = "DELETE_TODO";

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [];
    case DELETE_TODO:
      return [];
    default:
      return state;
  }
};

const store = createStore(reducer);

const onSubmit = (e) => {
  e.preventDefault();
  const toDo = input.value;
  input.value = "";
  store.dispatch({ type: ADD_TODO, text: toDo });
};

form.addEventListner("submit", onSubmit);
```

### state mutation 

https://redux.js.org/understanding/thinking-in-redux/three-principles

**NEVER MUTATE STATE !!!**

return new state 

### Add & Delete Todo 

```js
import { createStore } from "redux";

const form = document.querySelector("form");
const input = document.querySelector("input");
const ul = document.querySelector("ul");

const ADD_TODO = "ADD_TODO";
const DELETE_TODO = "DELETE_TODO";

const addToDo = (text) => {
  return {
    type: ADD_TODO,
    text,
  };
};

const deleteToDo = (id) => {
  return {
    type: DELETE_TODO,
    id,
  };
};

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [{ text: action.text, id: Date.now() }, ...state];
    case DELETE_TODO:
      return state.filter(toDo => toDo.id !== action.id);
    default:
      return state;
  }
};

const store = createStore(reducer);

store.subscribe(() => console.log(store.getState()));

const dispatchAddToDo = (text) => {
  store.dispatch(addToDo(text));
};

const dispatchDeleteToDo = () => {
  // console.log(e.target.parentNode.id);
  const id = parseInt(e.target.parentNode.id);
  store.dispatch(deleteToDo(id));
};

const paintToDos = () => {
  const toDos = store.getState();
  ul.innerHTML = "";
  toDos.forEach((toDo) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.innerText = "DEL";
    btn.addEventListener("click", dispatchDeleteToDo);
    li.id = toDo.id;
    li.innerText = toDo.text;
    li.appendChild(btn);
    ul.appendChild(li);
  });
};

store.subscribe(paintToDos);

const onSubmit = (e) => {
  e.preventDefault();
  const toDo = input.value;
  input.value = "";
  dispatchAddToDo(toDo);
};

form.addEventListner("submit", onSubmit);
```

- `array.splice()` 는 state 를 mutate 한다!
  - `array.filter()` 를 사용하자 !

## React Redux

### setup

App.js

```react
import React from "react";
import { HashRouter as Router, Route } from "react-router-dom";
import Detail from "../routes/Detail";
import Home from "../routes/Home";

function App() {
  return (
    <Router>
      <Route path="/" exact component={Home}></Route>
      <Route path="/:id" component={Detail}></Route>
    </Router>
  );
}

export default App;
```

Home.js

```react
import React from "react";

function Home() {
  const [text, setText] = useState("");
  function onChange(e) {
    setText(e.terget.value);
  }
  function onSubmit(e) {
    e.preventDefault();
    setText("");
  }
  return (
    <>
      <h1>To Do</h1>
      <form onSubmit={}>
        <input type="text" value={text} />
        <button>Add</button>
      </form>
      <ul></ul>
    </>
  );
}

export default () => "Home";
```

### Connecting the store

index.js

```react
import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import { Provider } from "react-redux";
import store from "./store";


ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);
```

### mapStateToProps 

Home.js

```react
function Home({ toDos }) {
	// ...
}

//mapStateToProps
function getCurrentState(state) {
  return { toDos: state }
}

export default connect(getCurrentState)(Home);
```

- `connect(mapStateToProps)(Component_name)`
  - 이를 통해, redux store 의 state 를 Home 컴포넌트에 props 로 전달하는 것이 가능함! 

### mapDispatchToProps 
