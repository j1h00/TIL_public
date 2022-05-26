from pprint import pprint

# 일반적인 풀이 => 2차원 배열을 s번 반복해야 하므로 효율적이지 못하다. 
def solution_slow(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])

    for s in skill:
        type, r1, c1, r2, c2, degree = s
        attack = 1 if type == 2 else -1
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += attack * degree  
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1

    return answer


# 누적합을 이용하는 풀이를 사용하자!
# https://blog.encrypted.gg/1031 참고!
def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    dp = [[0]*(M+1) for _ in range(N+1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        damage = -degree if type == 2 else +degree

        dp[r1][c1] -= damage 
        dp[r1][c2+1] += damage
        dp[r2+1][c1] += damage 
        dp[r2+1][c2+1] -= damage

    for i in range(1, N):
        for j in range(M):
            dp[i][j] += dp[i-1][j]
    for i in range(N):
        for j in range(1, M):
            dp[i][j] += dp[i][j-1]
    
    for i in range(N):
        for j in range(M):
            if dp[i][j] + board[i][j] > 0: 
                answer += 1

    return answer

a1 = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
a2 = solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])

print(a1, a2)