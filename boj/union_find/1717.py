"""
    초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 
    여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

    집합을 표현하는 프로그램을 작성하시오.

    합집합은 0 a b의 형태로 입력이 주어진다. 
    이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 
    두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 
    이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다
"""

def union(x, y):
    root[y] = find(x)
        

def find(x):
    if x != root[x]:
        while x == root[x]:
            x = root[x]
    return x
        
n, m = map(int, input().split())
root = list(range(n+1))

for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        output = 'YES' if root[a] == root[b] else 'NO'
        print(output)
    else:
        union(a, b)