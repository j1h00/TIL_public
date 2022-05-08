def solution(rooms, target):
    worker_room = {}
    worker_room_count = {}
    distance = {}

    for room_info in rooms:
        
        parsed_info = room_info.replace("[", "").split("]")
        room_num = int(parsed_info[0])

        workers = parsed_info[1].split(",")
        for worker in workers:
            if worker in worker_room:
                worker_room[worker].append(room_num)
                worker_room_count[worker] += 1
                for room in worker_room[worker]:
                    distance[worker] = min(distance[worker], abs(room - target))
            else:
                worker_room[worker] = [room_num]
                worker_room_count[worker] = 1
                distance[worker] = abs(target - room_num)
    

    all_workers = list(worker_room.keys())
    answer = []
    for worker in all_workers:
        if target in worker_room[worker]:
            continue
        answer.append(worker) 
    answer.sort(key = lambda x: (worker_room_count[x], distance[x], x))

    return answer

answer1 = solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)
answer2 = solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202)
answer3 = solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234)

print(answer1)
print(answer2)
print(answer3)


