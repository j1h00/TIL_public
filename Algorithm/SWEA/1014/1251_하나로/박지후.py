import sys
sys.stdin = open('input.txt')

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)
    
def kruskal(graph):
    result = []
    graph.sort()
    for d, island in graph:
        if find_set(island[0]) != find_set(island[1]):
            result.append(d)
            union(island[0], island[1])
    return result

def get_distance(i,j):
    loc1 = (X[i], Y[i])
    loc2 = (X[j], Y[j])
    distance_square = (loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2

    return distance_square

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = list(range(N)) # make_set()

    graph = []
    for i in range(N-1):
        for j in range(i+1, N):
            graph.append((get_distance(i, j), (i,j)))

    result = kruskal(graph)
    total = sum(result) * E

    print(f'#{tc} {round(total)}')