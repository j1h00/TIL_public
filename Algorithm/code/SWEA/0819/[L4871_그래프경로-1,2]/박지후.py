import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {v:[] for v in range(1, V+1)}

    for i in range(E):
        k, v = map(int, input().split())
        graph[k].append(v)

    S, G = map(int, input().split())

    stack = [S]
    done = 0
    while stack:
        now = stack[-1]
        if now == G:
            done = 1
            break
        if graph[now]:
            nxt = graph[now].pop()
            stack.append(nxt)
        else:
            stack.pop()

    print(f'#{tc} {done}')

