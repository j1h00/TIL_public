
def tower(top, dices):
    key = [5, 3, 4, 1, 2, 0]
    cnt = 0
    total = 0 
    while cnt < len(dices):
        for idx, num in enumerate(dices[cnt]):
            if num == top:
                bottom_idx = idx
        top_idx = key[bottom_idx]

        bottom = dices[cnt][bottom_idx]
        top = dices[cnt][top_idx]

        now_max = 0
        for num in dices[cnt]:
            if num != bottom and num != top:
                now_max = max(now_max, num)
        total += now_max

        cnt += 1

    return total

N = int(input())
dices = []
for i in range(N):
    dices.append(list(map(int, input().split())))

answer = 0 
for i in range(1, 7):
    answer = max(tower(i, dices), answer)

print(answer)

