import sys

sys.stdin = open('input.txt')

T = 10

# dfs version
for tc in range(T):
    tc, n = map(int, input().split())
    v1 = [0]*100            # 간선 정보를 저장하는 정적배열 1
    v2 = [0]*100            # 간선 정보를 저장하는 정적배열 2
    e = list(map(int, input().split()))
    for i in range(n):
        k, v = e[2*i:2*i+2]
        if not v1[k]:
            v1[k] = v
        else:
            v2[k] = v

    stack = []
    stack.append(0)
    done = 0
    while stack:
        now = stack[-1]
        if now == 99 or now == 99:      # 도착지에 도착하면, while loop 을 빠져나갑니다.
            done = 1
            break
        if v1[now] or v2[now]:          # 아직 갈 수 있는 정점이 남아있다면,
            if v1[now]:
                stack.append(v1[now])   # stack 에 다음 정점을 추가하고
                v1[now] = 0
                continue                # 다음 while loop 를 시작합니다.
            if v2[now]:
                stack.append(v2[now])
                v2[now] = 0
                continue
        else:
            stack.pop()

    print(f'#{tc} {done}')

