# A ⇒ < < < > < < > < >
# 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다.
# 3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0
# 5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4
# 여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 
# 최댓값과 최솟값을 찾아야 한다.


k = int(input())
signs = input().split()
nums = list(range(10))
visited = [0] * 10

num_list = []
# k 개의 sign => k+1 개의 숫자가 필요하다 

def check(prev, next, sign):
    if sign == ">" and prev > next:
        return True
    elif sign == "<" and prev < next:
        return True
    return False

def dfs(arr, count):
    if count == k:
        num_list.append("".join(map(str, arr)))
        return 

    for j in range(10):
        if not visited[j] and check(arr[-1], j, signs[count]):
            visited[j] = 1
            dfs(arr + [j], count + 1)
            visited[j] = 0

    return 

for i in range(10):
    visited[i] = 1
    dfs([i], 0)
    visited[i] = 0

print(num_list[-1])
print(num_list[0])




