# toy-projects

## JavaScript 30

> [javascript30](https://javascript30.com/)

- vanilla JS 연습을 위해 위 강좌를 보고 진행한 토이 프로젝트

----

### [Drum kit](./01%20-%20JavaScript%20Drum%20Kit)

- data-key 를 이용한 DOM select

  ```js
  const audio = document.querySelector(`audio[data-key="${e.key}"]`);
  const key = document.querySelector(`.key[data-key="${e.key}"]`);
  ```

- [keycode info](https://www.toptal.com/developers/keycode)

  - `event.keycode` is deprecated => use `event.key `

- audio element 는 play 로 실행 가능

- `key.classList.remove('playing')`
  - `setTimeOut` ?
  - `key.addEventListener('transitioned', removeTransition)`

----

### [Clock](./02%20-%20JS%20and%20CSS%20Clock)

- 시침, 분침, 초침이 원의 중심을 기준으로 `rotate()` 하는게 중요
  - `transform-origin: 100%;`
- `transition-timing-function` 으로 시침이 틱틱 거리는 걸 표현 가능
  - `cubic-bezier(0.1, 2.7, 0.58, 1)`
- easy

----

### [CSS variables](./03%20-%20CSS%20Variables)

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

----

### [Array cardio 1](./04%20-%20Array%20Cardio%20Day%201)

- `querySelectorAll()` 는 `NodeList` 타입의 리스트를 반환한다.
  - 따라서 `map()` 함수를 사용할 수 없다.

----

### [Flex Panel Gallery](./05%20-%20Flex%20Panel%20Gallery)

All about CSS

- `flex` 속성으로 flex children 의 비율을 조절 가능하다.
- `flex: 1`

- `transitionend` 이벤트를 리슨하고,
  - `event.propertyName` 으로 transition 이 종료된 이벤트의 이름을 가져올 수 있다.

----

### [Type Ahead](./06%20-%20Type%20Ahead/)

- `fetch()` 는 `Promise` 객체를 리턴한다.

  - 따라서 `.then()` 메서드를 사용한다.

  ```javascript
  const cities = [];

  fetch(endpoint)
    .then((blob) => blob.json())
    .then((data) => cities.push(...data));
  ```

  - 또한 데이터를 얻기 위해선, `__proto__` 인 `Response` 객체의 `.json()` 메서드를 사용한다.

  - `let` 이 아닌 `const` 로 선언한 cities 에 데이터를 넣을 땐, push 와 spread syntax 를 사용

- string to Regex

  - `'gi'` : global + insensitive(lower + upper)

  ```js
  function findMatches(wordToMatch, cities) {
    return cities.filter((place) => {
      const regex = new RegExp(wordToMatch, "gi");
      return place.city.match(regex) || place.state.match(regex);
    });
  }
  ```

- `change` vs `keyup`

  - `change` 는 input 에서 focues off 될 때 trigger 된다.
  - `keyup` 을 사용해야 매 번 타이핑할 때 trigger 할 수 있다.

- parse number with commas

  ```js
  function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  ```

---

### [Array cardio 2](./07%20-%20Array%20Cardio%20Day%202)

- `some()`, `every()`, `find()`, `findIndex()`

- remove element from array **with index**

  ```js
  const index = comments.findIndex((comment) => comment.id === 823423);
  comments.splice(index, 1);
  ```

---

### [HTML canvas](./08%20-%20Fun%20with%20HTML5%20Canvas)

- `mousedown`, `mousemove`, `mouseup`, `mouseout` 이벤트

- canvas 의 context 로 직선 그리기

  ```js
  function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke(); // draw

    // update last position
    [lastX, lastY] = [e.offsetX, e.offsetY];
  }
  ```

- HSL (for _hue_, saturation, lightness)
  - hue 는 0 ~ 360 사이의 값으로, 색상 지정 가능.
  - https://mothereffinghsl.com/

---

### [Dev Tools](./09%20-%20Dev%20Tools%20Domination)

console methods

- `log()`, `warn()`, `error()`, `info()`, `dir()`, `clear()`, `table()`

- `assert()`

  ```js
  console.assert(p.classList.contains("ouch"), "That is wrong!");
  ```

- `group(id) || groupCollapsed(id)` + `groupEnd(id)`
- `time(id)` + `timeEnd(id)`

---

### [Hold Shift](./10%20-%20Hold%20Shift%20and%20Check%20Checkboxes)

- attribute 로 element 를 선택할 때는 아래와 같다. 

  `selector[attr]` : attribute 를 가지는 elements

  `selector[attr=""]` : value 가 일치할 때 

  ````js
  const checkboxes = document.querySelectorAll('.inbox input[type="checkbox"]')
  ````

- `e.shiftKey : boolean` 

  shiftKey pressed 여부를 확인 가능 

- `<input type="checkbox>` 는 value 대신 `checkbox.checked` 를 이용한다. 

---

# [Custom Video Player](./11%20-%20Custom%20Video%20Player)

- `video` element

  `video.paused` 속성을 가진다. `video.playing` 은 없음..

  ```js
  function togglePlay() {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
  }
  
  // or 
  function togglePlay() {
      const method = video.pasued ? 'play' : 'pause'
      video[method]();
  }
  ```

  - `video.play()`, `video.pause()` 
  - `video.currentTime`, `video.duration` 

- `textContent` vs `innerText`

  - textContent 는 `<script>`, `<style>` 태그와 상관 없이 텍스트 값을 그대로 보여주고 
  - innterText 는 Element 내에 사용자에게 보여지는 그대로 텍스트를 가져온다. 따라서 `display: none` 속성을 가진 텍스트는 가져오지 않는다. 

- `flex-bais` CSS 속성을 이용하여 progress bar 표현 가능

  `e.offsetX` `element.offsetWidth` ... 



# [Key Sequence](12 - Key Sequence Detection)

연속된 키를 입력으로 받았을 때.. 

- `Array.splice(start, deleteCount, ...pushItems)`

  `Array.slice()` 와 다른 인자를 받는 것을 항상 주의하자. 

  ```js
  window.addEventListener('keyup', (e) => {
    pressed.push(e.key);
    pressed.splice(-secretCode.length - 1, pressed.length - secretCode.length);
  })
  ```

  - `pressed` 의 길이를 `secretCode` 의 길이 이하로 유지 가능하다.

