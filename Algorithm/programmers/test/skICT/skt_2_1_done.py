from pprint import pprint

# def paint()

def solution(n, clockwise):
    board = [[0]*n for _ in range(n)] 

    # 시계방향일 경우 방향과 시작점
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = [[0, 0], [0, n-1], [n-1, n-1], [n-1, 0]]
    move_start = [(1,1), (1, -1), (-1, -1), (-1, 1)]

    if not clockwise: # 반시계 방향일 경우 방향과 시작점이 달라진다. 
        directions[0], directions[1] = directions[1], directions[0]
        directions[2], directions[3] = directions[3], directions[2]
        start[1], start[3] = start[3], start[1]
        move_start[1], move_start[3] = move_start[3], move_start[1]

    # 시작점을 기준으로 
    # 특정한 방향, 특정한 칸만큼 일직선으로 이동하면서 숫자를 채우는 함수
    def paint(start, d, l, count): 
        x, y = start # 시작점 
        for _ in range(l): # l 만큼 이동하면서 
            board[x][y] = count # 숫자를 채운다. 
            dx, dy = d 
            x, y = x + dx, y + dy # 채우고 난 뒤엔 특정 방향으로 이동한다. 
            count += 1 # 숫자를 1 높여준다. 
        
    count = 1
    _len = n-1 
    for k in range(n // 2): # ex) n 이 5인 경우, 5x5 의 가장 바깥, 그 다음엔 3x3 의 가장 바깥을 채운다. 
        for i in range(4): # 4개 방향에 대하여 실행한다. 
            paint(start[i], directions[i], _len, count)
        
        count += _len
        _len = _len - 2
        for k in range(4): # ex) n 이 5인 경우, 다음 숫자를 채우기 위해 시작점을 3x3 에 맞게 업데이트 해준다. 
            start[k][0], start[k][1] = start[k][0] + move_start[k][0], start[k][1] + move_start[k][1]
    
    if n % 2: # 홀수 인 경우엔 가장 가운데를 마저 채워준다. 
        board[n//2][n//2] = count

    return board 

# answer1 = solution(5, True)
# pprint(answer1)

answer2 = solution(6, False)
pprint(answer2)


# answer3 = solution(9, False)
# pprint(answer3)