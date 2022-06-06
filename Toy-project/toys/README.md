# toy-projects 

## 1. JavaScript 30 

> [javascript30](https://javascript30.com/) 

- vanilla JS 연습을 위해 위 강좌를 보고 진행한 토이 프로젝트

### [Drum kit](./javascript30/drum-kit)

- data-key 를 이용한 DOM select
- [keycode info](https://www.toptal.com/developers/keycode)
  - `event.keycode` is deprecated => use `event.key `

- audio element 는 play 로 실행 가능 
- `key.classList.remove('playing')`
  - `setTimeOut` ? 
  - `key.addEventListener('transitioned', removeTransition)`



### [Clock](./javascript30/clock)

- 시침, 분침, 초침이 원의 중심을 기준으로 `rotate()` 하는게 중요
  - `transform-origin: 100%;`
- `transition-timing-function` 으로 시침이 틱틱 거리는 걸 표현 가능 
  - `cubic-bezier(0.1, 2.7, 0.58, 1)`

- easy

## 2. creative coding 

>[interactive developer 김종민 channel](https://www.youtube.com/watch?v=hCHL7sydzn0&list=PLGf_tBShGSDNGHhFBT4pKFRMpiBrZJXCm)

- HTML canvas 를 활용한 creative coding tutorial 따라하기 

### [Ball collision](./creative/ball-collision)

- `window.onload` 

  - > https://velog.io/@leyuri/javaScript-window.onload%EB%9E%80

  - `window.onload` 함수를 오버라이딩하여, 해당 함수 내의 코드가 웹브라우저 내의 모든 요소가 준비된 후 실행이 되도록 한다. 

    

- >[CanvasRenderingContext2D API docs](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/arc)

  - 



