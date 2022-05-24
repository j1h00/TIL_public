from itertools import permutations


def solution(n, weak, dist):
    L = len(weak)
    answer = -1
    weak = weak + [w + n for w in weak]
    
    for i in range(L):
        for friends in permutations(dist):
            count = 1
            position = weak[i]

            for f in friends:
                position += f
                if position < weak[i+L-1]:
                    count += 1
                    position = [w for w in weak[i+1:i+L] if w > position][0]
                else:
                    if answer == -1:
                        answer = count
                    else:
                        answer = min(answer, count)
                    break
        
    return answer



answer1 = solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
print(answer1)


answer2 = solution(12, 	[1, 3, 4, 9, 10], [3, 5, 7])
print(answer2)



    # 바로 오른쪽 지점과의 거리가 어느 정도인지 찾아보자 
    # diff = []
    # for i in range(len(weak) - 1):
    #     diff.append(weak[i+1] - weak[i])
    # diff.append(n + weak[0] - weak[-1])
    # print(diff)
    # short_path = sum(diff) - max(diff)
    
    # if short_path <= max(dist):
    #     return 1

    # num = len(weak)
    # diff = [[] for _ in range(num)]
    # for i in range(num):
    #     for j in range(1, num):
    #         a = (i + j - 1) % num 
    #         b = (i + j) % num
    #         now_diff = weak[b] - weak[a]
            
    #         diff[i].append(now_diff if now_diff > 0 else now_diff + 12)
    # diff.sort(key= lambda x: sum(x))
    # min_diff = diff[0]
    # if sum(min_diff) <= max(dist):
    #     return 1
    
    # while True:
    #     count = 1
    #     for 

    # MIN_COUNT = 10
    # dist.sort(reverse=True)
    # num = len(weak)
    # for i in range(num):
    #     d = 0
    #     for j in range(1, num):
    #         index = i + j % num 
    #         diff = weak[index] - weak [i] 
    #         diff = diff if diff > 0 else diff + n 
    #         if dist[d] < diff:
    #             d += 1