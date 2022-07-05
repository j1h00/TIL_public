# LeetCode: methods 

문제 풀이하면서 기억해둘만한 짧은 코드를 모아봅니다.. 

## Javascript

### string, number, array

특수 문자 제거 

```js
const newString = s.replace(/[^a-z0-9]/gi, "").toLowerCase();

const words = paragraph.toLowerCase().split(/\W+/);
```

- `[^...]` : `...` 를 제외하고 선택

채우기 

```js
string.padEnd(10, '.') // 'hello' => 'hello.....'
string.padStart(4, '0') // '5' => '0005'
```

swap => 구조 분해 할당 

```js
[s[i], s[j]] = [s[j], s[i]];
```

중복 제거 

```js
const arr = [1,3,2,4,3,1,5,6,2,1];
const newArr = [...new Set(arr)];
const newArr2 = Array.from(new Set(cars));
const newArr3 = arr.filter((i) => i !==s.indexOf(s[i]))

const str = "abcdacbe";
const newStr = [...new Set(str)].join('');

const arr = [1,1,4,1,1];
arr.filter( el => arr.indexOf(el) === arr.lastIndexOf(el) );
```

`slice` vs `splice`

```js
arr.slice(startIndex, endIndex); // => return new arr 
arr.splice(startIndex, count, addItem) // => 배열 변경 
```

`isNan`

```js
isNaN('item') // return true 
isNaN(123) // return false 
```

default 배열 생성

```js
Array(5).fill(1); // [1,1,1,1,1]
Array(5).fill(1).map((el, i) => el+i); // [1,2,3,4,5]
```

2차원 배열

```js
Array.from(Array(5), () => new Array(2)); // 빈 배열, 
Array.from(Array(5), () => Array(2).fill(null)); // null 로 초기화 
                        
Array.from({length: 20}, () => Array(10).fill(0));               
```

합집합 / 교집합

```js
const union = new Set([...setA, ...setB]);
const intersection = new Set([...setA].filter(x => setB.has(x)));

const difference1 = new Set([...setA].filter(x => !setB.has(x))); // setA - setB
```

Math 

```js
Math.pow(2,10); // 2의 10승 : 1024
Math.round(0.4); // 반올림 : 0
Math.ceil(0.4); // 올림 : 1
Math.floor(1.4); // 내림 : 1
Math.abs(-5); // 절대값 : 5
Math.max(x,y,z); // 가장큰 인자 반환(min도 있음)
Math.random(); // 0과 1.0 사이에 임의수 반환
Math.sqrt(4); // 제곱근 반환 : 2
Math.pow(x,y); //x의 y제곱을 반환
```

함수형으로 for loop 제거 

```js
let sum = 0;
for (let i = 0; i < 10; ++i) {
  sum += i;
};

const sum = [...Array(10)].reduce((acc, _, i) => acc += i, 0);
```

### Object

for `key` in object / for `value` of object

```js
for (let key in iterable) {
    console.log(key); // key of object, every property of array 
}

for (let val in iterable) {
    console.log(val); // every value 
}
```

함수형 객체 배열 복제 

```js
const result = cities.reduce((accumulator, item) => {
  return {
    ...accumulator,
    [item.name]: item.visited
  }
}, {});
```

value 로 key 찾기 

```js
Object.keys(object).find(key => object[key] === value);
Object.keys(object).filter((key) => object[key] === value);
```



## Python

### 문자열

특수 문자 제거

```python
string.isalpha() # 문자 (알파벳, 한글 ...) return True
string.isdigit() # 숫자 
string.isalnum() # alpha + num 
```

```python
 # import re (regex module)
# \w : alpha + numeric => [a-zA-Z0-9_] 
# \W : non-alphanumeric => [^a-zA-Z0-9_] 
words = re.findall(r'\w+', p.lower()) # faster than sub
words = re.split(r'\W+', paragraph.lower())

s = re.sub('[^a-z0-9]', '', s) # [^...] means except ... 
```

```python
a = re.split(r'\W+', paragraph.lower()) # 
```



palindrome

```python
return s==s[::-1]
```

