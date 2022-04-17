def solution(people, limit):
    s_people = sorted(people) # 오름차순
    answer = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        if s_people[i] + s_people[j] <= limit:
            i += 1 
        j -= 1

    return answer