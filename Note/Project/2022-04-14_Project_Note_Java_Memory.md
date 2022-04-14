# Project Note: Java Memory 

Java 기본 복습하기

> [[JAVA/자바] 메모리 구조(static, stack, heap)](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=heartflow89&logNo=220954420688)
> 

### static area

- 하나의 JAVA 파일은 크게 **필드(field)**, **생성자(constructor)**, **메서드(method)**로 구성
- 필드 부분에서 선언된 변수(전역변수)와 정적 멤버변수(static이 붙은 자료형)의 데이터 값이 저장되는 공간
- Static 영역의 데이터는 프로그램의 시작부터 종료가 될 때까지 메모리에 남아있게 된다.
    - 따라서 프로그램이 종료될 때까지 어디서든 사용이 가능하다.
    - 그러나 무분별하게 사용하다 보면 메모리가 부족할 우려가 있다!
- static 필드와 메서드
    - 몇 개의 인스턴스를 생성하든, 클래스 당 1개의 값만을 가지며, 공유가 가능하다. 또한 인스턴스를 생성하지 않고 클래스로 바로 접근이 가능하다.
    - 정적 메서드에서는 정적 필드만 사용 가능하고, 정적 메서드만 호출이 가능하며, this 키워드를 사용할 수 없고 메서드 오버라이딩이 불가능하다.

### Stack area

- 메서드 내에서 정의하는 기본 자료형 (int, double, byte, long, boolean 등) 에 해당되는 지역변수 (매개 변수 및 블럭문 내 변수 포함) 의 데이터 값이 저장되는 공간

```java
public class StackAreaEx {
	public static void main(String[] args) {
		int a = 5;	a = 4;	a = 3;	a = 2;
		System.out.println(a);
		for(int i=0; i<5; i++){
		}
	//	System.out.println(i); 컴파일 에러
	}
}
```

- a 라는 변수는 main 메서드가 호출될 때 stack 영역에 할당되고, 종료 시 해제된다.
- Stack 영역은 LIFO 구조를 갖고 변수에 새로운 데이터가 할당되면 이전 데이터는 지워진다.
- 또한 for 문 내에 정의한 `int i`  는 지역 변수이므로 for 문의 종료와 함께 Stack 영역에서 해제되어 출력 시 에러를 발생시킨다.

### Heap area

- 참조형(Reference Type) 의 데이터 타입을 갖는 객체(인스턴스), 배열 등의 데이터 값이 저장되는 공간
- 변수(객체, 객체 변수, 참조 변수) 는 Stack 영역의 공간에서 new 연산자를 통해, 실제 데이터가 저장된 Heap 영역의 참조값(reference value, 해시코드 / 메모리에 저장된 주소를 연결해주는 값) 을 리턴받는다.
- 다시 말하면, 실제 데이터를 갖고 있는 Heap 영역의 참조 값을 Stack 영역의 객체가 갖고 있다.
- Heap 에 저장된 데이터는 더 이상 사용이 불필요하면 JVM 의 GC 에 의해 자동으로 해제된다.

### new

- new 는 클래스 타입의 인스턴스(객체) 를 생성해주는 역할을 한다.
- 위에서 설명했듯, Heap 영역에 데이터를 저장할 공간을 할당 받고, 그 공간의 참조값을 객체에게 반환하여 주고, 마지막으로 생성자를 호출하게 된다.
  
    ![Untitled](2022-04-14_Project_Note_Java_Memory.assets/Untitled.png)
    

### 지역 변수 / 전역 변수

- 필드에서 선언된 변수는 지역 변수와는 다르게 값을 할당하지 않아도 자동으로 초기값을 갖는다.
- 메서드 내에서, 지역 변수가 전역 변수보다 우선 순위가 높다.
    - 필드의 값을 출력하기 위해선 `this` 를 사용하면 된다.

### 접근 제한자 Access Modifier

- 클래스를 제한하여 다른 패키지에서 클래스의 접근을 막거나,
- 생성자를 제한하여 클래스에서 객체 생성을 막거나,
- 필드 및 메소드를 제한하여 중요한 정보를 갖고 있는 필드나 메서드의 접근을 막을 수 있다.
- 은닉화 / 캡슐화

![Untitled](2022-04-14_Project_Note_Java_Memory.assets/Untitled%201.png)

- default 는 접근 제어자가 없는 경우를 의미한다.