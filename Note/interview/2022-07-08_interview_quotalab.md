# interview questions : quotalab 02

## 쿼타랩 직무 심화  



## 프로젝트

>자기소개 

>비전공자인데, SSAFY 에 와서 처음 프로그래밍을 접한건가요?

>프로젝트하면서 기술적으로 어려웠던 점

>최근에 관심있게 보고 있는 기술이나 트렌드 

>프론트엔드 직무를 선택하게 된 이유가 있나요

>JRStock 주식에 관한 서비스를 기획부터 진행했는데, 어려웠던 점이 있는지  
>
>8가지 전략과 커스터마이징이 무엇을 뜻하나요?

>프로젝트 우수상 두 개를 받았는데, 어떤 이유에서 받았다고 생각하는지와 자신이 기여한 역할에 대해 말해주세요

>프론트엔드 개발자에 대해 설명해주세요

## 기술 

>Javascript 를 사용하면서 어려웠던 부분이 있나요?

>자바스크립트에서 비동기 처리를 할 수 있는 방법에 대해 말해주세요 
>
>callback, promise, async & await 각각의 차이가 뭔가요
>
>async & await 이 가독성을 높여준다는게 어떤 뜻인가요?

- 가독성 좋게 비동기 처리를 동기 처리처럼 동작하도록 구현할 수 있다. 
  - 프로미스의 후속 처리 메서드 없이 마치 동기 처리처럼 프로미스가 처리 결과를 반환하도록 구현할 수 있다. 
  - 에러 핸들링에서, `.catch()` 문을 사용하지 않고, `try / catch` 를 통해 에러 처리



>함수 컴포넌트는 사실상 리렌더 되면서 다시 실행되는 것과 마찬가지인데, state 가 어떻게 유지되나요?

[Deep dive: How do React hooks really work?](https://www.netlify.com/blog/2019/03/11/deep-dive-how-do-react-hooks-really-work/)

=> may be `closure`

>Javascript 에서 어떤 함수의 데이터? 상태? 를 유지하기 위해 사용하는 방법에 대해 아나요?  

closure?

>hook 에 대해 알고 있나요? 
>
>hook 을 왜 사용하나요?

함수 컴포넌트에선, state 와 라이프사이클 API 의 사용이 불가능했는데, `v16.8` 업데이트 이후 hooks 를 적용하여 해결하였다. 



>지후님이 컴포넌트를 작성할 때 고려하는 게 있나요?
