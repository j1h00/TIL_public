# Project Note: Kafka

> [Basic of BIGDATA ๐What is apache kafka?](https://www.youtube.com/watch?v=waw0XXNX-uQ)
>
> [๋ฐ์ดํฐ๐พ๊ฐ ์ ์ฅ๋๋ ํ ํฝ์ ๋ํด์ ์์๋ด์๋ค.](https://www.youtube.com/watch?v=7QfEpRTRdIQ&list=PL3Re5Ri5rZmkY46j6WcJXQYRlDRZSUQ1j&index=2)

## Intro 

### **Before Kafka** 

๋ฐ์ดํฐ๋ฅผ ์ ์กํ๋ Source Application ๊ณผ ๋ฐ์ดํฐ๋ฅผ ๋ฐ๋ Target Application ๊ฐ์ ๊ฐ๋จํ ๋จ๋ฐฉํฅ ํต์ ์ ๊ฒฝ์ฐ, 

Source ์ Target Application ์ ๊ฐฏ์๊ฐ ๋์ด๋ ์๋ก ๋ณต์ก๋๊ฐ ๋์ด๋๊ณ , ๋ฐ์ดํฐ ์ ์ก ๋ผ์ธ๋ ๋ง์์ง๋ค. 

๋ฐ์ดํฐ ์ ์ก ๋ผ์ธ์ด ๋ง์์ง๋ฉด ๋ฐฐํฌ์ ์ฅ์ ์ ๋์ํ๊ธฐ ์ด๋ ต๋ค. 

๋ํ ๋ฐ์ดํฐ ์ ์ก ์ protocol format ์ ํํธํ๊ฐ ์ฌํด์ง๋ค. ์ถํ์ format ๋ณ๊ฒฝ ์ฌํญ์ด ์์ ๊ฒฝ์ฐ ์ ์ง ๋ณด์๊ฐ ๋งค์ฐ ์ด๋ ต๋ค. 

์ด๋ฌํ ๋ณต์ก์ฑ์ ํด๊ฒฐํ๊ธฐ ์ํด Linked In ์์ Kafka ๋ฅผ ๊ฐ๋ฐํ์ฌ ์คํ์์ค๋ก ์ ๊ณตํ์๋ค. 

### Kafka

Source ์ Target Application ์ฌ์ด์ coupling ์ ์ฝํ๊ฒ ํ๋ค. 

Source ๋ Kafka ์ ๋ฐ์ดํฐ๋ฅผ ์ ์กํ๊ณ , Target ์ Kafka ์์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์จ๋ค. 

์๋ฅผ ๋ค์ด, Source ์์ ๋ก๊ทธ ๋ฐ์ดํฐ๋ฅผ Kafka ์ ๋ณด๋ด๋ฉด Target ์์๋ Kafka ์์ ๋ก๊ทธ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ ์ ์ฌํ๊ฑฐ๋ ์ด๋ฅผ ์ฒ๋ฆฌํ๋ค.  

Source ์์ ๋ณด๋ผ ์ ์๋ ๋ฐ์ดํฐ์ ํ์์๋ ๊ฑฐ์ ์ ํ์ด ์๋ค. 

![image-20220415093214268](2022-04-15_Project_Note_Kafka.assets/image-20220415093214268.png)

Kafka ์๋ Topic ์ด๋ผ๋ ๊ฐ๋์ด ์์ผ๋ฉฐ, ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๋ Queue ๋ผ๊ณ  ๋ณด๋ฉด ๋๋ค. 

๋ฐ์ดํฐ๋ฅผ ๋ณด๋ด๊ณ  ๋ฐ๋ ์ญํ ์ Kafka Producer ์ Consumer ๊ฐ ๋ด๋นํ๋๋ฐ, ์ด๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ํ์์ผ๋ก ๋์ด ์์ด ๊ตฌํ์ด ๊ฐ๋ฅํ๋ค. 

๊ฒฐ๋ก ์ ์ผ๋ก, Kafka ๊ฐ ์์ฃผ ์ ์ฐํ Queue ์ญํ ์ ํ๋ค๊ณ  ๋ณด๋ฉด ๋๊ณ , ๋ฐ์ดํฐ ํ๋ฆ์ ์์ด fault tolerant (๊ณ ๊ฐ์ฉ์ฑ) ๋ก ์๋ฒ์ ์๊ธด ์ด์ ์ํฉ์ ๋์ํ์ฌ ๋ฐ์ดํฐ๋ฅผ ์์ค ์์ด ๋ณต๊ตฌํ  ์ ์๋ค.  

๋ํ ๋ฎ์ ์ง์ฐ (latency) ์ ๋์ ์ฒ๋ฆฌ๋ (Throughput) ์ ํตํด์ ํจ๊ณผ์ ์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ์ฒ๋ฆฌํ  ์ ์๋ค. 

๋ฐ๋ผ์ ๋น๋ฐ์ดํฐ ์ฒ๋ฆฌ์์ ํ์์ด๋ค!



## Topic

- ๋ค์ํ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๋ ๊ณต๊ฐ, ์ผ๋ฐ์ ์ธ AMQP ์๋ ๋ค๋ฅด๊ฒ ๋์ํ๋ค. 

- ๋ฐ์ดํฐ ๋ฒ ์ด์ค์ ํ์ด๋ธ์ด๋, ํ์ผ ์์คํ์ ํด๋์ ์ ์ฌํ ์ฑ์ง์ ๊ฐ์ง๊ณ  ์๋ค. 

- Topic ์ ๋ชฉ์ ์ ๋ฐ๋ผ click_log, send_sms, location_log ๋ฑ ์ด๋ฆ์ ์ง์ ํ  ์ ์๋ค. 
  - ๋ชํํ ์ด๋ฆ์ ํตํด ์ ์ง ๋ณด์ ์ ํธ๋ฆฌํ๊ฒ ๊ด๋ฆฌํ  ์ ์๋ค. 

![image-20220415094128849](2022-04-15_Project_Note_Kafka.assets/image-20220415094128849.png)

- ํ๋์ Topic ์ ์ฌ๋ฌ ๊ฐ์ partition ์ผ๋ก ๊ตฌ์ฑ๋  ์ ์์ผ๋ฉฐ, partition ์ `#0` ๋ถํฐ ์์ํ๋ค. 

- ํ๋์ partition ์ Queue ์ ๊ฐ์ด ๋ด๋ถ์ producer ๋ก ๋ถํฐ ๋ฐ์ ๋ฐ์ดํฐ๊ฐ ๋์์๋ถํฐ ์ฐจ๊ณก์ฐจ๊ณก ์์ธ๋ค. 

- consumer ๋ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ฅ ์ค๋๋ ์์๋๋ก ๊ฐ์ ธ๊ฐ๊ฒ ๋๋ค. 

  - ๋์ด์ ๋ฐ์ดํฐ๊ฐ ๋ค์ด์ค์ง ์์ผ๋ฉด, consumer ๋ ๋ ๋ค๋ฅธ ๋ฐ์ดํฐ๊ฐ ๋ค์ด์ฌ ๋๊น์ง ๊ธฐ๋ค๋ฆฐ๋ค. 

  - consumer ๊ฐ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ๊ฐ๋๋ผ๋, ๋ฐ์ดํฐ๋ ์ญ์ ๋์ง ์๊ณ  partition ์ ๊ทธ๋๋ก ๋จ๊ฒ ๋๋ค. 

- ์๋ก์ด consumer ๊ฐ ๋ถ๊ฒ ๋๋ฉด, ๋ค์ 0๋ฒ ๋ฐ์ดํฐ๋ถํฐ ๊ฐ์ ธ๊ฐ ์ ์๋ค. 

  - ๋ค๋ง, consumer ๊ทธ๋ฃน์ด ๋ฌ๋ผ์ผ ํ๊ณ , `auto.offset.reset = earliest` ๋ก ์ค์ ๋์ด ์์ด์ผ ํ๋ค. 

  - ์ด๋ฌํ ๋ฐฉ๋ฒ์ผ๋ก **๋์ผํ ๋ฐ์ดํฐ๋ฅผ 2๋ฒ ์ฒ๋ฆฌ**ํ  ์ ์๋๋ฐ, 
  - **๊ฐ์ ๋ฐ์ดํฐ**๋ฅผ ElasticSearch ์ ์ ์ฅํ๊ณ , ๋ ๋ฐฑ์์ ์ํด Hadoop ์ ์ ์ฅํ๋ ๊ฒ์ด ๊ฐ๋ฅํ๋ค. 

![image-20220415094407819](2022-04-15_Project_Note_Kafka.assets/image-20220415094407819.png)

- partition ์ด 2๊ฐ ์ด์์ธ ๊ฒฝ์ฐ, producer ๊ฐ ๋ฐ์ดํฐ๋ฅผ ๋ณด๋ผ ๋ ํค๋ฅผ ์ง์ ํ์ฌ ์ด๋ partition ์ ๋ฐ์ดํฐ๋ฅผ ์์ ์ง ์ ํ  ์ ์๋ค. 
- ํค๊ฐ null ์ด๊ณ  ๊ธฐ๋ณธ ํํฐ์๋๋ฅผ ์ฌ์ฉํ  ๊ฒฝ์ฐ 
  - ๋ผ์ด๋ ๋ก๋น์ผ๋ก ํ ๋น 
- ํค๊ฐ ์๊ณ , ๊ธฐ๋ณธ ํํฐ์๋๋ฅผ ์ฌ์ฉํ  ๊ฒฝ์ฐ 
  - ํค์ ํด์ ๊ฐ์ ๊ตฌํ์ฌ ํน์  partition ์ ํ ๋น 

- partition ์ ๋๋ฆด ๋๋ ๋งค์ฐ ์ ์คํด์ผ ํ๋ค. partition ์ ๋ค์ ์ค์ผ ์ ์๋ค!! 
  - partition ์ ๋๋ ค ๋ฐ์ดํฐ ์ฒ๋ฆฌ๋ฅผ ๋ถ์ฐ์ํฌ ์ ์๋ค. 
  - partition ์ ๋ฐ์ดํฐ๊ฐ ์ญ์ ๋๋ ํ์ด๋ฐ์ ์ต์์ ๋ฐ๋ผ ๋ค๋ฅธ๋ฐ, ์ ์ฅ๋๋ ์ต๋ ์๊ฐ๊ณผ ํฌ๊ธฐ๋ฅผ ์ง์ ํ  ์ ์๋ค. 
    - `log.retention.ms` : ์ต๋ record ๋ณด์กด ์๊ฐ 
    - `log.retention.byte` : ์ต๋ record ๋ณด์กด ํฌ๊ธฐ (byte)
