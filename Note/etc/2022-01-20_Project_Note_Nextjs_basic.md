# Project Note : Next.js 도입 

## Next.js 

### install

기존 진행하던 CRA 프로젝트에 next 만 설치하여 적용해보고자 했으나, 구조 상 바꿀 부분이 많았다. 

CNA(create-next-app) 로 프로젝트를 생성하여, 기존의 코드와 파일을 옮겨서 이전하였다. 

 ```bash
 npm create-next-app
 ```

CRA 구조와 다르게, src 폴더가 없고, 프로젝트 가장 상위에 pages 폴더를 통해 routing 기능을 사용할 수 있다. 

내 프로젝트에는 public 폴더에 이미지 파일, styles 폴더에 css 파일을 담고, components 폴더를 생성하여 컴포넌트를 담았다. 

또한 pages 폴더 내에, 2개의 파일을 추가했다. 

```react
//_app.js
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import "../styles/global.css"

function MyApp({ Component, pageProps }) {
  return (
    <div>
      <div className="navbar">
        <Navbar></Navbar>
      </div>
      <div className="page_body min-vh-100">
        <Component {...pageProps} />
      </div>
      <Footer />
    </div>
  );
}

export default MyApp;
```

- `_app.js` 는 page 컴포넌트가 렌더링 될 때 거쳐가는 root 컴포넌트와 역할이 같다. 
- css 파일을 `_app.js` 에 위치시키면 전역에 적용이 가능하다. navbar, footer 와 같은 컴포넌트도 마찬가지!

```react
//_document.js
import Document, { Html, Head, Main, NextScript } from "next/document";

class CustomDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
            crossOrigin="anonymous"
          />
          <link
            href="https://fonts.googleapis.com/icon?family=Material+Icons"
            rel="stylesheet"
          />
          <body>
            <Main />
            <NextScript />
            <script
              src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
              integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
              crossOrigin="anonymous"
            ></script>
          </body>
        </Head>
      </Html>
    );
  }
}

export default CustomDocument;

```

- `_document.js` 는 CRA 초기에 주어지는 `index.html` 과 비슷하다. `next/document` 의 컴포넌트를 가져와서 Html > Head & body  구조로 구성해야 하며, 이 곳에 google font 등의 styling CDN 을 적용하면 된다. 

### styling

html img 태그가 말썽이다. 

```react
import Image from 'next/image'
```

- `<Image>` 컴포넌트를 대신 사용하자 

특정 컴포넌트 scope 에만 적용하고 싶은 css 파일은, `<filename>.module.css` 과 같이 css 파일을 생성하여 작성한다. 또한 객체 형태로 import 해야 한다. 

```react
import styles from "../styles/footer.module.css"

// ...
	<div className={styles.footer-body}></div>
	<div className={`${styles.footer-context} btn-primary`}></div>
// ... 
```

위와 같이 객체로 접근해야 한다... 후... 

### routing

next.js 에서는 파일 구조로 routing url 설정이 가능하다. 

>공식문서 : [Link](https://nextjs.org/docs/api-reference/next/link)
>
>1. next js 라우팅 간단 사용법 : https://merrily-code.tistory.com/52
>
>2. react-router-dom 과의 차이 : [Next.js를 배우기전에...!](https://velog.io/@thsoon/next.js를-배우기-전에)
>

위의 두 글을 참고하여 파일 구조를 쉽게 이해할 수 있었다.  

동적 라우팅을 위해선, 변수에 해당하는 url 을 `[]` 로 감싸면 해결! ex) `/detail/:id` => `/detail/[id].js`

navbar 에 `next/link` 라이브러리에서 가져온 `<Link>` 컴포넌트를 적용하여 `<a>` 태그처럼 사용했다. 

>공식문서 : [useRouter & router object](https://nextjs.org/docs/api-reference/next/router#userouter)

또한 `useRouter` API 를 통해 `router` 객체에 접근할 수 있고, 

router 객체의 `pathname`, `asPath`, `query`  를 통해 현재 url 과 params 에 쉽게 접근 가능하다. 

`query` 는 동적 라우팅을 위해 작성한 params 를 객체 형태로 담고 있다. 



### SSR, pre-rendering 구현하기 

> [[FE] SSR(Server-Side-Rendering) 그리고 SSG(Static-Site-Generation) (feat. NEXT를 중심으로)](https://velog.io/@longroadhome/FE-SSRServer-Side-Rendering-%EA%B7%B8%EB%A6%AC%EA%B3%A0-SSGStatic-Site-Generation-feat.-NEXT%EB%A5%BC-%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C)
>
> 1. 굳이 SEO 적용 또는 데이터 pre-rendering이 필요 없다면 CSR 방식
> 2. 정적 문서로 충분한 화면이면서 빠른 HTML 문서 반환이 필요하다면 SSG 방식
> 3. 매 요청마다 달라지는 화면이면서 서버 사이드로 이를 렌더링 하고자 한다면 SSR 방식
>
> [Next.js getStaticProps 사용기](https://velog.io/@taeung/Next.js-getStaticProps-%EC%82%AC%EC%9A%A9%EA%B8%B0)

Next js 에서 useEffect, getStaticProps, getServerSideProps 의 차이를 구분하기 위해 많은 시간을 할애했다. 

서버에서 데이터를 가지고 오기 위해 axios 요청을 언제 보내야 하는지, redux store 의 값을 언제 가져와서 사용해야 할 지.. 고민이 많았는데, 위의 두 글을 읽고 어느 정도 해소됐다.  

덕분에 CSR 과 SSG, SSR 을 각각 언제 써야하는지 명확히 알게 되었다!





