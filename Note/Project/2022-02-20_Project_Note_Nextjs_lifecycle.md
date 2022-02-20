# Project Note : Next.js tips 02

이번 프로젝트에서 Next.js 프레임워크를 처음 사용해보며 여러 문제에 마주쳤는데, 기억 나는대로 정리해보려고 한다. (순서는 기억의 흐름대로..)

## CSS

>[Next.js Built-in CSS](https://nextjs.org/docs/basic-features/built-in-css-support)

global scope 에서 적용되는 CSS 파일은 최상위 컴포넌트인 `_app.js` 에서 다음과 같이 import 하여 적용하면 된다. 

```react
import "../styles/globals.css";
import "../styles/navbar.css";
import "../styles/footer.css";
```

그러나 위 처럼, `navbar.css`, `footer.css` 와 같은 CSS 는 navbar, footer 에서만 적용될 CSS 를 뜻하므로 global 로 적용하기 적절치 않을 수 있다. 

이와 같은 CSS 를 특정 컴포넌트 스코프에만 적용하기 위해선, 특정 규칙이 존재한다.

>[Adding Component-Level CSS](https://nextjs.org/docs/basic-features/built-in-css-support#adding-component-level-css)

CSS 파일명을 `[name].module.css` 과 같이 작성하고, 컴포넌트에서 다음과 같이 적용한다. 

```css
# Button.module.css
.error {
  color: white;
  background-color: red;
}
```

```react
import styles from './Button.module.css'

export function Button() {
  return (
    <button
      type="button"
      className={styles.error}
    >
      Destroy
    </button>
  )
}
```

여러 개의 클래스명을 적용해야 하거나, 직접 작성한 CSS 컴포넌트 모듈과 흔히 사용하는 tailwind CSS 등의 클래스명을 같이 사용해야 할 경우엔?

>[How to add multiple classNames to nextjs elements](https://stackoverflow.com/questions/65912413/how-to-add-multiple-classnames-to-nextjs-elements)

1. backtick string 을 사용한다. 

```react
<li className={`${styles.projects-pd-text} ${styles.projects-pd-subdetail}`}>
   {sub}
</li>
```

2. join 메서드를 사용한다. 

```react
<li className={[styles.projects_pd_text, styles.projects_pd_subdetail].join(" ")}>
   {sub}
</li>
```

3. classnames 라이브러리를 설치하여 사용하면 심플하다!

>[classnames github](https://github.com/JedWatson/classnames)

```react
import cn from "classnames";
import styles from "../styles/surveySubmit.module.css";

<div className={cn(styles.submitError, "rounded", "p-1", "fs-0" )}>
  <span className="material-icons fs-6">priority_high</span>
  <span>시작일 입력은 필수입니다.</span>
</div>
```

나의 경우 3번을 사용했다!

직접 작성한 CSS 와 bootstrap, tailwind 의 CSS 클래스명을 같이 써야 하는 경우 유용하다. 



