import sys
sys.stdin = open('input.txt')

def dfs(index):
    global cnt
    for i in range(len(parent[index])):
        if parent[index][i]:
            cnt += 1
            dfs(parent[index][i])
    return


for test_case in range(int(input())):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    parent = [[] for _ in range(e+2)]
    for i in range(0, len(nodes)-1, 2):
        parent[nodes[i]].append(nodes[i+1])
    cnt = 1
    dfs(n)
    print(f'#{test_case+1} {cnt}')