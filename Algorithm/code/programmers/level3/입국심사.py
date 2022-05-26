def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for t in times:
            count += mid // t
            if count >= n:
                break 

        if count < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid

    return answer


answer1 = solution(6, [7, 10])
answer2 = solution(10, [6, 8, 10])
print(answer1)
print(answer2)
