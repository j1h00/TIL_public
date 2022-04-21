# Project Note: Maven dependency

> [How to add dependency to Ant project](https://stackoverflow.com/questions/26650590/how-to-add-dependency-to-ant-project)

Ant 프로젝트를 빌드 시, dependecy 를 추가하기 위해서는 ivy 라는 또 다른 패키지 관리자가 필요했다. 

따라서 kafka-client dependecy 를 쉽게 추가하기 위해, 기존의 Ant 프로젝트를 Maven 프로젝트로 변경하고자 하였다. 

> [How to convert Ant project to Maven project](https://stackoverflow.com/questions/4029501/how-to-convert-ant-project-to-maven-project)

이를 위해 위 글을 참고하여, 기존의 `build.xml` 의 내용을 `pom.xml` 로 옮기고, 소스파일을 `src/main/java` 의 하위로 옮겨야했다.

 이후, kafka-client dependency 를 추가하고, plugin 을 이용하여 manifest 를 작성하였다. 

> [Java - Javaagent](https://ncucu.me/144)

위 글을 참고하여 아래처럼  `maven-jar-plugin` 을 추가하였다. 

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <configuration>
        <archive>
            <index>true</index>
            <manifest>
                <addClasspath>true</addClasspath>
                <classpathPrefix>lib</classpathPrefix>
            </manifest>
            <manifestEntries>
                <mode>development</mode>
                <url>${project.url}</url>
                <key>value</key>
                <Premain-Class>com.toptal.jvm.monitoring.Agent</Premain-Class>
                <Can-Redefine-Classes>true</Can-Redefine-Classes>
                <Can-Retransform-Classes>true</Can-Retransform-Classes>
            </manifestEntries>
        </archive>
    </configuration>
</plugin>
```

이후 `mvn package` 명령어를 통해 `.jar` 파일을 얻는데 까지는 성공했으나, 이후 javaagent 의 runtime 단계에서 에러가 발생했다. 

kafka-client 패키지의 클래스를 찾을 수 없다는 에러였는데, 빌드 과정에서 dependency 가 제대로 추가되지 않은 것으로 보였다. 

> [How can I create an executable JAR with dependencies using Maven?](https://stackoverflow.com/questions/574594/how-can-i-create-an-executable-jar-with-dependencies-using-maven)

위 글에 해결 가능한 여러가지 방법이 소개되어 있었지만, 두 가지를 시도해서 실패했다. 

1. `maven-jar-plugin` 과 `maven-dependency-plugin` 를 사용하여 dependency 경로를 설정해주어 찾도록 한다. 
2. `maven-assembly-plugin` 으로 한 번에 해결한다. 

그러나 `premain` 관련한 manifest 가 작성되어 있어야 하는 java agent 의 특성상 동일한 케이스를 찾기가 어려웠고, 잘 동작하지 않아 시간을 많이 투자했다. 

결국 stackoverflow 에 처음으로 질문을 등록하게 되었다.. 

>[`java.lang.NoClassDefFoundError` from javaagent built by `maven package`](https://stackoverflow.com/questions/71939150/java-lang-noclassdeffounderror-from-javaagent-built-by-maven-package)

이게 답변이 달릴까 싶었는데, 다행히 친절한 답변이 달렸다.. 

답변에 의하면 java agent 는 `-jar` 옵션으로 실행되지 않기 때문에, dependency 가 자동으로 추가되지 않는 것으로 보였다. 맞는지는 한 번 더 확인해봐야 할 것으로 보인다. 

2022-04-21 이어서.. 

답변을 상세히 확인해보니, Java `Instrumentation` API 를 사용해보라는 내용이 있어 시도하였다. 

>[Adding jar file to instrumentation path](https://stackoverflow.com/questions/38213651/adding-jar-file-to-instrumentation-path)

- Intrumentation 객체의 `appendToSystemClassLoaderSearch `메서드를 이용하면 java agent 실행 시 system class loader 에 의해 JAR 파일이 정의되도록 할 수 있다.. 
- 정확한 구동 방식은 이해를 못했지만, 동작은 잘 되었다. 

또 다른 방법으로 `maven-dependency-plugin` 을 등록하고 `mvn install dependency:copy-dependencies` 명령어를 실행하면, 자동으로 dependency 폴더가 생성되고 그 안에 의존하는 `.jar` 파일이 모두 복사된 것을 확인할 수 있다.  

`maven-jar-plugin` 설정 시 classpath prefix 를 lib 으로 설정해두었기 때문에,  모든 `.jar` 파일들은 dependency 가 아니라 lib 경로에 존재해야 했다. 그러나 `maven-dependency-plugin` 설정 시 output directory 를 lib 으로 작성해도 dependency 폴더만 생성되어, 어쩔 수 없이 수동으로 dependency 폴더 이름을 lib 으로 변경하였다.  

그 이후 약간의 문제가 있었지만, agent 가 잘 동작하였다. 

- `Failed to load class org.slf4j.impl.StaticLoggerBinder`  라는 slf4j 관련 warning message 가 출력되는데, 원인은 알 수 없었다.. 

   

