# Project Note : Java Thread

>[[JAVA] Thread 1 - 자바의 쓰레드](https://velog.io/@tomato2532/JAVA-Thread-1-%EC%9E%90%EB%B0%94%EC%9D%98-%EC%93%B0%EB%A0%88%EB%93%9C)
>
>[[JAVA] Thread 2 - JVM 쓰레드 스케줄링](https://velog.io/@tomato2532/JAVA-Thread-2-JVM-%EC%93%B0%EB%A0%88%EB%93%9C-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81)
>
>[[JAVA] Thread 3 - 공유자원, 쓰레드 동기화](https://velog.io/@tomato2532/JAVA-Thread-3-%EA%B3%B5%EC%9C%A0%EC%9E%90%EC%9B%90-%EC%93%B0%EB%A0%88%EB%93%9C-%EB%8F%99%EA%B8%B0%ED%99%94)

## Java Thread

### intro

**Concurrent vs Parallel - 동시성과 병렬성**

- 자바의 쓰레드는 Concurrent하게 동작 
- Concurrent 는 논리적으로 여러 작업을 동시에 처리하는 멀티쓰레드 동작이지만 여러 쓰레드가 물리적으로 동시에 실행되지는 않고, 실제 동작은 여러 쓰레드의 수행시간을 쪼개어 동작한다. 
- Parallel도 어떤 작업을 여러 작업으로 쪼개고 동시에 수행하는 것을 말하는데, Parrallel은 Concurrent와 다르게 물리적으로 동시에 여러쓰레드를 병렬적으로 수행하는 것을 말한다. 

**Thread**

- 프로세스를 구성하는 세부 실행단위(Unit)
- 자바는 JVM을 통해 멀티 쓰레드를 구성하여 concurrent 하게 동작하여 동시에 여러 작업을 수행 가능 
- 하지만 동시에 수행되는 쓰레드의 수행 순서는 보장하지 않는다. 

- [OS04: Threads](https://github.com/j1h00/TIL_public/blob/master/Note/CS/OS/2021-12-10_OS04_Thread.md) 참고 

### 주요 메서드

`start()`

- 쓰레드를 스케줄러에 포함시킨다. 
- 스케줄러에 포함된 쓰레드는 쓰레드 큐 내에서 runnable 상태로 대기하다가, 수행 차례가 되면 `run()` 을 호출하여 동작을 수행한다. 
- Terminate 되었거나, Waiting 인 상태이면 `start()` 를 호출할 수 없다. 

`run()`

- 스케줄러 내에서 실제 동작하는 부분이며, `Thread` 클래스는 `Runnable` 인터페이스의 `run()` 메서드를 구현했다. 
- 쓰레드의 `start()` 를 통하지 않고,  `run()` 을 직접 호출하면, 스케줄러에 포함되지 않고 일반 메서드 호출한 것 처럼 동작한다. 

`sleep()` 

- Waiting pool 로 보내 대기 상태에 들어간다. 
- ms 단위 시간을 변수로 받아 해당 시간만큼 대기시킨다. 
- interrupt 가 발생하면 다시 Runnable 상태가 된다. 

`join()`

- ms 단위 시간을 변수로 받으며, `join()` 을 호출한 쓰레드는 호출된 쓰레드가 수행이 완전히 종료되고, 매개로 받은 대기 시간만큼 대기한 후 다시 수행한다. 
- 호출 시 쓰레드는 Waiting pool 로 이동했다가, 호출된 쓰레드가 Terminate 되면 다시 Runnable 상태가 된다. 

`yeild()` 

- 현재 Running 상태인 쓰레드(`yeild()` 메서드를 호출한 쓰레드) 가 Running 상태를 양보한다. 
- 호출한 쓰레드는 Runnable 큐로 이동한다. 



### 구현

자바에서 쓰레드를 구현하는 방법은 두 가지이다.

1. `java.lang.Thread` 클래스 상속



2. `java.lang.Runnable` 인터페이스 구현

   - `Runnable` 인터페이스를 구현한 객체를 Thread 객체 생성자의 매개변수로 넘겨야 한다. 

   ```java
   public class myRunnable implements Runnable{
       @Override
       public void run(){
       //... do something...
       }
   }
   
   //...
   public static main(String[] args){
       myRunnable mr = new myRunnable();
       Thread myThread = new Thread(mr);
       myThread.start();
   }
   ```



## JVM Thread Scheduling

### Thread State

![img](https://velog.velcdn.com/images%2Ftomato2532%2Fpost%2F0022530f-4d0c-4013-b241-1c9a30a273f7%2FThreadScheduling.png)

Process 의 State 와 같은 상태를 가진다. 

1. New 

   각 쓰레드 객체의 `start()` 메서드를 통해 동작시키게 되면 해당 쓰레드 객체는 JVM의 쓰레드 스케줄링 대상이 되며 **Runnable** 상태가 된다. 한 번 New 상태에 돌입한 쓰레드는 다시 New 상태가 될 수 없다.

2. Runnable

   Runnable 큐에 대기하며, JVM은 각 쓰레드의 우선순위에 따라서 **Running** 상태로 만들어 쓰레드를 동작시킨다. 

3. Running

   `run()` 메서드를 호출하여 실제 동작을 수행하며, `run()` 이 종료되면 Terminate 상태가 된다. 

   중간에 I/O 호출, `sleep()`, `join()` 등의 인터럽트가 발생하면 Waiting Pool 로 이동하여 대기한다. 

   또한 해당 쓰레드의 `run()` 메소드의 수행이 길어지거나 `yield()` 메서드가 수행되게되면 JVM은 해당 쓰레드를 다시 **Runnable** 상태로 옮긴다. 

4. Waiting

   Running 상태의 쓰레드가 I/O 호출, `sleep()`, `join()` 메서드에 의해 대기해야 할 경우 Waiting pool 로 이동

   위 해당 조건이 끝나거나 인터럽트가 발생하면 다시 Runnable 로 이동

5. Terminate

   `run()` 메서드 수행이 종료된 상태이며, 쓰레드가 종료된다. 

   한 번 Terminate 된 쓰레드 객체는 다시 `start`() 메서드로 호출하여 스케줄러에 포함시킬 수 없다. 

### Priority 

JVM 은 Runnable 상태의 쓰레드들의 우선순위 값을 확인하여 Running 상태에 돌입할 수 있는 기회를 부여한다. 

`Thread` 클래스 내에서 아래와 같이 기본 우선 순위를 제공하고 있다.  

```java
/**
     * The minimum priority that a thread can have.
 */
public final static int MIN_PRIORITY = 1;

/**
 * The default priority that is assigned to a thread.
 */
public final static int NORM_PRIORITY = 5;

/**
 * The maximum priority that a thread can have.
 */
public final static int MAX_PRIORITY = 10;
```

`setPriority()` 를 통해 1 ~ 10 사이의 값을 우선순위로 부여할 수 있다. 

```java
public final void setPriority(int newPriority) {
    ThreadGroup g;
    checkAccess();
    if (newPriority > MAX_PRIORITY || newPriority < MIN_PRIORITY) {
        throw new IllegalArgumentException();
    }
    if((g = getThreadGroup()) != null) {
        if (newPriority > g.getMaxPriority()) {
            newPriority = g.getMaxPriority();
        }
        setPriority0(priority = newPriority);
    }
}

public final int getPriority() {
    return priority;
}
```

## Thread synchronize

레퍼런스 타입으로 선언된 변수는 여러 개의 쓰레드에서 동시에 접근 가능한데,  이를 공유 자원이라고 한다. 

공유 자원에 접근할 시, 쓰레드의 수행 순서가 정해지지 않았거나 하는 경우 의도치 않은 결과를 얻기 쉽다. 

따라서 멀티쓰레드 환경에서는 `synchronized` 를 통한 동기화로 공유자원에 대한 임계영역 (critical section) 설정이 필요하다. 

공유자원에 대하여 원자성을 확보하기 위해 `synchronized` 를 사용할 때, `synchronized` 메서드와 `synchronized` 블럭을 사용할 수 있다. 

### synchronized method 

메서드 제어자에 `synchronized`  키워드 작성을 통해 임계 영역 설정할 수 있다. 

`synchronized` 메서드가 호출되면 

1. 해당 메서드의 객체는 호출한 쓰레드에게 Lock Flag를 전달하며

2. 해당 쓰레드 외에 공유객체를 필요로 하는 쓰레드는 **Running** 상태가 될 수 없으며,

3. Lock Flag 가 반납될 때까지 Waiting Pool의 Lock pool에서 대기하게 됩니다.

