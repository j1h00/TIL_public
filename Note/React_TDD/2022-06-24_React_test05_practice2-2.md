# React test: 05  practice

>[인프런: 따라하며 배우는 리액트 테스트 by John Ahn](https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%85%8C%EC%8A%A4%ED%8A%B8)

- 위 강의를 듣고 정리한 내용입니다. 



04 practice 이어서.. 

### Order Page 

#### 04

1. 해야할 일 작성 => `여행 상품과 옵션의 개수에 따라 가격을 계산해주기 `

2. 테스트 작성 

   `userEvent.clear() ` 를 통해, `input` 혹은 `textarea` 의 텍스트를 제거 가능하다.  

   ```jsx
   test("update product's total when products change", async () => {
     render(<Type orderType="products" />);
   
     const productsTotal = screen.getByText("상품 총 가격:", { exact: false });
     expect(productsTotal).toHaveTextContent("0");
   
     const americaInput = await screen.findByRole("spinbutton", {
       name: "America",
     });
   
     userEvent.clear(americaInput);
     userEvent.type(americaInput, "1"); // input에 1 입력 
     expect(productsTotal).toHaveTextContent("1000");
   });
   ```

3. 테스트 실행 => Fail

4. 테스트에 대응하는 실제 코드 작성

   React Context API 를 사용하여 `priceState` 상태 관리! 

   ```js
   // Type.js  
   const ItemComponent = orderType === "products" ? Products : Options;
   ```

   

5. 테스트 실행 => Pass

