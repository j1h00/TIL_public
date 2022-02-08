# Project Note : SpringBoot JPA

## JPA

표준 ORM (Object Relational Mapping) (객체 관계 매핑)

데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법  



1. @Entity 

2. JpaRepository 



### DB 설계 

### application.properties

```java
spring.datasource.url = jdbc:h2:mem:testdb
    
spring.jpa.generate-ddl=true
spring.spa.hibernate.ddl-auto=update
    
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.lebel.org.hibernate.type.descriptor.sql.BasicBinder=trace
```

### Relational Mapping

1. 다중성

@OneToOne

@OneToMany

@ManyToOne

@ManyToMany



2. 방향성

@JoinColumn 

양방향은 JPA 에서 지양하자!



3. 연관 관계의 주인 

@OneToMany(mappedBy = "boardFk")

// @joinColumn (name="boardFK")

양방향일 경우 어떤 테이블 기준으로 데이터를 삭제하면 그것에 관련된 데이터들을 다 삭제할 것인가?

FK 키 관리 주인을 설정해준다. 

@ManyToOne 은 항상 주인이다. 



### JpaRepository

Read : find**** 로 시작

Delete delete**** 로 시작

Create: save

Update: 객체 조회 후 값 변경 그리고 다시 save

```java

```

