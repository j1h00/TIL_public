# 1, 마지막 확인 후 
# 조합을 돌린다 
import itertools
# itertools.permutations(pool, 2)

def solution(n, m, k, records):
    
    answer = [0] * k 
    key_count = len(list(set(records[0])))
    min_distance = 200000
    for record in records:
        for i in range(k):
            if record[i] == 1:
                answer[i] = 1
            elif record[i] == m:
                answer[i] = m

        distance = max(record) - min(record)
        min_distance = min(min_distance, distance)
    
    # 순열로 나머지 원소를 채워야 한다. 
    # key_count - found 개

    if answer[0] == 1 and answer[-1] == m:
        pool = range(2, m)
        count = key_count - 2

    elif answer[0] == 1:
        pool = range(2, m+1)
        count = key_count - 1
    elif answer[-1] == m:
        pool = range(1, m)
        count = key_count - 1
    else:
        pool = range(m+1)
        count = key_count

    p = list(itertools.combinations(pool, count))
    print(p)
                
    return answer


answer1 = solution(8, 4, 4, [[1, 5, 1, 3], [5, 7, 5, 6]], )
# print(answer1)

answer2 = solution(8, 4, 4, [[1, 5, 1, 3]])
# print(answer2)

answer3 = solution(10, 3, 3, [[1, 2, 3], [5, 7, 10]])
# print(answer3)