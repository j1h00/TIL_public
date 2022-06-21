def solution(p):
    n = len(p)
    i = 0

    answer = [0] * n # 정답을 담을 배열 (해당 위치의 값이 몇 번 바뀌었는지 담는다.)
    # 문제 요구사항에 맞추어 정렬 알고리즘 작성 (selection sort)
    while i < n: # i 가 n 보다 작은 경우 계속, n 인 경우 종료
        j = i # p[i] ~ p[n-1] 중에 가장 작은 숫자의 인덱스 j 
        for idx in range(i+1, n): # j 를 찾는다. 
            if p[idx] < p[j]:
                j = idx 
        
        if i != j: # 3번 조건에 따라, i와 j 가 다르다면 swap 
            p[i], p[j] = p[j], p[i]
            answer[i] += 1 # 해당 위치의 값이 바뀌었으므로 횟수를 증가
            answer[j] += 1

        i += 1
    
    return answer