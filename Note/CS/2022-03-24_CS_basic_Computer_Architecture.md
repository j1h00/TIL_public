# CS_basic : Computer Architecture

기본적인 CS 지식을 정리한 글입니다. 

>출처 
>
>[📖Tech Interview for developer : 신입 개발자 전공 지식 & 기술 면접 백과사전 ](https://gyoogle.dev/blog/)

## Computer Architecture

### Intro

#### Central Processing Unit (CPU)

- 주기억장치에서 프로그램 명령어와 데이터를 읽어와 처리하고 명령어의 수행 순서를 제어함 중앙처리장치는 비교와 연산을 담당하는 **산술논리연산장치(ALU)**와 명령어의 해석과 실행을 담당하는 **제어장치**, 속도가 빠른 데이터 기억장소인 **레지스터**로 구성되어있음

#### 기억장치

- 주기억장치와 보조기억장치로 나누어지며, RAM과 ROM도 이곳에 해당함. 실행중인 프로그램과 같은 프로그램에 필요한 데이터를 일시적으로 저장한다.

  보조기억장치는 하드디스크 등을 말하며, 주기억장치에 비해 속도는 느리지만 많은 자료를 영구적으로 보관할 수 있는 장점이 있다.

#### 시스템 버스 

- 데이터 버스 
  - 중앙처리장치와 기타 장치 사이에서 데이터를 전달하는 통로 (양방향)
- 주소 버스 
  - 데이터를 정확히 실어나르기 위해서는 기억장치 '주소'를 정해주어야 한다. 
  - 주소버스는 중앙처리장치가 주기억장치나 입출력장치로 **기억장치 주소를 전달**하는 통로이기 때문에 '단방향'
- 제어 버스 
  - 주소 버스와 데이터 버스는 모든 장치에 공유되기 때문에 이를 제어할 수단이 필요함
  - 제어 버스는 중앙처리장치가 기억장치나 입출력장치에 **제어 신호**를 전달하는 통로임 (읽기 쓰기를 수행하는 양방향)
  - 제어 신호 종류 : 기억장치 읽기 및 쓰기, 버스 요청 및 승인, 인터럽트 요청 및 승인, 클락, 리셋 등

### CPU 

#### 연산 장치 (ALU; Arithmetic & Logic Unit)

- 산술연산과 논리연산 수행 (따라서 산술논리연산장치라고도 불림)

- 연산에 필요한 데이터를 레지스터에서 가져오고, 연산 결과를 다시 레지스터로 보냄

#### 제어 장치 (CU; control unit)

- 명령어를 순서대로 실행할 수 있도록 제어하는 장치

- 주기억장치에서 프로그램 명령어를 꺼내 해독하고, 그 결과에 따라 명령어 실행에 필요한 제어 신호를 기억장치, 연산장치, 입출력장치로 보냄

  또한 이들 장치가 보낸 신호를 받아, 다음에 수행할 동작을 결정함

#### 레지스터 

- 고속 기억장치, 명령어 주소, 코드, 연산에 필요한 데이터, 연산 결과 등을 임시로 저장

#### CPU 동작 과정 

1. 주기억장치는 입력장치에서 입력받은 데이터 또는 보조기억장치에 저장된 프로그램 읽어옴
2. CPU는 프로그램을 실행하기 위해 주기억장치에 저장된 프로그램 명령어와 데이터를 읽어와 처리하고 결과를 다시 주기억장치에 저장
3. 주기억장치는 처리 결과를 보조기억장치에 저장하거나 출력장치로 보냄
4. 제어장치는 1~3 과정에서 명령어가 순서대로 실행되도록 각 장치를 제어

#### 명령어 집합 (ISA; Instruction Set Architecture)

Operation Code + Operand 

- 연산 코드는 연산, 제어, 데이터 전달, 입출력 기능을 가짐

- 피연산자는 주소, 숫자/문자, 논리 데이터 등을 저장

- CPU가 주기억장치에서 한번에 하나의 명령어를 인출하여 실행하는데 필요한 일련의 활동을 '명령어 사이클'이라고 말함

  명령어 사이클은 인출/실행/간접/인터럽트 사이클로 나누어짐

### Cache Memory 

속도가 빠른 장치와 느린 장치에서 속도 차이에 따른 병목 현상을 줄이기 위한 메모리를 말한다. CPU 에 보통 2 ~ 3개 정도 사용됨. 

- L1 : CPU 내부에 존재
- L2 : CPU와 RAM 사이에 존재
- L3 : 보통 메인보드에 존재한다고 함

#### 작동 원리 

- 시간 지역성
  - for나 while 같은 반복문에 사용하는 조건 변수처럼 한번 참조된 데이터는 잠시후 또 참조될 가능성이 높음
-  공간 지역성
   -  A[0], A[1]과 같은 연속 접근 시, 참조된 데이터 근처에 있는 데이터가 잠시 후 또 사용될 가능성이 높음

이처럼 캐시에 데이터 저장 시, 참조 지역성(공간)을 최대한 활용하기 위해 해당 데이터 뿐 아니라 옆 주소의 데이터도 같이 가져와 미래에 쓰일 것을 대비한다. 

CPU가 요청한 데이터가 캐시에 있으면 **Cache Hit**, 없으서 DRAM 에서 가져오면 **Cache Miss**

#### Cache Miss 3 case

1. Cold miss : 해당 메모리 주소를 처음 불러서 나는 미스 
2. Conflict Miss : 캐시 메모리에 A와 B 데이터를 저장해야 하는데, A와 B가 같은 캐시 메모리 주소에 할당되어 있어서 나는 미스 (direct mapped cache에서 많이 발생)
3. Capacity Miss : 캐시 메모리의 공간이 부족해서 나는 미스 (Conflict는 주소 할당 문제, Capacity는 공간 문제)
   - 캐시 메모리 공간을 키워서 해결하는 경우, 캐시 접근 속도가 느려지고 파워의 소모가 크다. 
