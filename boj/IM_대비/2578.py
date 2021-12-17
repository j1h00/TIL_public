def erase(x, arr, bingo):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == x:
                bingo[i][j] = 1


def check(bingo):
    cnt = 0 

    for row in bingo:
        if sum(row) == 5:
            cnt += 1

    for col in zip(*bingo):
        if sum(col) == 5:
            cnt += 1
    
    d1 = 0 
    d2 = 0 
    for i in range(5):
        if bingo[i][i]:
            d1 += 1
        if bingo[i][4-i]:
            d2 += 1

    if d1 == 5:
        cnt += 1
    if d2 == 5:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False
        

arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

call = []
for _ in range(5):
    call.extend(map(int, input().split()))

bingo = [[0]*5 for _ in range(5)]
for idx, x in enumerate(call):
    erase(x, arr, bingo)
    if check(bingo):
        print(idx + 1)
        break 

