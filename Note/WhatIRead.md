# What I Read 

Velog 인기글을 읽고, 좋은 내용은 정리해두고 싶어서 기록한다. 

## 2022-03-01 

>[Velog: [최적화] 웹 성능 최적화 방법 5분 완성](https://velog.io/@hsecode/%EC%B5%9C%EC%A0%81%ED%99%94-%EC%9B%B9-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B0%A9%EB%B2%95-5%EB%B6%84-%EC%99%84%EC%84%B1)
>
>[Velog: 나는 리액트를 어떻게 설계할 것인가](https://velog.io/@dahye-program/%EB%82%98%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%84%A4%EA%B3%84%ED%95%A0-%EA%B2%83%EC%9D%B8%EA%B0%80)

- good!



>[Velog: Typescript는 어떻게 공부해야 하나요?](https://velog.io/@teo/typescript)

### Javascript 

- javascript 는 간결한 문법을 가지면서도 타입 없이 객체지향도 함수형 프로그래밍도 가능한 `prototype 객체기반 함수형 동적타입 스크립트` 이라는 독특한 컨셉을 가진다. 
- javascript 의 부족한 문법을 개선하고, OOP 를 도입하기 위한 시도들이 있어왔다. 
- 그 중 가장 아쉬운 부분은 Static Typing 이다. 자잘한 오타로 인한 에러발생과 실행하면서 런타임이 되어서야 에러를 발견할 수 있다는 치명적인 문제!

### TypeScript

- MS 에서 자신들이 개발한 VSCode IDE 에서 제대로 동작할 수 있는 언어를 개발 
- 속도 문제?
  - IDE에서는 백그라운드에서 체크를 하고 실제 빌드시에는 타입체크를 하지 않으므로서 속도 문제를 해결.
  - Babel 과 결합하여 빌드 속도 상승. 이후엔 esbuild 의 등장으로 속도가 더이상 문제가 되지 않음 

- 라이브러리 에러 
  - any 타입 선언
  - 지금은 많은 라이브러리가 typescript 지원

>#### Typescript에 대한 자주하는 오해 3가지
>
>오해1. 타입스크립트는 정적 타입의 새로운 언어기에 러닝 커브가 높다.
>오해2. 타입스크립트를 하면 class와 객체지향 프로그래밍을 해야한다.
>오해3. 타입스크립트를 하면 협업은 좋으나 당장의 생산성은 떨어진다.

- Typescript 는 JavaScript 의 슈퍼셋이다. 
- 전혀 새로운 언어가 아니며, JS 에 `타입검사 + AutoComplete` 이 추가된 개념이라고 생각하자. 

### How?

1. 변수 선언과 함수 인자에 타입을 넣는 것부터 시작하자. 

```typescript
let name:string = "teo.yu"
let age:number = NaN
let isFrontEnd:boolean = true
let favorites:string[] = ["svelte", "rxjs", "vite", "adorableCSS"]

const doBest = (params:string) => {
 
}
```

2. 타입 선언보다는 가급적 자동추론을 사용하자 

```typescript
let bad:number = 10
let good = 10
```

3. 인터페이스를 선언해보자 

```typescript
intercae User {
  id:string
  name:string
  age:number
  email:string
}

const getUser(id:string):Promise<User> {
  ...
}
