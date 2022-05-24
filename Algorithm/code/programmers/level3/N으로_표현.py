def solution(N, number):
    answer = 0
    count = [0]*32000
    
    q = []
    now = q.pop()
    for nxt in [now*N, now/N, now+N, now-N]:
        count[nxt] = count[now] + 1


    return answer


answer = solution(5, 12);
answer = solution(2, 11);
print(answer)
