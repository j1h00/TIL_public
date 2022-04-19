# Java : Byte Code 조작

>[더 자바, 코드를 조작하는 다양한 방법 by 백기선](https://www.inflearn.com/course/the-java-code-manipulation/dashboard)

위 강의를 듣고 정리한 내용입니다. 

## Byte Code manipulation

```java
// Moja.java
public class Moja {
    
    public String pullOut() {
    	return "";
    }
}
```

```java
// Masulsa.java
public class Masulsa {
    
    public static void main(String[] args) {
    	System.out.println(new Moja().pullOut());
    }
}
```

`pullout()` 을 실행했을 때 토끼가 출력되도록 해보자 => 바이트 코드 조작이 필요하다. 

바이트코드 조작 라이브러리

-  ASM: https://asm.ow2.io/
-  Javassist: https://www.javassist.org/
-  ByteBuddy: https://bytebuddy.net/#/ 추천



```java
public class Masulsa {
    
    public static void main(String[] args) {
        try {
            new ByteBuddy().redefine(Moja.class)
                	.method(named("pullOut")).intercept(FixedValue.value("Rabbit!"))
                	.make().saveIn(new File("/Users/workspace/classloadersample/target/classes"))
        } catch (IOException e) {
            e.printStackTrace();
        }
           
//    	System.out.println(new Moja().pullOut());
    }
}
```



### Java agent 

Javaagent JAR 파일 만들기

- https://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html
- 붙이는 방식은 시작시 붙이는 방식 premain과 런타임 중에 동적으로 붙이는 방식 agentmain이 있다.
- Instrumentation을 사용한다.

Javaagent 붙여서 사용하기

- 클래스로더가 클래스를 읽어올 때 javaagent를 거쳐서 변경된 바이트코드를 읽어들여 사용한다.

- ByteBuddy 를 사용할 때는 컴파일 시 생성되는 클래스 파일 자체를 변경하는 것이었다면, 

  Java agent 는 클래스 로딩 시에 적용이 된다. (클래스 파일 자체가 바뀌지 않는다)

```java
public class MasulsaAgent {
    public static void premain(String agentArgs, Instrumentation inst) {
        new AgentBuilder.Default()
        .type(ElementMatchers.any())
        .transform((builder, typeDescription, classLoader, javaModule) -> builder.method(named("pullOut")).intercept(FixedValue.value("Rabbit!"))).installOn(inst);
        }
}
```



