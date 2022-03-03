"""
    "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 
            단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 
            단, 현재 선택된 행은 바뀌지 않습니다.
    
    표의 마지막 행을 삭제한 경우, 바로 윗 행을 선택하는 점에 주의합니다.
"""
    
def solution1(n, k, cmd):
    table = [1 for _ in range(n)]
    prev = [-1] + [i for i in range(n-1)]
    nxt = [i for i in range(1, n)] + [-1]
    deleted = []
    for c in cmd:
        if c == 'C':
            p, nx = prev[k], nxt[k] 
            if nx != -1:
                nxt[p] = nx
            if p != -1:
                prev[nx] = p
            table[k] = 0
            deleted.append(k)
            k = p if nx == -1 else nx
            
        elif c == 'Z':
            revive = deleted.pop()
            p, nx = prev[revive], nxt[revive] 
            if p != -1:
                nxt[p] = revive
            if nx != -1:
                prev[nx] = revive
            table[revive] = 1
            
        elif c[0] == 'D':
            for _ in range(int(c[2])):
                k = nxt[k]
        elif c[0] == 'U':
            for _ in range(int(c[2])):
                k = prev[k]

    answer = ''
    for i in table:
        if i:
            answer += 'O'
        else:
            answer += 'X'

    return answer


def solution(n, k, cmd):
    k = k+1
    table = ["O" for _ in range(n+1)]
    graph = {i:[i-1, i+1] for i in range(1, n+1) }
    deleted = []
    for c in cmd: 
        if c == 'C':
            k_prev, k_next = graph[k]
            if k_prev:
                graph[k_prev][1] = k_next
            if k_next != n+1:
                graph[k_next][0] = k_prev

            table[k] = "X"
            deleted.append(k)
            k = k_prev if k_next == n+1 else k_next
            continue

        elif c == 'Z':
            revive = deleted.pop()
            r_prev, r_next = graph[revive]
            if r_prev:
                graph[r_prev][1] = r_next
            if r_next != n+1:
                graph[r_next][0] = r_prev
            table[revive] = "O"
            continue
        elif c[0] == "D":
            for _ in range(int(c[2])):
                k = graph[k][1]
                continue
        elif c[0] == "U":
            for _ in range(int(c[2])):
                k = graph[k][0]
                continue


    return "".join(table[1:])

def solution2(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)}
    OX = ["O" for i in range(1,n+1)]
    stack = []
    k += 1
    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"

            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)

# 처음 행 개수, 선택된 행의 위치 k
n, k = 8, 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

answer1 = solution(n, k, cmd1)
answer2 = solution(n, k, cmd2)

print(answer1, answer2)



    