
# 독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

def main():
    while True:
        INPUT = list(map(int, input().split()))

        if INPUT[0] == 0:
            break

        k = INPUT[0]
        S = INPUT[1:]
        visited = [0] * k
        dfs([], -1, 0, k, visited, S)
        print()


def dfs(nums, prev, count, k, visited, S):

    if count == 6:
        print(" ".join(map(str, nums)))
        return 

    for i in range(k):
        if not visited[i] and S[i] > prev:
            visited[i] = 1
            dfs(nums + [S[i]], S[i], count + 1,  k, visited, S)
            visited[i] = 0
    
    
main()
    