"""
    "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 
            단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 
            단, 현재 선택된 행은 바뀌지 않습니다.
"""
    

def solution(n, k, cmd):
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



n, k = 8, 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

solution(n, k, cmd1)
solution(n, k, cmd2)


    