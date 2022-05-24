def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    rocks.append(distance)
    left = 0 
    right = distance

    while left <= right:
        mid = (left + right) // 2
        prev = 0
        count = 0
        min_d = distance
        for r in rocks:
            if (r - prev) >= mid:
                min_d = min(min_d, r - prev) 
                prev = r
            else:
                count += 1


        if count > n:
            right = mid - 1
        else:
            answer = min_d
            left = mid + 1
    
    return answer


answer = solution(25, [2, 14, 11, 21, 17], 2)
print(answer)