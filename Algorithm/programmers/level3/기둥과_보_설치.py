# 삭제 결과가 기준을 만족하지 않으면 무시된다. 

def solution(n, build_frame):
    answer = []

    built = [[[0]*2 for _ in range(n)] for _ in range(n)]

    for x, y, a, b, in build_frame:
        if a and b:
            if built[x][y-1][0] or built[x+1][y-1][0]:
                built[x][y][a] = 1
            elif 0 < y < n-1 and built[x-1][y][1] and built[x+1][y][1]:
                built[x][y][a] = 1
            continue
        elif a and not b:
            if built[x][y-1][0]



        

    return answer