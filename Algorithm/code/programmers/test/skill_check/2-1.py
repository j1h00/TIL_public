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


answer1 = solution([70, 50, 80, 50], 100)
answer2 = solution([70, 80, 50], 100)
answer3 = solution([70, 80, 50, 50, 30, 20 ], 100)

print(answer1)
print(answer2)
print(answer3)


# Fail 
# def solution(people, limit):
#     answer = 0
#     s_people = sorted(people, reverse = True)

#     boats = [s_people[0]]

#     for i in range(1, len(people)):
#         now_person = s_people[i]
#         flag = True
#         for j in range(len(boats)):
#             if now_person + boats[j] <= limit:
#                 boats[j] += now_person
#                 flag = False
#                 break 
#         if flag:
#             boats.append(now_person)
        
#     return len(boats)
