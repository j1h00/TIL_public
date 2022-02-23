# Project Note : file upload

## intro 

이 글에선, 아래 두 과정에 대해 작성해보려고 한다. (React + Node Express)

1. input tag 로 이미지 파일 등의 파일을 입력받아, 이를 node 백엔드 서버에 전송한다. 
2. node 에선 "multer" 라는 middleware 를 사용하여 파일 객체를 받아, 이를 서버 디렉터리에 파일로 저장한다.

> [node multer middleware](http://expressjs.com/en/resources/middleware/multer.html)
>
> Multer is a node.js middleware for handling `multipart/form-data`, which is primarily used for uploading files.

multer 는 요청으로 받은  `multipart/form-data` 형식의 데이터를 가공하여, 서버에 "파일"로 저장하도록 돕는다. 

multer 는 `multipart/form-data` 형식의 요청 데이터만 다룰 수 있으므로, react 에서 서버로 요청시엔, 데이터를 `FormData` 라는 객체 형태로 가공하고, 이 데이터가 `multipart/form-data` 임을 명시하여 서버에 전송해야 한다.

## 1. form-data 로 파일 전송

저번 글에서 설명한, react-hook-form 을 사용할 경우,  form submit 시에 handleSubmit 함수의 인자로 지정된 onSubmit 함수가 실행된다. 이 때 인자로 받는 data 를 다시 `FormData` 객체 형태로 가공하여야 한다. 

==react-hook-form 을 사용하지 않는 경우에도==, input tag (`type="file"`) 로 파일 객체를 입력받는 경우에,  동일한 방법으로 FormData 를 생성하여 전송하면 된다! [참고](https://www.pluralsight.com/guides/how-to-use-a-simple-form-submit-with-files-in-react)

아래는 내 프로젝트에 적용한 react-hook-form 예제이다. 

```react
// input tag 
<div className="label-box">
  <label htmlFor="logo_image">로고</label>
</div>
<div className="input-box">
  <input
    id="logo_image"
    type="file"
    accept="image/*"
    {...register("logo_image")}
    onChange={onFileChange}
    />
</div>
```

```react
// onSubmit // make Formdata 
const makeFormData = (data) => {
  const fd = new FormData();

  for (let key in data) {
    if (key === "logo_image" && data[key].length) {
      const logoFile = data[key][0];
      const logoName = logoFile.name;
      fd.append(`logo_image`, logoFile);
      fd.append(`logo_name`, logoName);
    } else {
      fd.append(`${key}`, data[key]);
    }
  }
  return fd;
};

const onSubmit = async (data) => {
  const fd = makeFormData(data);

  await axios
    .post(SIGNUP_URL, fd, {
    headers: {
      "Content-Type": `multipart/form-data`,
    },
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

- 위와 같이 `onSubmit` 함수의 인자로 `data` 를 받은 뒤, 

  `const fd = new FormData()` 처럼 `FormData` 객체를 생성하여, 이 객체에 차례차례 append 한다. 

- node 서버 디렉터리에는 파일을 저장하고, 데이터베이스에는 파일 이름만 저장하고 싶은 경우 위와 같이 `logo_image` 와 `logo_name` 을 나누어서 요청 보내면, node 서버에서 받아 처리하기 수월하다. 
  - `logo_image` : file 객체 
  - `logo_name` : string 형태의 이미지 파일 이름

- react-hook-form 을 사용하지 않는 경우에도, input tag 의 value 를 마찬가지로 가공하면 된다. 
- 요청시에는, `header` 에 `Content-Type` 을 `multipart/form-data` 로 명시해준다. 

## 2. 파일 받기 & 저장

>[multer 공식문서 # disk storage](https://github.com/expressjs/multer/blob/master/doc/README-ko.md#diskstorage)
>
>https://www.zerocho.com/category/NodeJS/post/5950a6c4f7934c001894ea83

node express 에서 multer 를 이용하여 파일을 받는 경우 아래와 같은 코드가 필요하다. 

아래는 프로젝트에 적용한 예제

```javascript
// /utils/multer.js
// multer
const multer = require("multer");
const path = require("path");

const storage = multer.diskStorage({
  destination: (req, file, done) => {
    done(null, "uploads/logo");
  },
  filename: (req, file, done) => {
    const ext = path.extname(file.originalname);
    const fileName = path.basename(file.originalname, ext) + ext;
    done(null, fileName);
  },
  limits: { fileSize: 5 * 1024 * 1024 },
});

const logo_upload = multer({ storage: storage });
```

- diskStorage 를 이용하여, 파일이 업로드 될 경로와 파일 이름 등을 설정하고, `logo_upload` 생성
  - 파일 업로드 경로는 미리 생성해두자
  - 파일 이름의 경우, 중복되지 않게 고유한 이름으로 저장되도록 설정해준다. (Datatime stamp 를 활용하면 고유 이름 생성이 쉽다.)

```javascript
// /routes/signup.js
const { logo_upload } = require("../utils/multer");

router.post("/join", logo_upload.single("logo_image"), async (req, res) => {
 // ...
 // req.logo_image 는 file 객체이다.
}
```

- react 에서 전송한 form-data 에 담긴 파일 객체인 `logo_image` 를,  multer.js 에서 생성한 `logo_upload` 객체를 통해 업로드 한다. 
- 하나의 로고 이미지만 전송 받으므로, `single` 메서드 를 사용한다. (여러 개의 파일을 전송받는 경우 `array` 메서드 사용)

## 끝!









