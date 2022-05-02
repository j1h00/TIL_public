# Project Note: Java json-simple

>https://code.google.com/archive/p/json-simple/
>
>dependency | https://mvnrepository.com/artifact/com.googlecode.json-simple/json-simple/1.1.1

Kafka 메시지 큐에 JSON 형식의 데이터를 보내기 위해 json-simple 라이브러리를 사용함.

`JSONObject`, `JSONArray`, `JSONParser` 3가지만 알면 되어 매우 간단하고, 가벼워서 사용하기 좋은 것 같았다. 

>docs | http://alex-public-doc.s3.amazonaws.com/json_simple-1.1/index.html

- 공식 Docs 는 없는게 흠이다. 



`JSONObject` 는 HashMap 사용법과 동일하며, key & value 로 이루어져 있다. 

```java
JSONObject jsonObject = new JSONObject();
 
jsonObject.put("Name", "iPhone");
jsonObject.put("company", "Apple");
jsonObject.put("OS", "iOS");
jsonObject.put("category", "Phone");
```

Intelli j 의 `Unchecked call to 'put(K, V)' as a member of raw type 'java.util.HashMap'` 에러를 피하려면 아래처럼 사용하자 

```java
HashMap<String, String> hashMap = new HashMap<>();

hashMap.put("Name", "iPhone");
hashMap.put("company", "Apple");
hashMap.put("OS", "iOS");
hashMap.put("category", "Phone");
        
JSONObject jsonObject = new JSONObject(hashMap);
```



`JSONArray` 는 json 객체 내의 배열이다. `add()` 를 통해 원소를 추가한다. 

```java
JSONArray jsonArray = new JSONArray();

jsonArray.add(iphone);
jsonArray.add(galaxyNote9);
```



사용한 카프카 라이브러리인 `kafka-clients` 에는 `StringSeriazlier` 만 제공이 되기 때문에, 생성한 json 객체를 다시 `toString()` 으로 문자열로 변환한 뒤, `StringSerializer` 를 이용하여 전송했다. 

직접 `JsonSerializer` 를 작성하는 방법도 있겠지만, `fasterxml jackson`이라는 다른 라이브러리를 써야하기도 해서, 일단 넘어갔다. 

문자열 json 은 `JSONParser` 를 이용하여 다시 json 객체로 파싱이 가능하다. 



