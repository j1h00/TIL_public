# toy-projects 

## JavaScript 30 

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



### [CSS variables](./javascript30/CSS-variable)

- `:root` pseudo class 
  - document tree 의 루트 요소를 선택
  - 즉 CSS variables (custom properties)을 전역으로 사용하고자 할 때, `:root {}` 에 정의
- CSS variables (custom properties)
  - 이름은 `--` (double hyphen) 으로 시작하며, 대소문자를 구분한다. 
  - 사용 시에는 `var()` 내부에 변수를 작성한다. 
  - `var()` 은 fallback 을 제공하므로, default 값을 설정 가능하다. 
    - `margin: var(--box-margin, 20px);`

- 단순한 `'change'` 이벤트 리스너로는, range bar 를 마우스로 조작할 때 실시간으로 변화를 주긴 어렵다. 
  - 따라서 `'mousemove'` 이벤트도 같이 리슨한다. 
- tag 에 `data-sizing` 이라는 속성을 이용하여, 추가적인 정보를 사용할 수 있다. 
  - `data-name`, `data-whatever` 
  - 사용 시엔, 선택한 요소의 `dataset` 속성에 접근하여 사용
    - `const suffix = this.dataset.sizing || "";`



### [Array cardio 1](./javascript30/array-cardio)

- `querySelectorAll()` 는 `NodeList` 타입의 리스트를 반환한다. 
  - 따라서 `map()` 함수를 사용할 수 없다.  
