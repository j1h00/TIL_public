# TIL : React Practice with NC 01

[ReactJS로 영화 웹 서비스 만들기](https://nomadcoders.co/react-for-beginners) 를 보고 React 를 복습하고 정리한 내용입니다.  

## 10.4 Protection with PropTypes

```bash
npm install prop-types
```

```jsx
import PropTypes from "prop-types";
```

proto-types 를 통해 props naming 을 관리할 수 있다. 

## 11.1 All you need to know about State

1. state 를 직접 변경하지 말자!
2. state 값 변경 시에, 이전 state 값 혹은 다른 state 값에 의존하는 것은 좋지 않다. 
3. `setState()` 를 사용하자! => state 변경될 때마다 update 가 가능함. 

```jsx
import React from "react";
import PropTypes from "prop-types";

class App extends React.Component {
  state = {
    count: 0
  };
  add = () => {
    this.setState(current => ({ count: current.count + 1}));
  };
  minus = () => {
    this.setState(current => ({ count: current.count - 1}));
  };
  render() {
    return (
      <div>
        <h1>The number is: {this.state.count}</h1>
        <button onClick={this.add}>Add</button>
        <button onClick={this.minus}>Minus</button>
      </div>
    );
  }
}

export default App;
```

## Movie-app

강의를 하나하나 보기 귀찮으므로, 실습을 통해 모르는 부분을 살펴보자.

server API 로 이미 만들어 둔 django API 를 사용해봐도 재미있을 듯!

### 11.3 Planning the Movie Component

```jsx
import './App.css';
import { React } from 'react';

class App extends React.Component {
  state = {
    isLoading: true,
    moives: []
  };

  componentDidMount() {
    setTimeout(() => {
      this.setState({ isLoading: false });
    }, 6000);
  }
  render() {
    const { isLoading } = this.state;
    return <div>{isLoading ? "Loading..." : "We are ready"}</div>;
  }
}

export default App;
```

- `setTimeout()` 을 이용하여, 첫 랜딩 페이지에 로딩 시간을 부여하고, 
- 로딩 되는 동안 axios 를 통해 movie 정보를 가져와서 state 에 저장하자!

### 12.0 Fetching Movies from API

```bash
npm install axios
```

[yts movie API](https://yts.mx/api) 를 사용해보자! 

List Movie API url => https://yts.mx/api/v2/list_movies.json

위 url 은 계속해서 바뀌므로, Nomad Coder 의 yts-proxy API 를 대신 사용하자 

https://yts-proxy.now.sh/list_movies.json

```jsx
import axios from 'axios';
// ... 
  getMovies = async () => {
    const {
      data: {
        data: { 
          movies }
        }
      } = await axios.get("https://yts-proxy.now.sh/list_movies.json?sort_by=rating");
    this.setState({ movies, isLoading: false });
  }
  componentDidMount() {
    this.getMovies();
  }
```

- axios 를 통해 movies data 를 가져온다. 
- async await 로 `getMovies()` 를 동기적으로!

### 12.1 Rendering the Movies

`Movie` 컴포넌트 생성

```jsx
import React from 'react';
import PropTypes from 'prop-types';

function Movie({ id, year, title, summary, poster}) {
    return <h4>{title}</h4>
}

Movie.propTypes = {
    id: PropTypes.number.isRequired,
    year: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    summary: PropTypes.string.isRequired,
    poster: PropTypes.string.isRequired,  
};

export default Movie;
```

- prop-types 로 prop 으로 받을 인자를 지정한다.

`App` 에서 `<Movie>` 렌더링!

```jsx
  render() {
    const { isLoading, movies } = this.state;
    return <div>{isLoading ? "Loading..." : movies.map(movie => {
      return (
        <Movie 
          id={movie.id} 
          year={movie.year} 
          title={movie.title} 
          summary={movie.summary} 
          poster={movie.medium_cover_image}
        />
      );
    })}</div>;
  }
```

- 삼항연산자를 이용하여, isLoading 이 false 인 경우(`getMovies()` 에서 await 가 완료된 경우) 에만 Movie 를 렌더링 한다.  





