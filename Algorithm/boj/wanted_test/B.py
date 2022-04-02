

def dfs(x, y, road):
    
    return 

def main():
    N, Q = map(int, input().split())

    nums = [0] + list(map(int, input().split()))
    road = {k:[] for k in range(N)}
    play = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)

    for _ in range(Q):
        x, y = map(int, input().split())
        play.append((x, y))

    for x, y in play:
        dfs(x, y)
    
        
    
    return 


main()