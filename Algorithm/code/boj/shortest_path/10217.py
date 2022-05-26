"""
    초대장 내용에 의하면 구글은 찬민에게 최대 M원까지의 비용만을 여행비로써 부담해주겠다고 한다. 
    인천에서 LA행 직항 한 번 끊어주는게 그렇게 힘드냐고 따지고도 싶었지만, 
    다가올 결승 대회를 생각하면 대회 외적인 곳에 마음을 쓰고 싶지 않은 것 또한 사실이었다. 
    그래서 찬민은 인천에서 LA까지 M원 이하로 사용하면서 도착할 수 있는 가장 빠른 길을 차선책으로 택하기로 하였다.

    각 공항들간 티켓가격과 이동시간이 주어질 때, 
    찬민이 인천에서 LA로 갈 수 있는 가장 빠른 길을 찾아 찬민의 대회 참가를 도와주자.

    입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.
"""
from pprint import pprint

def solve():    
    N, M, K = map(int, input().split()) # 공항 수, 총 지원비용, 티켓의 수 

    tickets = {k:[] for k in range(1, N+1)} 
    for _ in range(K):
        u, v, c, d = map(int, input().split()) # 출발공항, 도착공항, 비용, 소요시간
        tickets[u].append((v, c, d))

    # 단순히 다익스트라를 사용할 수 없다. 
    # => 다음 공항 중에 어떤 공항이 priority 를 가지는지 모른다 
    # => 비용과 소요시간을 모두 고려해야 하므로! 

    # 따라서 모든 경우를 dp 배열에 표시하자
    # dp[i][j]
    # => i 는 공항의 인덱스, j 는 출발 공항에서부터 필요한 비용 (0 <= j <= n) 일 때.
    # => dp[i][j] 는 i 공항까지 가는데, j 만큼의 비용을 사용했을 때 소요시간이다. ]
    # 이 dp 배열을 왼쪽에서 오른쪽으로 (비용이 0 일때부터 점점 증가하는 방향으로) 채워나간다.
    # how? 
    
    INF = 10**9
    dp = [[INF]*(M+1) for _ in range(N+1)] # 비용 M 까지 가능, 입력으로 받은 공항 번호가 1 ~ N 이므로 N+1
    dp[1][0] = 0

    for j in range(M+1): # j == cost, 왼쪽에서 오른쪽으로 비용을 증가시키면서 채워나간다. 
        for i in range(1, N+1):
            if dp[i][j] != INF:
                for v, c, d in tickets[i]:
                    if j + c <= M: # 비용을 만족.
                        dp[v][j + c] = min(dp[v][j + c], dp[i][j] + d)
                        # i 에 연결된 도착 공항 v 들에 대해 
                        # dp[v][j+c] : v 까지 가는데에는 j+c 만큼의 비용이 들고, 
                        # 이 때 소요시간은, min(기존의 소요시간,  i 까지의 소요시간 + d)
    
    result = min(dp[N])
    if result == INF:
        print("Poor KCM")
    else:
        print(result)

T = int(input())
for tc in range(T):
    solve()



