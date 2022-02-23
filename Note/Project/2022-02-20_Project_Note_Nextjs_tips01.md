# Project Note : Next.js tips 01

이번 프로젝트에서 Next.js 프레임워크를 처음 사용해보며 여러 문제에 마주쳤는데, 기억 나는대로 정리해보려고 한다. (순서는 기억의 흐름대로..)

## Server Side Rendering 

>[공식문서 getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props)
>
>[[FE] SSR(Server-Side-Rendering) 그리고 SSG(Static-Site-Generation) (feat. NEXT를 중심으로)](https://velog.io/@longroadhome/FE-SSRServer-Side-Rendering-%EA%B7%B8%EB%A6%AC%EA%B3%A0-SSGStatic-Site-Generation-feat.-NEXT%EB%A5%BC-%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C)
>
>[Next.js getStaticProps 사용기](https://velog.io/@taeung/Next.js-getStaticProps-%EC%82%AC%EC%9A%A9%EA%B8%B0)

Next.js 의 경우, pre-Rendering 을 통한 Static Generation 과 SSR 구현이 가능하다. Next.js 는 PreRendering 을 위해 `getStaticProps` 와 `getServerSideProps` 두가지 함수를 제공한다. 

둘의 차이는? 

`getStaticProps` 는 빌드 시에 데이터를 요청하여 정적 페이지를 생성한다. 또한, `getStaticPaths` 와 함께 사용하여 해당하는 path 를 미리 생성하고 캐싱하여 페이지 이동 시 매우 빠른 렌더링을 보여준다.  

`getServerSideProps` 는 페이지가 요청될 때마다, 데이터를 재요청한다. 	

내 프로젝트의 경우엔, 

1. 게시물의 생성, 수정 삭제로 인해 페이지의 업데이트가 잦다.
2. 그때 그때 요청에 따라 페이지의 콘텐츠가 달라져야 한다. 

따라서 `getStaticProps` 를 이용한 정적 페이지 구성은 유용하지 않다고 판단되어 React hook (`useEffect`) 를 이용한 CSR 과 `getServerSideProps` 를 이용한 SSR 방식을 사용하였다. 

`useEffect` 와 `getServerSideProps`를 통한 데이터 fetching 은 페이지 요청 시에 재실행 된다는 점에서는 비슷해보이지만, CSR 과 SSR 의 본질적인 차이가 있다. 

`useEffect` 는 컴포넌트 마운트 된 이후에 실행되기 때문에 data fetching 시간에 의한 깜빡거림이 발생한다. 따라서 따로 로딩 상태를 화면에 보여주는 등의 처리를 통해 사용자 경험을 향상시켜야 한다. 

`getServerSideProps` 는 data fetching 후에 페이지를 로드 하기 때문에, 페이지 전환이 조금 느릴 순 있어도, 깜빡거림을 따로 처리해 줄 필요는 없을 것이다. (또한, 선택적으로 preview mode 를 사용하여 데이터 로드 전 페이지를 미리 로드하는 것도 가능하다. [참고](https://nextjs.org/docs/advanced-features/preview-mode))

### getServerSideProps 

>[Context parameter](https://nextjs.org/docs/api-reference/data-fetching/get-server-side-props#context-parameter)
>
>[getServerSideProps return values](https://nextjs.org/docs/api-reference/data-fetching/get-server-side-props#getserversideprops-return-values)

`getServerSideProps` 는 context 객체를 인자로 받으며, `params`, `req`, `res` 등의 key 를 가진다. 리턴값으로는 `props`, `notFound`, `redirect` 사용이 가능하다.  

아래는, 프로젝트에 작성한 `getServerSideProps` 함수 예시이다. 

```react
export async function getServerSideProps({ params }) {
  const { id } = params;
  

  const SURVEY_DETAIL_URL = `${process.env.NEXT_PUBLIC_SERVER}/api/survey/${id}`;
  const surveyDetail = await axios
    .get(SURVEY_DETAIL_URL)
    .then((res) => res.data)
    .catch((err) => console.log(err));

  if (surveyDetail.status !== 0) {
    return {
      return {
        notFound: true
      },
    };
  }

  return {
    props: {
      sId: id,
      surveyDetail,
    },
  };
}
```

- context params 를 통해 게시물 id 를 가져온 뒤, axios 요청으로 데이터를 요청한다. 
- 데이터 상태가 유효하지 않은 경우, `notFound` 페이지로 redirect 한다. 
  - Next.js 에선 `pages/404.js` 를 작성하여 not found페이지로 사용 가능하다. 
- 로그인 되어 있지 않은 사용자의 경우, `redirect` 를 리턴하여 로그인 페이지로 이동 시키는 등의 방법도 사용 가능하다. 
- props 를 리턴하여 컴포넌트에 데이터를 전달한다. 

____

## `window` 객체 

`window` 객체는 local storage, session storage 등에 접근하거나, `window` 객체에 이벤트 리스너를 등록해 사용해야 할때 필요하다. 

Next.js 사용 시, pre-Rendering 은 server-side 에서 발생한다. 따라서 pre Rendering 시엔 client-side 에만 존재하는 `window` 객체를 사용할 수 없다. `document` 객체도 마찬가지이다. 

아래 정리된 글을 참고하면 이해가 쉽다.

>[Next.js "window,document is not defined" 해결하는 법](https://sumini.dev/issue/000-nextjs-window,document-is-not-defined/)

1. `componentDidMount` lifecycle hook 사용

2. `next/dynamic`사용 

3. 가장 단순한 If 문 사용 

   ```react
   if (typeof window !== 'undefined') {
     // do something 
   }
   ```

3번 방식이 간단하고, 가장 흔히 사용되는 것으로 보였다.

`useEffect` 내에서 작성 예시.

```react
useEffect(() => {
  if (typeof window !== 'undefined') {
  	window.addEventListener(scroll, scrollAnimate)
	}
  return window.addEventListener(scroll, scrollAnimate)
}, [])
```

## wow.js 

위에서 설명했듯, `window` 객체가 없으므로 React 에 적용할 때와 조금 다르다. 

```react
// react.js
import WOW from 'wowjs';

function App() => {
  useEffect(() => {
    new WOW.WOW().init();
  }, []);
  
  return (
    <h2 className={"wow fadeInUp"}>I'm animated!</h2> 
  )
}
```

```react
// next.js 
const isServer = typeof window === 'undefined'
const WOW = !isServer ? require('wow.js') : null

function MyComponent() {
  componentDidMount() {
    new WOW.WOW().init()
  }
  
  return (
    <h2 className={"wow fadeInUp"}>I'm animated!</h2> 
  )
}
```

or 

```react
componentDidMount() {
  if(typeof window !== 'undefined') {
    window.WOW = require('wowjs');
  }
  new WOW.WOW().init();

}
```



