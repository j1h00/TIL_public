# TIL : React Practice with NC 02

[ReactJS로 영화 웹 서비스 만들기](https://nomadcoders.co/react-for-beginners) 를 보고 React 를 복습하고 정리한 내용입니다.  

## 7.0 To Do List part One

## 7.1 To Do List part Two

[Todo app Link](../../Toy-project/my-todo-app)

## 7.2 Coin Tracker 

[Coin Tracker app Link](../../Toy-project/my-coin-tracker)

## 7.3 Movie app part One (with Hook)

## 7.4 Movie app part Two(with Hook)

[Movie app Link](../../Toy-project/my-movie-app-hook)

## 7.5 React Router

```jsx
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./routes/Home";
import Detail from "./routes/Detail";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/movie/:id">
          <Detail />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}
```

- `:id` 로 parameter 전달 가능 

## 7.6 Parameters

```jsx
const { id } = useParams();
```

- `useParams()` 라는 간단한 API 로 url 의 parameter 를 전달받아 사용 가능하다. 

## 7.7 Publishing

```bash
npm i gh-pages
npm run build
```

```json
// package.json
// ...
	"scripts" : {
        // ...
        "deploy": "gh-pages -d build",
        "predeploy": "npm run build"
    }
	},
	"homepage": "https://username.github.io/repository_name"
}
```

```bash
npm run deploy
```

