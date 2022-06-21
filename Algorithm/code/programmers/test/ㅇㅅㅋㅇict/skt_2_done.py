from pprint import pprint

# def paint()

def solution(n, clockwise):
    board = [[0]*n for _ in range(n)] 

    # 시계방향일 경우 방향과 시작점
    d_clockwise = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    s_clockwise = [(0, 0), (0, n-1), (n-1, n-1), (n-1, 0)]

    # 반 시계방향일 경우 방향과 시작점
    d_counter_clockwise = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    s_counter_clockwise = [(0, 0), (n-1, 0), (n-1, n-1), (0, n-1)]

    if clockwise:
        directions = d_clockwise
        start = s_clockwise
    else:
        directions = d_counter_clockwise
        start = s_counter_clockwise

    while :
        x, y = start[i] 
        board[x][y] = 1 # 시작점을 1로 초기화한다. 

        d_index = i # 현재 이동할 방향
        _len = n - 2 # 현재 방향으로 이동할 칸의 수
        count = 2 # 이동한 칸에 채울 숫자

        for _ in range(3): # 총 세 번 다른 방향으로 이동한다. 
            dx, dy = directions[d_index] # 현재 이동할 방향 

            for _ in range(_len): # _len 길이 만큼 이동한다. 
                x, y = x + dx, y + dy # 현재 방향으로 dx, dy 만큼 한칸 이동한다. 
                board[x][y] = count # 이동한 칸을 숫자로 채운다.
                count += 1 # 숫자를 1 늘린다. 
            
            d_index = d_index + 1 if d_index < 3 else 0 # 방향을 시계방향으로 바꿔준다. 
            _len -= 1 # 방향이 바뀔 때마다 이동하는 칸의 수가 1 줄어든다.
    
    return board 

answer1 = solution(5, True)
pprint(answer1)

answer2 = solution(6, False)
answer3 = solution(9, False)


pprint(answer2)
pprint(answer3)