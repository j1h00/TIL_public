"""
    징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
    디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
    단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.

    "니니즈 친구들"은 한 번에 한 명씩 징검다리를 건너야 하며, 
    한 친구가 징검다리를 모두 건넌 후에 그 다음 친구가 건너기 시작합니다.

    최대 몇 명까지 징검다리를 건널 수 있는지 return 하도록 solution 함수를 완성해주세요.
"""
# 효율성도 만족해야 함. 
# 이진탐색 문제였다... 
def solution(stones, k):
    answer = 0
    
    fast_forward = min(stones)
    stones = list(map(lambda x: x - fast_forward, stones))
    answer += fast_forward

    left = 1
    right = max(stones)
    N = len(stones)
    # 이진탐색
    while left <= right:

        # mid : 징검다리를 건널 수 있는 수 
        mid = (right + left) // 2 

        max_skip = 0
        prev = 0
        for i in range(N): 
            if stones[i] - mid <= 0: 
                max_skip = max(max_skip, i - prev)     
            else: 
                prev = i 

            if max_skip > k: # 건널 수 없는 경우 
                break

        if max_skip <= k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))