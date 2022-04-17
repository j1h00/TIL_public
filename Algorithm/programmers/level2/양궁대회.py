MAX_SCORE = 0
answer = []

def solution(n, info):
    global MAX_SCORE
    MAX_SCORE = 0 

    need_points = []
    for p in info:
        need_points.append(p+1)

    def get_subsets(count, index, my_info):
        global MAX_SCORE, answer


        if index == 11:            
            score = sum(my_info)
            if count < n:
                remain = n - count
                for i in range(11):
                    if not my_info[i] and remain >= need_points[i]:
                        my_info[i] = need_points[i]
                        score += 11 - i - 1
                        remain -= need_points[i]

            if score > MAX_SCORE:
                print(index, my_info, score)
                MAX_SCORE = score
                answer = [my_info]
            elif score == MAX_SCORE:
                print("@@", index, my_info, score)
                answer.append(my_info)

            return 

        if count + need_points[index] <= n:
            get_subsets(count + need_points[index], index + 1, my_info + [need_points[index]])

        get_subsets(count, index + 1, my_info + [0])
                
    # get subsets
    get_subsets(0, 0, [])
    answer.sort(key= lambda x: x[::-1], reverse=True)
    return answer

answer1 = solution(5, [2,1,1,1,0,0,0,0,0,0,0])
print(answer1)

# answer2 = solution(1, [1,0,0,0,0,0,0,0,0,0,0])
# answer3 = solution(9, [0,0,1,2,0,1,1,1,1,1,1])

# print(answer2)
# print(answer3)