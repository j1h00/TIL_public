"""
    대기실은 5개이며, 각 대기실은 5x5 크기입니다.
    거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
    단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

    응시자가 앉아있는 자리(P)를 의미합니다.	
    빈 테이블(O)을 의미합니다.	
    파티션(X)을 의미합니다.
"""

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

N = 5
adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
jump = [(i, j) for i in range(N) for j in range(N) if i + j == 2]
flag = False
for place in places:
    for x in range(N):
        for y in range(N):
            if place[x][y] == 'P':
                # 가능한 범위를 탐색한다. 
                for dx, dy in adj:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < N and 0 <= ny < N and place[nx][ny] == 'P':
                        flag = True
                        break 
                
                for dx, dy in jump:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and place[nx][ny] == 'P':
                        # partition 이 있는지 확인한다 
                        if x == nx or y == ny: # 일직선 상에 있는 것이므로 
                            if place[(nx + x)//2][(ny + y)//2] != 'X':
                                flag = True 
                                break 
                        else: # 대각선인 경우, 몇개로 나눌까? 4개? 2개?
                            if x < nx and y < ny:
                                if place[x+1][y] != 'X' or place[x][y+1] != 'X':
                                    flag = True 
                                    break 
                            if x < nx and y < ny:
                                if place[x+1][y] != 'X' or place[x][y+1] != 'X':
                                    flag = True 
                                    break
                                
                                
        if flag:
            break 
    
