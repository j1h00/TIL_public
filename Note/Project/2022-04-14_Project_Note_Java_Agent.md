# Project Note: Java Agent 

> [Guide to Java Instrumentation](https://www.baeldung.com/java-instrumentation)
>
> [jvm-monitoring-agent](https://github.com/toptal/jvm-monitoring-agent/blob/master/src/com/toptal/jvm/monitoring/Agent.java)

## Java Agent

What is Java Agent ?

- In general, a java agent is just a specially crafted jar file.
- It utilizes the [Instrumentation API](https://docs.oracle.com/en/java/javase/11/docs/api/java.instrument/java/lang/instrument/Instrumentation.html) that the JVM provides to alter existing byte-code that is loaded in a JVM.
  - Instrumentation API 를 이용하여, JVM 에 load 된 byte-code 를 수정 가능하게 한다. 
  - `transform` 메서드를 통해 이미 정의된 class 를 변경하는 것도 가능하다.  

`premain` & `agentmain` 을 구현하여 각각 정적, 동적 load 시에 사용 가능하다. 



## jvm-monitoring-agent 

과제 요구사항과 비슷한 Java agent 오픈소스 코드를 분석 

`java.util.TimerTask` 

- [https://docs.oracle.com/javase/8/docs/api/java/util/TimerTask.html](https://docs.oracle.com/javase/8/docs/api/java/util/TimerTask.html)
- [https://sangwoo0727.github.io/java/JAVA-36_timertask/](https://sangwoo0727.github.io/java/JAVA-36_timertask/)
- implements `Runnable` interface

`Agent` 

- extends TimerTask
- Timer 가 실행할 task 를 정의한 클래스
- Timer 인스턴스 생성 시에 boolean 인자를 매개변수로 지정 ⇒ 데몬 스레드

```java
public class Agent extends TimerTask {
		// ... 
		private final Timer                     timer          = new Timer(NAME, true);
	  private final WeakHashMap<Thread, Long> blockedThreads = new WeakHashMap<>()
		
        // premain method for static load 
		public static void premain(String stringArgs) {
				Agent agent = new Agent(stringArgs);
				agent.start(); 
		}
	
    	// agent TimerTask thread start 
		public void start() {
				// ... 
				run() 
		}
	
    	// start => run 
		@Override 
		public void run() {
            // set loop start - end time
            
            // checkthreads 
            boolean savedDump = checkThreads();

            if (blockedToLong)
		        msg += " - threads are blocked";
		    if (savedDump) {
		        lastSave = loopStartTime;
		        msg += " - saved dump: "+dumpFileName;
		    }
            if (blockedToLong || savedDump) {
		        log(msg);
            }
		}
	
		private void log(String msg) {
	      if (debug)
	          System.err.println("[" + NAME + "] " + msg);
	  }
	
		// check Threads and save dump 
		// check Blocked threads
		private boolean checkThreads() {
	      Map<Thread, StackTraceElement[]> threads = Thread.getAllStackTraces();
	
	      cleanUnBlockedThreads();
	      addBlockedThreads(threads.keySet());
	      checkBlockedToLong();
	      
	      return blockedToLong && shouldBeSaved() && saveThreadsDump(threads);
	  }
	
    	// printThreadDump to txt
		private boolean saveThreadsDump(Map<Thread, StackTraceElement[]> threads){
	      dumpFileName = root_path + "/threads_dump_" + loopStartTime + ".txt";
	
	      try (PrintStream stream = new PrintStream(dumpFileName)) {
	          printThreadsDump(stream, threads);
	          return true;
	      } catch (FileNotFoundException ex) {
	          log(ex.toString());
	          return false;
	      }
	  }
	
		
		private void printThreadsDump(PrintStream stream, Map<Thread, StackTraceElement[]> threads) {
	      // Thread 개수와 Blocked 개수 
          stream.format(
	          "#Threads: %d, #Blocked: %d%n%n",
	          threads.size(),
	          blockedThreads.size()
	      );

          // 모든 Thread 에 대해 Id, Name, Daemon, Priority, State 출력!
	      threads.forEach((thread, stack) -> {
	          stream.format(
	              "Thread:%d '%s' %sprio=%d %s%n",
	              thread.getId(),
	              thread.getName(),
	              thread.isDaemon() ? "daemon " : "",
	              thread.getPriority(),
	              thread.getState()
	          );
	          for (StackTraceElement line: stack)
	              stream.println("        " + line);
	          stream.println();
	      });
	  }
}
```



- 위 jvm-monitoring-agent 의 출력 포맷은 fastthread 에서 parsing 이 불가하다. 

- fastthread 나 다른 분석 툴에서 사용 가능하도록, 흔히 쓰이는 jstack 이나 visualVM 의 format 을 맞춰서 출력해보면 좋을 것 같다.

    - jvm-monitoring-agent FORMAT
      
        ```java
        Thread:381 'Thread-371' prio=5 BLOCKED
                com.toptal.Synchronized.run(Unknown Source)
                com.toptal.Nested.run(Unknown Source)
                com.toptal.Nested.run(Unknown Source)
                com.toptal.Nested.run(Unknown Source)
        				//... 
        ```
        
    - jstack FORMAT
      
        ```java
        2018-06-19 16:44:44
        Full thread dump Java HotSpot(TM) 64-Bit Server VM (10.0.1+10 mixed mode):
        
        Threads class SMR info:
        _java_thread_list=0x00000250e5488a00, length=13, elements={
        0x00000250e4979000, 0x00000250e4982800, 0x00000250e52f2800, 0x00000250e4992800,
        0x00000250e4995800, 0x00000250e49a5800, 0x00000250e49ae800, 0x00000250e5324000,
        0x00000250e54cd800, 0x00000250e54cf000, 0x00000250e54d1800, 0x00000250e54d2000,
        0x00000250e54d0800
        }
        
        "Reference Handler" #2 daemon prio=10 os_prio=2 tid=0x00000250e4979000 nid=0x3c28 waiting on condition  [0x000000b82a9ff000]
           java.lang.Thread.State: RUNNABLE
            at java.lang.ref.Reference.waitForReferencePendingList(java.base@10.0.1/Native Method)
            at java.lang.ref.Reference.processPendingReferences(java.base@10.0.1/Reference.java:174)
            at java.lang.ref.Reference.access$000(java.base@10.0.1/Reference.java:44)
            at java.lang.ref.Reference$ReferenceHandler.run(java.base@10.0.1/Reference.java:138)
        
           Locked ownable synchronizers:
            - None
        
        "Finalizer" #3 daemon prio=8 os_prio=1 tid=0x00000250e4982800 nid=0x2a54 in Object.wait()  [0x000000b82aaff000]
           java.lang.Thread.State: WAITING (on object monitor)
            at java.lang.Object.wait(java.base@10.0.1/Native Method)
            - waiting on <0x0000000089509410> (a java.lang.ref.ReferenceQueue$Lock)
            at java.lang.ref.ReferenceQueue.remove(java.base@10.0.1/ReferenceQueue.java:151)
            - waiting to re-lock in wait() <0x0000000089509410> (a java.lang.ref.ReferenceQueue$Lock)
            at java.lang.ref.ReferenceQueue.remove(java.base@10.0.1/ReferenceQueue.java:172)
            at java.lang.ref.Finalizer$FinalizerThread.run(java.base@10.0.1/Finalizer.java:216)
        
           Locked ownable synchronizers:
            - None
        
        "Signal Dispatcher" #4 daemon prio=9 os_prio=2 tid=0x00000250e52f2800 nid=0x2184 runnable  [0x0000000000000000]
           java.lang.Thread.State: RUNNABLE
        
           Locked ownable synchronizers:
            - None
        ```
        
        ![Untitled](Java%20Agent%2028cf8/Untitled.png)
        
    - Java visualVM FORMAT by 지호님
      
        ```java
        2022-04-14 16:22:06
        Full thread dump Java HotSpot(TM) 64-Bit Server VM (25.311-b11 mixed mode):
        
        "Inactive RequestProcessor thread [Was:VisualVM Shared RequestProcessor/null]" #41 daemon prio=1 os_prio=-2 tid=0x000002660138f800 nid=0x52ac in Object.wait() [0x00000078d80ff000]
           java.lang.Thread.State: TIMED_WAITING (on object monitor)
                at java.lang.Object.wait(Native Method)
                at org.openide.util.RequestProcessor$Processor.run(RequestProcessor.java:1977)
                - locked <0x00000000f3eac0c0> (a java.lang.Object)
        
           Locked ownable synchronizers:
                - None
        
        "VisualVM Shared RequestProcessor" #40 daemon prio=1 os_prio=-2 tid=0x000002660138e800 nid=0xe80 runnable [0x00000078d66fe000]
           java.lang.Thread.State: RUNNABLE
                at sun.tools.attach.WindowsVirtualMachine.enqueue(Native Method)
                at sun.tools.attach.WindowsVirtualMachine.execute(WindowsVirtualMachine.java:96)
                at sun.tools.attach.HotSpotVirtualMachine.executeCommand(HotSpotVirtualMachine.java:261)
                at sun.tools.attach.HotSpotVirtualMachine.remoteDataDump(HotSpotVirtualMachine.java:218)
                at org.graalvm.visualvm.attach.AttachModelImpl.takeThreadDump(AttachModelImpl.java:123)
                - locked <0x00000000d165c2d8> (a org.graalvm.visualvm.attach.AttachModelImpl)
                at org.graalvm.visualvm.jvm.JVMImpl.takeThreadDump(JVMImpl.java:439)
                at org.graalvm.visualvm.threaddump.impl.ThreadDumpProvider$1.run(ThreadDumpProvider.java:83)
                at org.openide.util.RequestProcessor$Task.run(RequestProcessor.java:1418)
                at org.netbeans.modules.openide.util.GlobalLookup.execute(GlobalLookup.java:45)
                at org.openide.util.lookup.Lookups.executeWith(Lookups.java:278)
                at org.openide.util.RequestProcessor$Processor.run(RequestProcessor.java:2033)
        
           Locked ownable synchronizers:
                - None
        
        "Inactive RequestProcessor thread [Was:VisualVM Shared RequestProcessor/org.graalvm.visualvm.tools.jmx.CachedMBeanServerConnectionFactory$SnapshotInvocationHandler$2]" #39 daemon prio=1 os_prio=-2 tid=0x000002660138b000 nid=0x18cc in Object.wait() [0x00000078d65ff000]
           java.lang.Thread.State: TIMED_WAITING (on object monitor)
                at java.lang.Object.wait(Native Method)
                at org.openide.util.RequestProcessor$Processor.run(RequestProcessor.java:1977)
                - locked <0x00000000f3eedc20> (a java.lang.Object)
        
           Locked ownable synchronizers:
                - None
        
        // ... 
        
        "VM Thread" os_prio=2 tid=0x0000026678516800 nid=0x1d34 runnable 
        
        "GC task thread#0 (ParallelGC)" os_prio=0 tid=0x0000026665161000 nid=0x31f0 runnable 
        
        "GC task thread#1 (ParallelGC)" os_prio=0 tid=0x0000026665162800 nid=0x2704 runnable 
        
        "GC task thread#2 (ParallelGC)" os_prio=0 tid=0x0000026665163800 nid=0x4878 runnable 
        
        "GC task thread#3 (ParallelGC)" os_prio=0 tid=0x0000026665165000 nid=0x2228 runnable 
        
        "GC task thread#4 (ParallelGC)" os_prio=0 tid=0x0000026665167800 nid=0x4cb8 runnable 
        
        "GC task thread#5 (ParallelGC)" os_prio=0 tid=0x0000026665169000 nid=0x229c runnable 
        
        "GC task thread#6 (ParallelGC)" os_prio=0 tid=0x000002666516c000 nid=0x1fd0 runnable 
        
        "GC task thread#7 (ParallelGC)" os_prio=0 tid=0x000002666516d000 nid=0x1f9c runnable 
        
        "GC task thread#8 (ParallelGC)" os_prio=0 tid=0x000002666516e000 nid=0x204c runnable 
        
        "GC task thread#9 (ParallelGC)" os_prio=0 tid=0x000002666516f000 nid=0x14c runnable 
        
        "VM Periodic Task Thread" os_prio=2 tid=0x000002667a9ab800 nid=0x614 waiting on condition 
        
        JNI global references: 941
        ```