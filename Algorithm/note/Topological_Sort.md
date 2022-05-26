# 위상 정렬 

>[위상 정렬(Topological sort) 개념 및 구현](https://yoongrammer.tistory.com/86)
>
>[[알고리즘] 위상 정렬(Topological Sort)이란](https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html)
>
>[boj: 게임 개발](https://www.acmicpc.net/problem/1516)

백준 문제를 풀이하면서 필요한 위상 정렬을 개념을 다시 한 번 복습한다. 

## 개념 

**위상 정렬(Topological sort)**

- 비순환 방향 그래프(DAG)에서 정점을 선형으로 정렬하는 것
- 모든 간선 (u, v)에 대해 정점 u가 정점 v보다 먼저 오는 순서로 정렬
- 어떤 일을 하는 순서를 찾는 알고리즘으로, 방향 그래프에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하는 것

특징 

- 하나의 방향 그래프에는 여러 위상 정렬이 가능하다.
- 위상 정렬의 과정에서 선택되는 정점의 순서를 위상 순서(Topological Order)라 한다.
- 위상 정렬의 과정에서 그래프에 남아 있는 정점 중에 진입 차수가 0인 정점이 없다면, 위상 정렬 알고리즘은 중단되고 이러한 그래프로 표현된 문제는 실행이 불가능한 문제가 된다.

## 구현

**in_degree (진입 차수) + BFS**

0. 모든 정점의 진입 차수를 in_degree 에 설정



1. 진입 차수가 0인 정점(즉, 들어오는 간선의 수가 0)을 선택

   - 진입 차수가 0인 정점이 여러 개 존재할 경우 어느 정점을 선택해도 무방하다.

   - 초기에 간선의 수가 0인 모든 정점을 큐에 삽입

2. 선택된 정점과 여기에 부속된 모든 간선을 삭제

   - 선택된 정점을 큐에서 삭제

   - 선택된 정점에 부속된 모든 간선에 대해 간선의 수를 감소

3.  1 - 2 번의 과정을 반복해서 모든 정점이 선택, 삭제되면 알고리즘 종료



### 1516 게임 개발

```python
from collections import deque

# 위상 정렬을 이용한 풀이
# initialize 
N = int(input())

in_degree = [0] * (N+1)
time = [0] * (N+1)
build_after = { k:[] for k in range(1, N+1) } # k 가 있을 때, 지을 수 있는 건물
q = deque() # queue for topological sort

for a in range(1, N+1):
    info = input().split()
    time[a] = int(info[0])
    for b in info[1:]:
        if b == "-1":
            break 
        else:
            build_after[int(b)].append(a)
            in_degree[a] += 1

    if not in_degree[a]:
        q.append(a)

# topological sort
result = [0] * (N+1)

while q:
    now = q.popleft()

    result[now] += time[now]
    for b in build_after[now]:
        in_degree[b] -= 1

        # 걸리는 최소 시간.. 만약 now 가 아니라 다른 선수 건물이 있는 경우, 
        # 그 선수 건물을 만들기까지 더 오래걸린다면 ?
        result[b] = max(result[b], result[now]) 
        if not in_degree[b]:
            q.append(b)

for answer in result[1:]:
    print(answer)
```

>[[BOJ 1516] 게임 개발 (Python)](https://velog.io/@kimdukbae/BOJ-1516-%EA%B2%8C%EC%9E%84-%EA%B0%9C%EB%B0%9C-Python) 참고



