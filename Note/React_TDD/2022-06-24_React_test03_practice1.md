# React test: 03 practice

>[인프런: 따라하며 배우는 리액트 테스트 by John Ahn](https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%85%8C%EC%8A%A4%ED%8A%B8)

- 위 강의를 듣고 정리한 내용입니다. 



## Create simple Counter App 

TDD 원칙에 따라 테스트를 먼저 작성해보자.

### TDD cycle 01

1. 해야할 일 작성 => `Counter 는 0 부터 시작한다. `

2. 테스트 작성 

   ```js
   test("the counter starts at 0", () => {
     render(<App />);
     // screen object 를 이용해서 원하는 엘리먼트에 접근(ID로)
     const counterElement = screen.getByTestId("counter");
     // id 가 counter 인 엘리먼트의 텍스트가 0인지 테스트 
     expect(counterElement).toBe(0)
   });
   ```

3. 테스트 실행 => Fail 

4. 테스트에 대응하는 실제 코드 작성 

   ```js
   function App() {
     const [count, setCount] = useState(0);
   
     return (
       <div className="App">
         <header className="App-header">
           <h3 data-testid="counter">count</h3>
         </header>
       </div>
     );
   }
   ```

5. 테스트 실행 => Fail 

   counterElement 는 엘리먼트 자체를 뜻하므로, counterElement.textContent 와 비교해야함

6. 테스트에 대응하는 실제 코드 다시 작성 

   ```js
   test("the counter starts at 0", () => {
     render(<App />);
     // screen object 를 이용해서 원하는 엘리먼트에 접근(ID로)
     const counterElement = screen.getByTestId("counter");
     // id 가 counter 인 엘리먼트의 텍스트가 0인지 테스트
     expect(counterElement).toHaveTextContent(0);
   });
   ```

6. 테스트 실행 => Pass



### TDD cycle 02

1. 해야할 일 작성 => `+, - 버튼 두개를 생성한다. `

2. 테스트 작성 

   ```js
   test("minus button has correct text", () => {
     render(<App />);
     const buttonElement = screen.getByTestId("minus-button");
     expect(buttonElement).toHaveTextContent("-");
   });
   
   test("plus button has correct text", () => {
     render(<App />);
     const buttonElement = screen.getByTestId("plus-button");
     expect(buttonElement).toHaveTextContent("+");
   });
   ```

3. 테스트 실행 => Fail

4. 테스트에 대응하는 실제 코드 작성

   ```html
   <div className="App">
     <header className="App-header">
       <h3 data-testid="counter">{count}</h3>
       <div>
         <button data-testid="minus-button">-</button>
         <button data-testid="plus-button">+</button>
       </div>
     </header>
   </div>
   ```

5. 테스트 실행 => Pass

### TDD cycle 03 

#### FireEvent API 

>[Firing Event](https://testing-library.com/docs/dom-testing-library/api-events)

유저가 발생시키는 액션(이벤트)에 대한 테스트를 해야 하는 경우 사용 

1. 해야할 일 작성 => `+ 버튼을 누르면 카운터가 1로 변하게 된다. `

2. 테스트 작성 

   ```js
   test("When the + button is pressed, the counter changes to 1", () => {
     render(<App />);
     const buttonElement = screen.getByTestId("plus-button");
     // click plus-button
     fireEvent.click(buttonElement);
     const counterElement = screen.getByTestId("counter");
     expect(counterElement).toHaveTextContent(1);
   });
   
   ```

3. 테스트 실행 => Fail

4. 테스트에 대응하는 실제 코드 작성

   ```html
   <header className="App-header">
     <h3 data-testid="counter">{count}</h3>
     <div>
       <button data-testid="minus-button">-</button>
       <button
         data-testid="plus-button"
         onClick={() => setCount((count) => count + 1)}
       >
         +
       </button>
     </div>
   </header>
   ```

5. 테스트 실행 => Pass



### TDD cycle 04

1. 해야할 일 작성 => `on/off 버튼을 만드는데, 이 버튼에 파란색 스타일을 주겠다. `

2. 테스트 작성 

   ```js
   test("on/off button has blue color", () => {
     render(<App />);
     const buttonElement = screen.getByTestId("plus-button");
     expect(buttonElement).toHaveStyle({ backgroundColor: "blue" });
   });
   ```

3. 테스트 실행 => Fail

4. 테스트에 대응하는 실제 코드 작성

   ```html
   <div>
     <button
       data-testid="on/off-button"
       style={{ backgroundColor: "blue" }}
     >
       on/off
     </button>
   </div>
   ```

5. 테스트 실행 => Pass



### TDD cycle 05

1. 해야할 일 작성 => `on/off 버튼 클릭 시, +, - 버튼을 disabled 시킨다. `

2. 테스트 작성 

   ```js
   test.only("Prevent the +, - button from being pressed when the on/off button is clicked", () => {
     render(<App />);
     const onOffButtonElement = screen.getByTestId("on/off-button");
     fireEvent.click(onOffButtonElement);
     const plusButtonElement = screen.getByTestId("plus-button");
     const minusButtonElement = screen.getByTestId("minus-button");
   
     expect(plusButtonElement).toBeDisabled();
     expect(minusButtonElement).toBeDisabled();
   });
   ```

3. 테스트 실행 => Fail

4. 테스트에 대응하는 실제 코드 작성

   ```html
   function App() {
     const [count, setCount] = useState(0);
     const [disabled, setDisabled] = useState(false);
   
     return (
       <div className="App">
         <header className="App-header">
           <h3 data-testid="counter">{count}</h3>
           <div>
             <button
               data-testid="minus-button"
               onClick={() => setCount((count) => count - 1)}
               disabled={disabled}
             >
               -
             </button>
             <button
               data-testid="plus-button"
               onClick={() => setCount((count) => count + 1)}
               disabled={disabled}
             >
               +
             </button>
           </div>
           <div>
             <button
               data-testid="on/off-button"
               style={{ backgroundColor: "blue" }}
               onClick={() => setDisabled((prev) => !prev)}
             >
               on/off
             </button>
           </div>
         </header>
       </div>
     );
   }
   ```

5. 테스트 실행 => Pass

### etc

`test.only`, `test.skip`



## Query 사용 우선 순위 

>[About Queries - Priority](https://testing-library.com/docs/queries/about/#priority)

testing library 에서 추천하는 쿼리 사용 우선순위 

1. **Queries Accessible to Everyone** 

   Queries that reflect the experience of visual/mouse users as well as those that use assistive technology.

   - `getByRole` : used to query every element that is exposed in the [accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/AOM) 

     >[list of roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques#roles)

   - `getByLabelText` : really good for form fields
   - `getByPlaceholderText`
   - `getByText`
   - `getByDisplayValue`

2. **Semantic Queries**

   HTML5 and ARIA compliant selectors

   - `getByAltText`
   - `getByTitle`

3. **Test IDs**
   - `getByTestId` :  only recommended for cases where you can't match by role or text or it doesn't make sense



## userEvent 

fireEvent API 보다 useEvent API 를 사용하는게 더 좋은 방법이다. 

userEvent 는 fireEvent 를 사용해 만들어졌는데, 엘리먼트 타입에 따라서 Label 이나 checkbox, radio 를 클릭했을 때 그 엘리먼트 타입에 맞는 더욱 적절한 반응을 보여준다. 



 



