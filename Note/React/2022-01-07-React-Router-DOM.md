# TIL : React Router DOM 

Vue 에서는 vue-router 를 이용해 rounting 을 해결했다. 

React 에서는, 자주 사용하는 두 가지 해결책이 있는 것으로 보인다.

1. React Router DOM
2. Next.js

오늘은 React Router DOM 를 통해 react routing 에 대해 간단히 정리하고, 그 후에 Next.js 활용법을 익히는 것이 좋겠다.   

## skeleton code

[생활코딩 React Router 영상](https://youtu.be/WLdbsl9UwDc) 참고 

다음과 같은 예시 코드가 있는 경우 

```react
function Topics() {
  return (
    <div>
      <h2>Topics</h2>
      Topics...  
    </div>
  )
}

function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact...  
    </div>
  )
}

function App() {
  return (
    <div>
      <h1>React Router DOM example</h1>
      <Home></Home>
      <Topics></Topics>
      <Contact></Contact>
    </div>
  )
}


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

- routing 을 통해  `Home`, `Topics`, `Contact` 컴포넌트 각각을 렌더링 하는 페이지로 이동가능 하도록 해보자.

## Install 

https://v5.reactrouter.com/web/guides/quick-start

```bash
yarn add react-router-dom
```

## Primary Components

**BrowserRouter**

```react
import {BrowserRouter} from 'react-router-dom'
// .... 
ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

- react-router 도움을 적용하고 싶은 컴포넌트의 최상위 컴포넌트를 감싸주는 Wrapper Component 

**Route**

```react
import {Route} from 'react-router-dom'
// ... 
function App() {
  return (
    <div>
      <h1>React Router DOM example</h1>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/topics">Topics</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
      <Route path="/"><Home></Home></Route>
      <Route path="/topics"><Topics></Topics></Route>
      <Route path="/contact"><Contact></Contact></Route>
    </div>
  )
}
```

- `<Route>` 로 감싼 뒤, `path` 지정.
- 그러나, `/topics` 혹은 `/contact` url 로 접근 시, `Home` 컴포넌트도 같이 렌더링 됨. 
  - `/` 가 포함되어 있으므로.. 이와 일치하는 모든 컴포넌트가 렌더링된다. 
  - 이 때, `<Route>` API 중 `exact` 를 사용하면 해결! https://v5.reactrouter.com/web/api/Route/exact-bool 

```react
function App() {
	// ... 
      <Route exact path="/"><Home></Home></Route>
	// ... 
}
```

**Switch**

```react
import {Switch} from 'react-router-dom'

function App() {
    // ... 
      <Switch>
        <Route path="/topics"><Topics></Topics></Route>
        <Route path="/contact"><Contact></Contact></Route>
        <Route path="/"><Home></Home></Route>
      </Switch>
    // ... 
}
```

- path 와 일치하는 첫번째 컴포넌트만 렌더링한다!

이를 이용하면, not found 페이지 설정이 간단하다 

```react
function App() {
    // ... 
      <Switch>
        <Route exact path="/"><Home></Home></Route>
        <Route path="/topics"><Topics></Topics></Route>
        <Route path="/contact"><Contact></Contact></Route>
        <Route path="/">Not Found</Route>
      </Switch>
    // ... 
}
```

**Link**

지금은 `<a>` 클릭 시 페이지가 reload 된다. `Link` 를 이용하면 SPA 구현이 매우 간단하다. 

```react
import {Link} from 'react-router-dom'

function App() {
    // ... 
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/topics">Topics</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
    // ... 
}
```

- Vue 의 `<router-link :to"{ name: 'Home' }">Home</router-link>` 와 동일한 기능을 한다. 

**HashRouter**

`BrowserRouter` => `HashRouter`

```react
import {HashRouter} from 'react-router-dom'

ReactDOM.render(
  <React.StrictMode>
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

- url path 에 `#` 이 추가된다. 

  - http://localhost:3000/#/topics
  - 웹서버 입장에서는 무시되는 url 이지만, 리액트 라우터 돔이 이 정보를 가져와서 이에 해당되는 컴포넌트를 라우팅 해준다. 

  > https://yung-developer.tistory.com/106
  >
  > Browser Router를 별도의 서버 설정 없이 사용하면 새로고침이나 올바르지 않은 URL 접근을 리디렉션 할 때 404 에러가 발생한다.
  >
  > Hash Router를 사용하면 # 뒤에 path가 오기 때문에 새로고침과 리디렉션을 해도 모두 올바른 entry point로 요청이 갈 수 있게 된다.

**NavLink**

https://v5.reactrouter.com/web/guides/primary-components/navigation-or-route-changers

`<Link>` => `<NavLink>` 

```react
import {NavLink} from 'react-router-dom'

function App() {
    // ... 
      <ul>
        <li><NavLink exact to="/">Home</NavLink></li>
        <li><NavLink to="/topics">Topics</NavLink></li>
        <li><NavLink to="/contact">Contact</NavLink></li>
      </ul>
    // ... 
}
```

- `class="active"` 추가가 가능하다. 
  - `active` 컴포넌트에 원하는 CSS 처리가 간단하다. 
  - 마찬가지로 `exact` 사용이 가능하다. 

**Parameter**

`<Topics>` 내에 컴포넌트를 추가해보자. 

```react
function Topics() {
  return (
    <div>
      <h2>Topics</h2>
      <ul>
        <li><NavLink to="/topics/1">HTML</NavLink></li>
        <li><NavLink to="/topics/2">JS</NavLink></li>
        <li><NavLink to="/topics/3">React</NavLink></li>
      </ul>
      <Switch>
        <Route path="/topics/1">
          HTML is ... 
        </Route>
        <Route path="/topics/2">
          JS is ... 
        </Route>
        <Route path="/topics/3">
          React is ... 
        </Route>
      </Switch>
    </div>
  )
}
```

- `<Topic>` 컴포넌트 내에 또 Route 가 존재하는 nested Route 구조를 가진다. 
- 만약 3개 이상으로 많은 경우 수동으로 작성하기 어렵다. 

동적 라우팅과 `useParams` Hook 을 이용해보자 

1. 먼저 `Topics` 컴포넌트를 아래와 같이 변경

```react
var contents = [
  {id:1, title:'HTML', description:'HTML is ...'},
  {id:2, title:'JS', description:'JS is ...'},
  {id:3, title:'React', description:'React is ...'},
]

function Topics() {
  var lis = [];
  for(var i = 0; i < context.lengthl; i++){
    lis.push(<li><NavLink to={'/topics/' + contents[i].id}>{context[i].title}</NavLink></li>)
  }
  return (
    <div>
      <h2>Topics</h2>
      <ul>
        {lis}
      </ul>
      <Route path="/topics/:topic_id">
        <Topic></Topic>
      </Route>
    </div>
  )
}
```

- `<NavLink>` 를 for 문을 이용하여 동적으로 생성하고, 
  - path 에 `:topic_id` 를 작성하면, url 에서 `topic_id` 를 parameter 로 받아 사용 가능하다. 
  - 그렇다면 현재 `topic_id` 에 해당되는 `<Topic>` 을 어떻게 렌더링하는가?

2. 아래와 같이 `Topic` 컴포넌트 작성

```react
function Topic() {
  var params = useParams(); // {topid_id: "1"}
  var topic_id = params.topic_id;
  var selected_topic = {
    title: 'Sorry',
    description: 'Not Found'
  }
  for(var i = 0; i < contents.length; i++) {
    if(contents[i].id === Number(topic_id)) {
      selected_topic = contents[i];
    }
  }

  return (
    <div>
      <h3>{selected_topic.title}</h3>
      {selected_topic.description}
    </div>
  )
}
```

- `userParams()` Hook 을 사용하여, 현재 url 에서 해당되는 parameter 를 가져올 수 있다. 

## 추가 공부할 요소들

**Server Side Rendering**

- https://v5.reactrouter.com/web/guides/server-rendering

**Code Splitting**

- 컴포넌트 구조가 복잡해지고, 용량이 커지는 경우 
- 컴포넌트를 적당히 쪼개서 필요할 때마다 로드 가능하다면 성능도 좋아지고, 서버 통신 데이터도 줄어 돈도 절약된다. 

최근 널리 사용되는 Next.js 를 통해 공부해두는 것이 좋겠다.

## 끝!

