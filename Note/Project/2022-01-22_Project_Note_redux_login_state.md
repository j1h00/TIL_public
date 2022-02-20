# Project Note : 로그인 상태 관리 

### 로그인 상태 관리 

로그인한 유저의 정보를 redux state 로 관리하기 위해서 redux 를 사용하고자 했다. 

각각의 페이지에 새로 접근할 때마다, 로그인 여부를 확인하기 위해 

- local storage 의 jwt 를 확인하고, 유저 정보를 요청하여 받아온다. 
- redux store 에 유저 정보를 저장하고 관리한다. 

둘 중 어떤게 더 좋은지는 잘 모르겠다.. => 추후에 찾아보자!



일단 redux store 에 `isLoggedIn` 과 `userInfo` 를  state 로 선언하고, 로그인과 로그아웃 시에 이를 변경했다. 

각각의 페이지에 접근할 때는, `react-redux` 에서 제공하는 hook 인 `useSelector` API 를 이용하여 `isLoggedIn` 에 접근하여 로그인 여부를 받아왔다.   

ex) `index.js`

```react
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Main from "../components/Main";
import MainOnLogin from "../components/MainOnLogin";

function Home() {
  const { isLoggedIn } = useSelector((state) => state.isLoggedIn);

  useEffect(() => {
    console.log("Home useEffect", isLoggedIn);
  }, [isLoggedIn]);

  return <div>{!isLoggedIn ? <Main /> : <MainOnLogin />}</div>;
}

export default Home;
```

### 로그인 상태 관리 2

기존의 코드가 잘못 작성된 점을 발견했다. 

redux store 는 페이지가 로드 될 때마다 새로 생성된다. 기존 코드에선 store 의 `initialState` 를 localstorage 에서 받아오는 방식으로 작성했는데, 아래 코드에서 `initialState` 의 `isLoggedIn` 가 계속 `true` 인 것을 확인했다.. 

```react
const getTokenToLocalStorange = async (token) => {
  if (typeof window !== "undefined") {
    const token = await window.localStorage.getItem("jwt");
    return token;
  }
};

const isLoggedIn = getTokenToLocalStorange() ? true : false;

export const initialState = { isLoggedIn: isLoggedIn, userInfo: {} };
```

- 기존 코드는 위와 같았는데, 제대로 작동하지 않아 `isLoggedIn` 이 항상 `true` 였다. 

디버깅을 해볼까 하다가, reload 시에도 손쉽게 redux store 의 상태를 유지하도록 도와주는 라이브러리인 `redux-persist` 를 사용해보기로 했다. => vuex 의 플러그인이었던 persistedState 와 같은 역할을 하는 것으로 보인다. 

>[Redux-persist + Next Redux Wrapper 사용하기](https://velog.io/@nahsooyeon/Redux-persist-Next-Redux-Wrapper-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
>
>[next-redux-wrapper 공식문서](https://github.com/kirill-konshin/next-redux-wrapper#usage-with-redux-persist)

위 두 글을 참고 

```bash
npm install redux-persist
```

`redux-persist` 의 `persistReducer` 로 rootReducer 와 별개로 reducer 를 따로 하나 더 생성한다. 

```react
// store/modules/index.js
import storage from "redux-persist/lib/storage";
import { persistReducer } from "redux-persist";

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);
```

이를 이용하여 server-side 일 때와 client-side 일 때의 경우를 구분하여 store 를 생성한다. 

```react
import { configureStore } from "@reduxjs/toolkit";
import { createWrapper } from "next-redux-wrapper";
import { persistStore } from "redux-persist";
import logger from "redux-logger";
import { rootReducer, persistedReducer } from "./modules";

const makeConfiguredStore = (reducer) =>
  configureStore({
    reducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
    devTools: process.env.NODE_ENV !== "production",
  });

const makeStore = () => {
  const isServer = typeof window === "undefined";

  if (isServer) {
    return makeConfiguredStore(rootReducer);
  } else {
    const store = makeConfiguredStore(persistedReducer);
    store.__persistor = persistStore(store); // Nasty hack
    return store;
  }
};

export const wrapper = createWrapper(makeStore, {
  debug: process.env.NODE_ENV !== "production",
});
```

- `isServer` 가 false 인 경우 client side !! 

마지막으로 `_app.js` 를 `PersistGate` 로 감싼다. 

```react
import { wrapper } from "../store";
import { useStore } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";

function MyApp({ Component, pageProps }) {
  const store = useStore();
  return (
    <PersistGate persistor={store.__persistor} loading={<div>Loading</div>}>
      <Component {...pageProps} />
    </PersistGate>
  );
}

export default wrapper.withRedux(MyApp);
```

- `useStore` hook 사용! 

  
