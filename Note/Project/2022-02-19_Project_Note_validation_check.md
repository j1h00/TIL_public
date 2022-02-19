# Project Note : validation check

## Intro 

회원 가입 및 로그인 로직을 구현하며... 입력된 회원 정보에 대한 유효성 검사를 진행해야 할 필요가 있었다. 

HTML input tag 의 `type`, `required`, `min`, `max` 등의 속성을 통해 간단한 유효성 체크가 가능하지만, 원하는 값을 정확히 입력 받기 위해서 좀 더 고도화된 유효성 검사가 필요함을 느꼈다. 

또한 백엔드 서버로 데이터를 보내는 과정에서, 복잡한 form data 에 관리가 필요함을 느꼈다. (특히 회원 정보 입력 뿐만 아니라, 프로젝트의 핵심 기술인 설문 생성 시에, 많은 양의 form data 관리에 용이하다. )

따라서 여러 방법을 검색 및 검토해보고, react-hook-form 를 통한 form data 관리와 yup 라이브러리를 적용해 해결하였다. 

## react-hook-form 

### intro

>[react-hook-form 공식 문서](https://react-hook-form.com/)
>
>Performant, flexible and extensible forms with easy-to-use validation.

- 랜딩 페이지에 react-hook-form 의 장점에 대해 설명되어 있다. 
- form-data 를 적은 코드로 쉽게 관리할 수 있도록 돕고, re-render 를 최소화해준다. 그리고 가볍다!!
- 또한 yup 라이브러리와 연동하여 유효성 검사를 쉽게 할 수 있도록 돕는다. 

아래 명령어를 통해 설치 가능하다. 

```bash
$ npm install react-hook-form
```

### 기본 예제 

가장 기본적인 예제를 살펴보자 

```react
import React from "react";
import { useForm } from "react-hook-form";

export default function App() {
  const { register, handleSubmit, watch, formState: { errors } } = useForm();
  const onSubmit = data => console.log(data);

  console.log(watch("example")); // watch input value by passing the name of it

  return (
    /* "handleSubmit" will validate your inputs before invoking "onSubmit" */
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* register your input into the hook by invoking the "register" function */}
      <input defaultValue="test" {...register("example")} />
      
      {/* include validation with required or other standard HTML validation rules */}
      <input {...register("exampleRequired", { required: true })} />
      {/* errors will return when field validation fails  */}
      {errors.exampleRequired && <span>This field is required</span>}
      
      <input type="submit" />
    </form>
  );
}
```

- `useForm` hook 에서 `register` 를 불러온 뒤, input tag 의 속성에 `{...register(name)}` 를 작성하여 등록한다.
- form 제출시에 `handleSubmit`의 인자로 넘긴 onSubmit 의 인자로 data 가 인자로 주어지며, 이 data 내에 위의 `register` 로 등록된 Input tag 의 value 가 모두 담겨있다. 
- register 시엔, `required` 등의 option 을 설정하여 관리할 수 있다. 
- `required` 등의 유효성 검사를 통과하지 못했을 경우,  errors 객체를 통해 확인 가능하다. 

### 적용

아래는 프로젝트에 적용한 react-hook-form 의 예제이다.

```react
// input tag register 예제 
<div className="input-box form-floating">
  <input
    id="email"
    type="text"
    className="form-control"
    placeholder=" "
    {...register("email", {
      onChange: () => setEmailChecked(false),
    })}
    />
  <label htmlFor="email">
    <p className="text-secondary">you@example.com</p>
  </label>
  <span className="fs-0 text-danger ms-1">
    {errors.email?.message}
  </span>
</div>
```

- 이메일 input 대한 register 예제 
- `useForm` 에서 호출한 `formState` 의 errors 객체에 저장된 에러 메시지도 출력이 가능하다. 
  - register 옵션, 혹은 아래 설명할 yup schema 작성 시에, 특정 경우에 대해 출력할 error message 를 설정할 수 있다. 


```react
// `onSubmit` 함수 예제 (파일 전송 시)
const onSubmit = async (data) => {
  if (!(emailChecked && bnChecked)) {
    toast.dismiss();
    toast.warning("중복 확인이 필요합니다.");
    return;
  }
  // 백엔드 서버에서 요구하는 형태로 가공 
  const requestData = processData(data);

  await axios
    .post(SIGNUP_URL, requestData, {
  })
    .then((res) => {
    toast.success("서비스 신청 완료!");
    router.push("/");
  })
    .catch((err) => {
    toast.dismiss();
    toast.error("서비스 신청 실패!");
    console.log(err);
  });
};
```

- `onSubmit` 의 data 는  input tag 의 value 들을 객체 형태로 담고 있다. 
- 백엔드 서버에서 요구하는 형식대로 데이터를 가공하여 전송한다. 

## yup 

### intro

yup 은 유효성 검사를 위해 널리 사용되는 라이브러리이다. 

>[yup github 문서](https://github.com/jquense/yup)
>
>[yup with react-hook-form](https://react-hook-form.com/get-started#schemavalidation)

react-hook-form 은 yup 등의 유효성 검사 라이브러리와의 연동을 지원한다. 

두번째 글에 기본 예제가 설명되어 있으며, 사용법이 매우 간단하다. 

아래 명령어를 통해 설치한다. 

```bash
$ npm install @hookform/resolvers yup
```

### 적용 

아래는 프로젝트에 적용한 yup validation schema 이다. 

```react
const schema = yup.object().shape({
  email: yup
    .string()
    .email("유효하지 않은 이메일입니다.")
    .required("이메일 입력은 필수입니다."),
  password: yup
    .string()
    .required("비밀번호 입력은 필수입니다.")
    .matches(
      /^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W))(?=.*[!@#$%^*+=-]).{8,16}$/,
      "비밀번호는 반드시 8~16자이며, 영문, 숫자, 특수문자를 포함해야 합니다."
    ),
  passwordConfirm: yup
    .string()
    .oneOf([yup.ref("password"), null], "비밀번호가 일치하지 않습니다.")
    .required("비밀번호 확인을 입력해주세요."),
  name: yup.string().required("병원명 입력은 필수입니다."),
  phone: yup
    .string()
    .required("전화번호 입력은 필수입니다.")
    .matches(
      /^((\\+[1-9]{1,4}[ \\-]*)|(\\([0-9]{2,3}\\)[ \\-]*)|([0-9]{2,4})[ \\-]*)*?[0-9]{3,4}?[ \\-]*[0-9]{3,4}?$/,
      "전화번호 양식에 맞게 입력해주세요"
    ),
  business_number: yup
    .string()
    .required("사업자 등록 번호 입력은 필수입니다.")
    .matches(
      /([0-9]{3})-?([0-9]{2})-?([0-9]{5})/,
      "사업자 등록 번호 양식에 맞게 입력해주세요. OOO-OO-OOOOO"
    ),
  logo_image: yup
    .mixed()
    .test("required", "병원 로고 이미지 파일을 선택해주세요!", (value) => {
      return value && value.length;
    })
    .test(
      "type",
      "png/jpeg/jpg 형식의 파일을 선택해주세요!",
      function (value) {
        return (
          value &&
          value[0] &&
          (value[0].type === "image/jpeg" ||
           value[0].type === "image/jpg" ||
           value[0].type === "image/png")
        );
      }
    )
    .test("fileSize", "파일 사이즈가 너무 큽니다!", (value, context) => {
      return value && value[0] && value[0].size <= 200000;
    }),
});

const {
  register,
  handleSubmit,
  formState: { errors },
  getValues,
} = useForm({
  resolver: yupResolver(schema),
});
```

- yup schema 를 작성한 뒤, react-hook-form 의 `useForm` hook 사용시, `resolver` 에 yup schema 를 등록해준다. 
- schema 는 기본적인 string 등의 type 설정은 물론, `required`, `oneOf`, `matches` 등을 통해 필요한 유효성 검사를 설정할 수 있다.
  - 특히 `matches` 에, regex 를 등록하여 비밀번호 형식, 사업자 등록 번호 형식 등을 제한 가능하다. 
-  또한, file input 을 받아야 하는 경우, 기본적인 HTML input tag 는 `accept` 속성을 통해 파일 형식을 지정할 수 있는데, 이는 사용자가 이미지 파일을 선택하도록 유도할 뿐, 파일 형식을 완전히 제한하지 못한다. (파일 선택 시 이미지 확장자 뿐만 아니라 모든 파일 확장자를 선택할 수 있다. )
  - 이 때 yup 을 통해 위와 같이 설정하면, 이미지 확장자 뿐만 아니라 파일 크기까지 제한 가능하다.

## 기타 

기타 사용한 react-hook-form 의 기능으로는 setValue, geValue, unregiser 등이  있다. 

1. setValue 는 input tag 의 value 를 원하는 값으로 set 가능하다. 

예를 들어, 게시글 등의 수정 페이지의 경우, 서버로부터 기존 데이터를 받아 그 데이터로  input 을 채워둬야 하는데, 이 때 setValue 를 사용하면 편리했다. 

```react
setValue("title", title);
setValue("context", context);
setValue("start_at", start_at.slice(0, 10));
setValue("end_at", end_at.slice(0, 10));
```

2. unregister 

내 프로젝트의 경우, 사용자가 설문 조사를 생성하는 페이지가 필요했다. (Google Form 처럼 설문조사를 생성할 수 있는 서비스를 생각하면 편하다.) 

이 때 사용자가 설문 문항을 추가하거나 삭제하는 것이 가능해야 했다. 따라서 동적으로 input tag 의 생성과 삭제가 가능해야 했으며, 그 input tag 의 data 도 관리가 필요했다. 다시 말해, 새로운 설문 문항이 생생되면 `register` 를 통해 고유한 이름으로 그 설문 문항 input tag 를  등록하고, 삭제할 때는 다시 `unregister` 를 사용하여 그 설문 문항의 input tag 의 등록을 삭제했다. 



## 끝!

이미지 파일과 같은 데이터를 서버에 전송해야 하는 경우, file 객체를 FormData 객체에 담아 전송하고, 서버에서는 이를 받아서 이미지 파일을 원하는 확장자로 저장해야 한다. 이 과정에서 고생한 경험이 있으므로, 다음 글에서 이에 대해 작성해보겠다. 



