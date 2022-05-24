# 삭제 결과가 기준을 만족하지 않으면 무시된다. 
# build_frame의 원소는 [x, y, a, b]형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, 
# [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.


# 아래처럼 조건에 맞으면 설치, 삭제 하려고 했는데,
# 삭제 조건이 너무 까다롭고 길을 잃기 쉬워보인다.. 

# 일단 설치 혹은 삭제 한 후에 
# 조건에 만족하는지 확인하는 방법이 훨씬 좋을 것 같다. (효율성 문제가 아니므로 통과 가능)
# 물론 아래처럼 모든 경우에 대해 비교한 풀이도 있었다. 
# def solution(n, build_frame):
#     answer = []

#     built = [[[0]*2 for _ in range(n)] for _ in range(n)]

#     for x, y, a, b, in build_frame:
#         if a: # 보
#             if b: # 보를 설치하는 경우
#                 if built[x][y-1][0] or built[x+1][y-1][0]: # 왼쪽 오른쪽 아래에 기둥이 설치된 경우
#                     built[x][y][a] = 1
#                 elif 0 < y < n-1 and built[x-1][y][1] and built[x+1][y][1]: # 왼쪽 오른쪽으로 보가 설치된 경우 
#                     built[x][y][a] = 1
#                 continue
#             else : # 보를 삭제하는 경우 
#                 if built[x][y][0]: # 바로 위에 기둥이 있는 경우 
#                     if 0 < x and (built[x][y-1][0] or built[x-1][y][1]): # 아래에 기둥이 있거나 왼쪽에 보가 있는 경우 삭제 가능 
#                         built[x][y][1] = 0 
#                     elif not x and built[x][y-1][0]: # 왼쪽 끝인데, 아래에 기둥이 있는 경우 삭제 가능 
#                         built[x][y][1] = 0
#                 if built[x+1][y][0]: # 오른쪽 끝 위에 기둥이 있는 경우 
#                     if x < n-1 and (built[x+1][y-1][0] or built[x+1][y][1]) # 오른쪽 아래에 기둥이 있거나, 오른쪽에 보가 있는 경우 삭제 가능 
#                         built[x][y][1] = 0
#                     if x == n-1 and built[x+1][y-1][0]: # 오른쪽 끝인 경우, 오른쪽 아래에 기둥이 있는 경우 삭제 가능
#                         built[x][y][1] = 0
#         else: # 기둥 
#             if b: # 기둥을 설치하는 경우 
#                 if y == 0: # 바닥인 경우 무조건 설치 
#                     built[x][y][0] = 1
#                 elif not x and (built[x][y-1][0] or built[x][y][1]): # 왼쪽 끝인 경우, 아래에 기둥이 있거나 보가 있는 경우 설치
#                     built[x][y][0] = 1
#                 elif 0 < x < n and (built[x][y-1][0] or built[x][y][1] or built[x-1][y][1]): # 양쪽 끝이 아닌 경우, 아래 기둥 혹은 양 옆으로 보가 있으면 설치 
#                     built[x][y][0] = 1
#                 elif x == n and (built[x][y-1][0] or built[x-1][y][1]): # 오른쪽 끝인 경우, 아래에 기둥이 있거나 왼쪽에 보가 있는 경우 설치
#                     built[x][y][0] = 1
#             else: # 기둥을 삭제하는 경우 
#                 if y < n and built[x][y+1][0]: # 위에 기둥이 있는 경우 
#                     if built[x-1][y+1][1] or built[x-1]: # 왼쪽 오른쪽 위에 보가 있으면 삭제 가능 

#                 elif : # 위에 보가 있는 경우 

#                 elif : # 위 왼쪽에 보가 있는 경우 

#     return answer


# reference to : https://velog.io/@tjdud0123/%EA%B8%B0%EB%91%A5%EA%B3%BC-%EB%B3%B4-%EC%84%A4%EC%B9%98-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
def impossible(built):
    for x, y, a in built:
        if not a: # 기둥인 경우
            # 바닥이 아닌 경우 && 아래에 기둥이 없는 경우 && 왼쪽 혹은 현재 위치에 보가 없는 경우
            if y and (x, y-1, 0) not in built and (x-1, y, 1) not in built and (x, y, 1) not in built:
                return True
        else: # 보인 경우 
            # 현재 그리고 오른쪽 아래에 기둥이 없는 경우 && 왼쪽과 오른쪽에 보가 없는 경우 
            if (x, y-1, 0) not in built and (x+1, y-1, 0) not in built and not ((x-1, y, 1) in built and (x+1, y, 1) in built):
                return True
    return False

def solution(n, build_frame):
    built = set()
    
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            built.add(item)
            if impossible(built):
                built.remove(item)
        elif item in built: # 삭제할 때
            built.remove(item)
            if impossible(built):
                built.add(item)
    list_built = map(list, built)

    return sorted(list_built, key = lambda x: (x[0], x[1], x[2]))



answer1 = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(answer1)

