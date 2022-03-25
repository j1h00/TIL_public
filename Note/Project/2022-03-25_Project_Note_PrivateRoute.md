# Project Note : Private Route

서비스를 개발하던 중, 특정 페이지에는 비로그인 유저가 접근할 수 없도록 제한해야 하는 경우가 있었다. 

저번 프로젝트에선 다음과 같은 방법을 사용하였다.  [2022-02-04_Project_Note_login_redirection](./2022-02-04_Project_Note_login_redirection.md)

1. client side 

   - `useEffect` 내에서 로그인 여부를 판별하여 `router.push()`
   - 컴포넌트가 생성된 이후에 실행되기 때문에, 페이지가 노출되면서 깜빡이는 현상이 존재했다. 
   - 다시 말해 loading spinner 가 필요하다 

2.   server side

   - `getServerSideProps` 내에서 redirect 를 리턴한다. 

   ```js
       if (!isLoggedIn) {
         // toast.error("로그인이 필요합니다.");
         return {
           redirect: {
             destination: "/login",
             permanent: false,
           },
         };
       }
   ```

그러나 위의 경우엔 모두 접근 제한이 필요한 컴포넌트 내에서 같은 코드를 반복해서 작성해야 하므로 좋은 방법이 아니라고 판단했다. 따라서 모든 페이지에서 아래와 같이 공통적으로 로그인 여부를 판별하는 `<LoginWrapper />` 컴포넌트를 생성했다. 

맞는 방법인지는 몰랐으나, 일단 동작은 잘 수행했다. 

이번 React 프로젝트에선, 로그인 접근 제한에 대한 레퍼런스 글을 찾아보고 적용하였다. 

>[[React] react-router에서 인증 및 권한 Router(Private) 구현하기(권한별 routing)](https://kimchanjung.github.io/programming/2020/06/24/react-router-private-router/)

- 일반적으로 react-router 라이브러리 사용 시, 접근 제한이 필요한 페이지는 `<Route>` 대신 `PrivateRoute` 라는 이름의 컴포넌트를 생성하여 사용하는 것으로 보였다. 
- 그러나 최근 react-router v6 업데이트 이후, 적용이 어려운 것으로 보였다. 

```react
import { Route, Redirect } from 'react-router';

const PrivateRoute = ({component: Component, ...parentProps}) => {
  return (
    <Route
      {...parentProps}
      render={props => (
        checkAuth() ? (
         <Component {...props} parentMenu={this.props.menu} />
        ) : (
         <Redirect to="/403" />
        )
      )}
    />
  );
}
```



>[React Router 6: Private Routes (alias Protected Routes)](https://www.robinwieruch.de/react-router-private-routes/)

- 따라서 위 글을 읽고 아래와 같은 `PrivateRoute` 컴포넌트를 생성하여 사용하였다. 

  

```react
import { Navigate, useLocation, Outlet } from "react-router-dom";
import useIsLoggedIn from "../util/useIsLoggedIn";

export default function PrivateRoute({ children }) {
  const location = useLocation();
  const isLoggedIn = useIsLoggedIn();
    
  if (!isLoggedIn) {
    return (
      <Navigate
        to="/login"
        replace="true"
        state={{ from: { pathname: location.pathname } }}
      />
    );
  }

  return children ? children : <Outlet />;
}
```

- 로그인 여부를 확인하는 custom hook 을 사용하여, 로그인 하지 않은 유저의 경우엔 로그인 페이지로 이동시킨다. 
-  `Outlet` 컴포넌트를 사용하여 `PrivateRoute` 를 단순히 Layout Component 로 사용 가능하다. 
- 로그인 페이지에서는 state 를 받아, 로그인 후 redirect 할 주소로 사용한다.  
- 아래와 같이 `Route` 컴포넌트의 element 에 넣어 사용한다. 

```react
        <Route
          path="home"
          element={
            <ProtectedRoute user={user}>
              <Home />
            </ProtectedRoute>
          }
        />
```

- 여러 컴포넌트를 감싸야 할 경우엔 아래와 같다. (`Outlet` 을 쓴 이유)

```react
        <Route element={<ProtectedRoute user={user} />}>
          <Route path="home" element={<Home />} />
          <Route path="dashboard" element={<Dashboard />} />
        </Route>
```



