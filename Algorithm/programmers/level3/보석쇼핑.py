def solution(gems):
    last = len(gems)
    gem_type = len(set(gems))
    map = {}
    answer = []
    result = []

    a = 0 
    b = 1
    map[gems[0]] = 1
    while b-1 < last:
        if len(map) == gem_type:
            result.append([[a+1,b], b-a])
            temp = gems[a]
            map[temp] -= 1
            if map[temp] == 0:
                map.pop(temp)
            a += 1
        else:
            if b == last:
                break
            if gems[b] in map:
                map[gems[b]] += 1
            else:
                map[gems[b]] = 1
            b += 1

    sorted_result = sorted(result, key = lambda x: x[1])
    answer = sorted_result[0][0]
    return answer