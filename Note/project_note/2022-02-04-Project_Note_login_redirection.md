# Project Note : Login redirection

로그인 하지 않은 유저가 특정 페이지에 접근하지 못하도록 구현해보고자 하였다. 

Next.js 에서는 redirection 에 크게 두가지 방법이 존재하는데,

**페이지가 렌더링 된 이후에, client side 에서 `useEffect` 내에서 처리**

```react
  useEffect(() => {
    if (!isLoggedIn) {
      toast.error("로그인이 필요합니다!");
      router.push("/login");
    }
  }, [isLoggedIn, router]);
```

- 이 방법은, 페이지가 렌더 된 이후에 실행되기 때문에,  페이지가 노출되면서 깜빡이는 현상이 존재한다. 

- 이를 조금이라도 방지하기 위해 컴포넌트에서 아래와 같은 코드가 필요하다 

  ```react
    if (!isLoggedIn) {
      return <div></div>;
    }
  ```

**`getServerSideProps` 에서 redirect 기능을 사용**

```react
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

그러나 나의 경우엔, `isLoggedIn` 상태를 redux state 로 관리하는데, server side rendering 시 작동하는 `getServerSideProps` 내에서 redux state 를 불러오는 것이 쉽지 않았다. 

그 이유는

1. 페이지가 새로고침 될 때마다 redux store 는 페이지가 새로고침 될 때마다 재생성되는 특징이 있는데, 

2. 나의 경우엔 redux-persist 를 이용하여 localstorage 에 state 를 저장했다가 hydrate 하는 전략을 취하므로.. 

3. ServerSide Render 시에 localstorage 에 접근이 불가하므로, hydrate 가 제대로 동작하지 못한다. 

4. 아래 console 을 보면, NEXT_REDUX_WRAPPER_HYDRATE 시에 userStatus 는 업데이트 되지 못하고, 

   persist/REHYDRATE 시에 비로소 업데이트 된다. 

![image-20220204140658631](2022-02-04-Project_Note_login_redirection.assets/image-20220204140658631.png)

이를 해결하기 위해선 redux-saga 등의 도움이 필요한 것으로 보이는데, 도입을 위한 공부가 필요할 것 같다. 

> https://hhyemi.github.io/2021/05/04/ssrprops.html
>
> 예를 들면 로그인했을 때는 내 정보를 보여주고 하지 않았을 때는 로그인하는 창이 뜬다고 하면 로그인하는 창이 잠깐 뜬 다음 내정보가 뜨게 된다. 이런 깜빡하는 현상이 거슬릴 수가 있는데 그걸 페이지 요청 시 **서버사이드 렌더링을 통해 서버 측 데이터를 먼저 받아온 후 렌더링 시키는 방법**이 있다.



따라서 redux-saga 도입에 시간이 필요할 것으로 보이므로, 일단 useEffect 를 사용한 redirection 을 이용하자!
