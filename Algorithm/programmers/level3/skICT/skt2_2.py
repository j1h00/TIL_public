# 읽기 작업 => 여러 프로세스가 동시에 가능 (쓰기는 대기해야 함)
# 쓰기 작업 => 하나의 프로세스만 작업 가능 (읽기, 쓰기 모두 대기해야 함)
# 대기 중인 작업 목록에서 => 읽기 보다 쓰기 먼저, 쓰기가 여러개면 요청된 순서대로 
# 수행 시작과 동시에 새 작업 요청이 들어온다면, 새 작업 요청을 포함하여 선택 
    # 10초에 작업이 끝났는데, 10초에 새로운 요청이 온경우 포함 
# 쓰기가 대기중이면 읽기도 대기해야 함 

# "read t1 t2 A B", 또는 "write t1 t2 A B C"
# t1 요청 시각, t2 소요 시간 / A ~ B 를 C 로 


from collections import deque

def solution(arr, processes):

    # status : 작업 중인 프로세스가 없는 경우 0, read 1, write 2
    status = 0
    end_time = 0
    process_queue = deque(processes)
    read_wait_queue = deque()
    write_wait_queue = deque()

    read_results = []
    def read(A, B):
        result = ""
        for i in range(A, B+1):
            result += str(arr[i])

        read_results.append("".join(result))
    def write(A, B, C):
        for i in range(A, B+1):
            arr[i] = C



    def handle_wait_queue(end_time, status):
        while write_wait_queue:
            command, t1, t2, A, B, C = write_wait_queue.popleft()
            end_time += int(t2)
            write(int(A), int(B), C)
            status = 2

        start = end_time
        while read_wait_queue:
            command, t1, t2, A, B = read_wait_queue.pop()
            end_time = max(end_time, start + int(t2))
            read(int(A), int(B))
            status = 1

        return end_time, status

    time_tick = 0
    while process_queue:

        if time_tick > end_time:
            status = 0

        if len(process_queue[0].split(" ")) == 5:
            command, t1, t2, A, B = process_queue[0].split(" ")
        else:
            command, t1, t2, A, B, C = process_queue[0].split(" ")

        if int(t1) == time_tick:
            process_queue.popleft()
            if command == "read":
                if status == 1 and not write_wait_queue:
                    end_time = max(end_time, int(t1) + int(t2) - 1)
                    status = 1
                    read(int(A), int(B))
                else:
                    read_wait_queue.append((command, t1, t2, A, B))

            else:
                if status:
                    write_wait_queue.append((command, t1, t2, A, B, C))
                else:
                    write(int(A), int(B), C)


        if time_tick == end_time + 1 or status == 0:
            end_time, status = handle_wait_queue(end_time, status)

        time_tick += 1

    return read_results + [str(end_time)]

answer1 = solution(["1","2","4","3","3","4","1","5"], 	["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"])
print(answer1)

answer2 = solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"])
print(answer2)




