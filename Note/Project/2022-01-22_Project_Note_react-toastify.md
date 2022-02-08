# Project Note : react-toastify

https://fkhadra.github.io/react-toastify/introduction

매우 귀엽고 사용이 간단한 알림창 라이브러리!

나의 경우엔, `<ToastContainer>` 컴포넌트를 루트 페이지에 선언하고 (이렇게 하면 페이지 전환 시에도 알림창이 남아있다! )

Toast Emitter 인 `toast("Alarm Message")` 로 로그인, 로그아웃 등의 경우에 알림창을 발생시켰다. 

playground 에서 데모를 사용해볼 수 있다!



## promise 

`toast.promise` 를 이용하면, 데이터 fetching 시 필요한 로딩 창을 쉽게 구현할 수 있을 것으로 보인다. 

https://fkhadra.github.io/react-toastify/promise

예시 코드)

```react
const resolveAfter3Sec = new Promise(resolve => setTimeout(resolve, 3000));
toast.promise(
    resolveAfter3Sec,
    {
      pending: 'Promise is pending',
      success: 'Promise resolved 👌',
      error: 'Promise rejected 🤯'
    }
)

const functionThatReturnPromise = () => new Promise(resolve => setTimeout(resolve, 3000));
toast.promise(
    functionThatReturnPromise,
    {
      pending: 'Promise is pending',
      success: 'Promise resolved 👌',
      error: 'Promise rejected 🤯'
    }
)
```

await 방식

```react
const response = await toast.promise(
    fetch("A_URL"),
    {
      pending: 'Promise is pending',
      success: 'Promise resolved 👌',
      error: 'Promise rejected 🤯'
    }
);
console.log(response)
```

`toast.loading` 과 `toast.update` 를 통해 수동으로 구현도 가능하다. 

```react
const id = toast.loading("Please wait...")
//do something else
toast.update(id, { render: "All is good", type: "success", isLoading: false });
```

