# Project Note : Next.js + redux

### install 

>[[Next.js] Next.js + redux toolkit 기본 세팅](https://cotak.tistory.com/164) => redux/toolkit (createSlice)
>
>[Next.js 의 서버사이드 렌더링에 Redux 적용하기](https://slog.website/post/14)
>
>https://andwinter.tistory.com/356

일반적으로 Next.js 에서 redux 를 사용하기 위해선 아래와 같은 세팅이 필요하다. 

```bash
npm i @reduxjs/toolkit 
npm i react-redux 
npm i next-redux-wrapper
npm i redux-logger --save-dev # 필요한 경우에 설치
```

- `@reduxjs/toolkit`: redux 사용을 편리하게 해주는 API를 포함 
- `next-redux-wrapper`: next 에서 redux store 를 사용할 수 있도록 해주는 Wrapper 

- `redux-logger`: redux state 변경 때마다 console 에서 변경사항 확인이 가능하다 => 매우 편리!

프로젝트 최상위에 다음과 같이 생성한다. 

- `/store`
  - `/modules`
    - `userInfo.js`
    - `index.js`
  - `index.js`

`userInfo.js` 에는 유저 정보에 접근하는 reducer 와 initialState 를 선언하고, 

```react
// modules/userInfo.js
const LOGIN = "LOGIN";
const LOGOUT = "LOGOUT";

const getTokenToLocalStorange = async (token) => {
  if (typeof window !== "undefined") {
    const token = await window.localStorage.getItem("jwt");
    return token;
  }
};

const isLoggedIn = getTokenToLocalStorange() ? true : false;

export const initialState = { isLoggedIn: isLoggedIn, userInfo: {} };

export default (state = initialState, action) => {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        isLoggedIn: true,
        userInfo: action.userInfo,
      };
    case LOGOUT:
      return {
        ...state,
        isLoggedIn: false,
        userInfo: {},
      };
    default:
      return state;
  }
};
```



`index.js` 에서 `combineReducer` 를 이용하여 rootReducer 를 선언했다. 또한 `next-redux-wrapper` 에서 제공하는 `HYDRATE` 를 action case 로 추가해주었다. `HYDRATE` 는 서버 사이드 데이터를 클라이언트 사이드 Store 에 통합해준다고 한다. 

```react
//modules/index.js
import { combineReducers } from "redux";
import { HYDRATE } from "next-redux-wrapper";

import userInfo from "./userInfo";

const reducer = (state, action) => {
  switch (action.type) {
    // // 서버 사이드 데이터를 클라이언트 사이드 Store에 통합.
    case HYDRATE:
      return { ...state, ...action.payload };
    default: {
      const combineReducer = combineReducers({
        userInfo,
      });
      return combineReducer(state, action);
    }
  }
};

export default reducer;
```



`store/index.js` 에선 `configureStore` 를 통해 redux store 를 선언한다. 이 때, reducer 와 `redux-logger` 에서 제공하는 `logger`를 미들웨어로 추가하고, store 를 `next-redux-wrapper` 의 `createWrapper` 로 감싼다. 

```react
// store/index.js
import { configureStore } from "@reduxjs/toolkit";
import { createWrapper } from "next-redux-wrapper";
import logger from "redux-logger";
import reducer from "./modules";

const makeStore = (context) =>
  configureStore({
    reducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
    devTools: process.env.NODE_ENV !== "production",
  });

export const wrapper = createWrapper(makeStore, {
  debug: process.env.NODE_ENV !== "production",
});
```



마지막으로 `_app.js` 에서 최상위 `App` 컴포넌트를 `wrapper` 와 연결해준다. 

```react
// pages/_app.js
export default wrapper.withRedux(MyApp);
```


