# Project Note : Next.js tips

이번 프로젝트에서 Next.js 프레임워크를 처음 사용해보며 여러 문제에 마주쳤는데, 기억 나는대로 정리해보려고 한다. (순서는 기억의 흐름대로..)

## CSS

global scope 에서 적용되는 CSS 파일은 `_app.js` 에서 다음과 같이 import 하여 적용하면 된다. 

```react
import "../styles/globals.css";
import "../styles/navbar.css";
import "../styles/footer.css";
```

그러나 위 처럼, `navbar.css`, `footer.css` 와 같은 CSS 는 navbar, footer 에서만 적용될 CSS 를 뜻하므로 global 로 적용하기 적절치 않을 수 있다. 

이와 같은 CSS 를 특정 컴포넌트 스코프에만 적용하기 위해선, 특정 규칙이 존재한다. 











## Server Side Rendering 





