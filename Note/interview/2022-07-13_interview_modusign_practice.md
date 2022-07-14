# interview modusign

### 쿠키란 ?  

>HTTP Cookie (웹 쿠키, 브라우저 쿠키) 는 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각입니다. 브라우저는 그 데이터 조각들을 저장해 놓았다가, 동일한 서버에 재 요청 시 저장된 데이터를 함께 전송합니다
>
>쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용합니다. 이를 이용하면 사용자의 로그인 상태를 유지할 수 있습니다. 상태가 없는([stateless](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#HTTP_is_stateless_but_not_sessionless)) HTTP 프로토콜에서 상태 정보를 기억시켜주기 때문입니다.



쿠키는 주로 3가지 목적을 위해 사용한다. 

1. 세션 관리 (Session Management): 서버에 저장해야 할 로그인, 장바구니, 게임 스코어 등의 정보 관리
2. 개인화 (Personalization): 사용자 선호, 테마 등의 세팅
3. 트래킹(Tracking)

과거엔 클라이언트 측에 정보를 저장할 수 있는 유일한 방법인 쿠키를 자주 사용했으나, 지금은 modern storage APIs (localStorage, sessionStorage, IndexedDB) 를 사용해 정보를 저장하는 걸 권장한다. (모든 요청마다 쿠키가 함께 전송되기 때문에 성능이 떨어지는 원인이 될 수 있다. )



세션 쿠키: 브라우저를 닫는 순간 삭제 

지속 쿠키: 디스크에 저장되며 브라우저를 닫거나 컴퓨터를 재시작해도 남아있다. => `Expires`, `Max-Age` 속성을 사용한다.



### **쿠키 만들기**

HTTP 요청 수신 시, 서버는 응답과 함께 `Set-Cookie` 헤더를 전송할 수 있다. 쿠키는 보통 브라우저에 의해 저장되며, 

```
Set-Cookie: <cookie-name>=<cookie-value>
```

그 후 쿠키는 같은 서버에 의해 만들어진 요청(Request) 들의 Cookie HTTP 헤더 안에 포함되어 전송된다. 

```
GET /sample_page.html HTTP/1.1
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry
```

만료일 혹은 지속기간을 명시하며, 만료된 쿠키는 더 이상 보내지지 않는다. 또한 특정 도메인 혹은 경로 제한을 설정할 수 있으며 이는 쿠키가 보내지는 것을 제한할 수 있다.

**쿠키 라이프타임** 은 두 가지 방법으로 정의할 수 있다. 

- 세션 쿠키는 현재 세션이 끝날 때 삭제된다. 브라우저는 현재 세션이 끝나는 시점을 정의하며, 어떤 브라우저들은 재시작 시 세션을 복원해 세션 쿠키가 무기한 존재할 수 있도록 한다. 
- 영속적인 쿠키는 `Expires` 속성에 명시된 날짜에 삭제되거나, `Max-age` 속성에 명시된 기간 이우헤 삭제된다. 

**`Secure` 과 `HttpOnly`** 쿠키 

Secure 쿠키는 HTTPS 프로토콜 상에서 암호화된 요청일 경우에만 전송된다. (하지만 민감한 정보는 절대 쿠키에  저장되면안된다)

Cross-Site Scripting (XSS) 공격을 방지하기 위해, `HttpOnly` 플래그를 사용하면 Javascript 의 `Document.cookie` API 에 접근할 수 없고 서버에게 전송되기만 한다. 



**쿠키 스코프**

`Domain`과 `Path` 디렉티브는 쿠키의 스코프를 정의한다.

`Domain` 은 쿠키가 전송되게 할 호스트를 명시하며, 명시된 경우 서브도메인들은 항상 포함된다.  (만약 명시되지 않는다면, 현재 문서 위치의 호스트 일부를 기본값으로)

`Path` 는 `Cookie` 헤더를 전송하기 위해 요청되는 URL 내에 반드시 존재해야 하는 URL 경로이다. 

만약 `Path=/docs` 로 설정되면, `/docs`, `/docs/Web/`, `/docs/Web/HTTP` 와 같은 경로들은 모두 매치된다. 



### 보안

쿠키를 가로채는 것은 인증된 사용자의 세션 하이재킹으로 이어질 수 있다. 

일반적으로 소셜 공학 사용 혹은 애플리케이션 내 XSS 취약점을 이용하는 방법으로 쿠키를 가로챈다. 

`HttpOnly` 쿠키 속성은 자바스크립트를 통해 쿠키 값에 접근하는 것을 막아 이런 공격을 누그러뜨릴 수 있다. 



## Quick Sort 

```js
function quickSort(array) {
    if (array.legnth < 2) {
        return array;
    }
    
    const pivot = [array[0]];
    const left = [];
    const right = [];
    
    for (let i = 1; i < array.length; i++) {
    	if (array[i] < pivot) {
            left.push(array[i])
        } else if (array[i] > pivot) {
            right.push(array[i])
        } else {
            pivot.push(array[i])
        }
    }
    
    return quickSort(left).concat(pivot, quickSort(right));
}
```



## Merge Sort

```js
function mergeSrot(arr) {
    if (arr.length < 2) {
        return arr;
    }
    
    const mid = Math.floor(array.length / 2);
    const left = array.slice(0, mid);
    const right = array.slice(mid);
    
    return merge(mergeSort(left), mergeSort(right))
}

function merge(left, right) {
    const resultArr = [];
    let leftIndex = 0;
    let rightIndex = 0;
    
    while(leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            resultArr.push(left[leftIndex]);
            leftIndex++;
        } else {
            resultArr.push(right[rightIndex]);
            rightIndex++;
        }
    }
    
    return resultArray.concat(left.slice(leftIndex), right.slice(rightIndex));
}
```

## 이미지 최적화 

>https://oliveyoung.tech/blog/2021-11-22/How-to-Improve-Web-Performance-with-Image-Optimization/

### 이미지 종류 및 특성 

래스터 이미지와 벡터 이미지 

- Raster Image

  (.jpeg .gif .png) 픽셀에 표현하고자 하는 색상을 그려서 이미지 형태로 표현하는 방식

- Vector Image: 

  이미지 안에 있는 계산식으로 연산하여 이미지를 제공, 사이즈가 변경되어도 이미지가 깨지거나 정보가 달라지지 않는다. 따라서 항상 같은 이미지 품질을 유지하므로 아이콘, 폰트 등에 사용되며 대표적인 W3C 포맷인 SVG 가 많이 사용된다. 

무손실 이미지와 손실 이미지 

- 무손실 이미지

  원본 이미지에서 이미지를 렌더링하는데 필요하지 않은 정보들을 제거한 이미지이며, 원본 이미지보다 용량이 줄어들 수 있다. (GIF, PNG)

- 손실 이미지 

  무손실 이미지의 화질 감소를 감수하면서도 사이즈를 줄여 빠른 렌더링을 할 수 있는 이미지. (JPEG)

WebP & AVIF 포맷

![AVIF Format Size](https://oliveyoung.tech/static/caf8d6b7a02bc8b6aef36f0c98b0776e/62aaf/6.jpg)

### 이미지 최적화 방법

#### 1. 브라우저 사이즈에 맞춰 적절한 이미지 제공 

데스크톱의 이미지는 모바일의 이미지보다 상대적으로 용량이 클 수 밖에 없고, 사용자는 필요 이상의 이미지를 다운받게 되어 리소스가 낭비될 수 있다. 그러므로 브라우저 사이즈에 맞게 브레이크 포인트를 걸어 과도한 리소스를 사용하지 못하게 한다. 

이를 위해 미디어쿼리, `<img>` 태그의 srcset 속성, `<picture>` 태그 등의 방법이 있다. 

#### 2. 이미지 Lazy Loading

최대한 사용자가 보이는 부분부터 로드되도록 처리하며, 보이지 않는 부분은 Lazy Loading 을 적용하여 사용자 경험 저하를 막는다. 사용자가 처음부터 보지 않는 부분을 초기 렌더링 시 로드하게 되면 정작 사용자가 보이는 화면의 로딩 시간이 지연되게 된다. 

#### 3. 이미지 CDN 사용 

#### 4. CSS Image Sprite 

Sprite 이미지는, 여러 개의 이미지를 합친 하나의 이미지 셋을 말한다. 사용 시 네트워크 상에서는 실제로 10번의 이미지 요청을 1번의 요청으로 해결할 수 있으며, 트래픽이 절약되는 효과도 있다. position 값으로 잘라서 사용한다. 

## React Portal 

공식 문서에서는 이렇게 적혀있었다.

> portal의 전형적인 유스케이스는 부모 컴포넌트에 `overflow: hidden`이나 `z-index`가 있는 경우이지만, 시각적으로 자식을 “튀어나오도록” 보여야 하는 경우도 있습니다. 예를 들어, 다이얼로그, 호버카드나 툴팁과 같은 것입니다.

일단 주로 Modal, Tooltip 같이 뭔가 튀어나오는 요소에 사용된다. 위에서도 설명이 나오는데, 이런 컴포넌트들은 `z-index` , `overflow: hidden` 같은 부모 컴포넌트의 CSS에 방해를 받아 제 역할을 하기 힘들 수 있다.

그럴 때 Portal을 이용해 DOM 트리 상에서 부모 컴포넌트의 영향을 받지 않도록, 최상위 계층으로 옮김으로써 의도치 않은 CSS 상의 방해를 받지 않을 수 있다.
