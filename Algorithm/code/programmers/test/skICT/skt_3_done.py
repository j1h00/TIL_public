def solution(width, height, diagonals):
    w = width 
    h = height

    # 경우의 수 문제!
    # a = 시작점에서 대각선의 한 점까지 이동하는 경우의 수
    # b = 대각선의 다른 한 점에서 도착점까지 이동하는 경우의 수 
    # a x b 
    # 대각선의 개수 만큼 반복

    # 팩토리얼 계산
    def factorial(x):
        result = 1
        for i in range(1, x+1):
            result *= i 
        return result 

    # x * y 크기에서의 최단 경로 계산 
    def cal_case(x, y):
        return int(factorial(x + y)) // int(factorial(x) * factorial(y))

    answer = 0
    for a, b in diagonals:
        x1, y1 = a-1, b # 대각선의 좌측 상단 점
        x2, y2 = a, b-1 # 대각선의 우측 하단 점 
        case1 = cal_case(x1, y1) * cal_case(w-x2, h-y2)
        case2 = cal_case(x2, y2) * cal_case(w-x1, h-y1)
        answer += case1 + case2

    return answer % 10000019

answer1 = solution(2, 2, [[1,1],[2,2]])
print(answer1)

answer2 = solution(51, 37, [[17,19]])
print(answer2)
