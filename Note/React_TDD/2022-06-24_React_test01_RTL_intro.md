# React test: 01 What is test?

>[인프런: 따라하며 배우는 리액트 테스트 by John Ahn](https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%85%8C%EC%8A%A4%ED%8A%B8)

- 위 강의를 듣고 정리한 내용입니다. 

## Why test?

>[TDD?](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Development_common_sense#tdd)
>
>Test-Driven Development(TDD)는 매우 짧은 개발 사이클의 반복에 의존하는 소프트웨어 개발 프로세스이다. 우선 개발자는 요구되는 새로운 기능에 대한 자동화된 테스트케이스를 작성하고 해당 테스트를 통과하는 가장 간단한 코드를 작성한다. 일단 테스트 통과하는 코드를 작성하고 상황에 맞게 리팩토링하는 과정을 거치는 것이다. 말 그대로 테스트가 코드 작성을 주도하는 개발방식인 것이다.



#### 왜 어플리케이션을 TEST 해야 할까요?

아무리 코드를 잘 작성하더라고, 오류가 나기 마련이다. 더 안정적인 어플리케이션을 위해서 여러 방법으로 테스트가 필요하다. 

1. 디버깅 시간 단축

   만약 데이터가 잘못 나왔다면 그것이 UI의 문제인지 DB의 문제인지등 전부 테스트를 해봐서 찾아야 하는데 테스팅 환경이 구축되 어있다면 자동화 된 유닛 테스팅으로 특정 버그를 쉽게 찾아 낼 수 있다. 

2. 안정적인 어플리케이션

   많은 테스트 코드와 함께 작성된 코드의 어플리케이션은 안정적이다. 

3. 리팩토링 시간 단축, 추가 구현 용이 



## React Testing Library

Create React App 으로 리액트 앱 생성 시, 기본적으로 React Testing Library 를 사용할 수 있다. 

>[React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)

- 간단히 말하자면, RTL 은 리액트 컴포넌트를 테스트하는 가벼운 솔루션이다. 
- RTL 은 React 구성 요소 작업을 위한 API 를 추가하여 DOM Testing Library 위에 구축된다. 
  - DOM Testing Library 란 DOM 노드를 테스트하기 위한 매우 가벼운 솔루션이다. 

- Create React App 으로 생성된 프로젝트는 즉시 RTL 을 지원하며, 그렇지 않은 경우 npm 을 통해 추가할 수 있다. 

  ```bash
  npm install --save-dev @testing-library/react
  ```

RTL 은 에어비앤비에서 만든 Enzyme 을 대체하는 솔루션이다. 

- Enzyme 은 React 개발자에게 React 구성 요소의 내부를 테스트할 수 있는 유틸리티를 제공하는 동안, RTL 은 "React 구성 요소를 테스트하여 React 구성 요소를 완전히 신뢰하는 방법" 에 대해 질문한다. 

  - 구성 요소의 구현 세부 정보를 테스트하는 대신, RTL 개발자를 React 앱 사용자의 입장에 둔다.

- Enzyme : 구현 주도 테스트 (Implementation Driven Test)

  - ```html
    <p>
    Edit <code>src/App.js</code> and save to reload..
    </p>
    ```

    위 UI를 테스트할 때 주로  `<p>` 태그가 쓰였고 Edit 등의 문자가 들어갔다는것 을 테스트합니다. 그래서 만약 `<p>` 태그를 `<h2>` 태그로 바뀌면 에러가 날 것입니다.

- RTL : 행위 주도 테스트 (Behavior Driven Test)

  - Component 의 state 흐름, props 교환 등 사용자 입장에서 신경쓰지 않는 부분을 고려하지 않는다. 



### DOM 

> Document Object Model (문서 객체 모델) 은 XML, HTML 문서의 각 항목을 계층으로 표현하여 생성, 변형, 삭제할 수 있도록 돕는 인터페이스이다. 

#### 웹 페이지 빌드 과정 (Critical Rendering Path, CRP)

브라우저가 서버에서 페이지에 대한 HTML 응답을 받고 화면에 표시하기 전에 여러 단계가 존재한다. 

웹 브라우저가 HTML 문서를 읽고, 스타일을 입히고 뷰포트에 표시하는 과정 ![JavaScript | Critical Rendering Path](https://images.velog.io/images/eommoonjoo/post/061458db-0894-4ca0-8e55-bd0b362504e1/Critical-Rendering-Path.png)



1. 문서를 읽어들여서 그것들을 파싱하고, 어떤 내용을 페이지에 렌더링할 지 결정 

   (HTML, CSS) + JavaScript

2. Render Tree : 브라우저가 DOM 과 CSSOM 을 결합하고, 화면에 보이는 모든 콘텐츠와 스타일 정보를 모두 포함하는 최종 렌더링 트리를 출력
3. Layout : 브라우저가 페이지에 표시되는 각 요소의 크기와 위치를 계산
4. Paint: 브라우저는 레이아웃 결과를 확인하고 픽셀을 화면에 페인트 



![img](https://miro.medium.com/max/1400/0*rkjgCl-RSVTvRGgS)

정리하면, 

- DOM 은 HTML 이 브라우저의 렌더링 엔진에 의해 분석된, HTML 요소들의 구조화된 표현이다. 
- HTML 문서가 유효하지 않게 작성되었을 때는 브라우저가 올바르게 교정해준다. 
- DOM 은 자바스크립트에 의해 수정될 수 있지만, HTML 은 수정하지 않는다. 







