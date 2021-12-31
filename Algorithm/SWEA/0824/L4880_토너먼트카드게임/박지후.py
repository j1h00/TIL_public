import sys
sys.stdin = open('input.txt')

# 가위바위보 승자를 리턴합니다.
def rsp(a, b):
    if a[1] == 3 and b[1] == 1:
        return b
    elif b[1] == 3 and a[1] == 1:
        return a
    else: # 가위 < 바위 < 보
        if a[1] >= b[1]:
            return a
        else:
            return b

# 토너먼트를 합니다. 만약 학생 수가 1명이면 승자는 그 학생, 2명이면 둘 중 가위바위보의 승자를 리턴합니다.
# 만약 학생 수가 2명 보다 많으면, 그룹을 나누어 토너먼트를 진행합니다.
def tournament(students): # students 의 원소는 (idx, card) 형태
    if len(students) == 1:
        return students[0]
    elif len(students) == 2:
        winner = rsp(students[0], students[1])
        return winner
    else:
        left = students[:(len(students)+1)//2]  # 왼쪽 그룹
        right = students[(len(students)+1)//2:] # 오른쪽 그룹
        left_winner = tournament(left) #
        right_winner = tournament(right)
        return rsp(left_winner, right_winner)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    # tournament 에 학생의 인덱스값과 가위바위보 값을 모두 넘겨주기 위해 (idx, card) 를 사용합니다.
    students = []
    for idx, card in enumerate(cards):
        students.append((idx, card))

    winner = tournament(students)

    print(f'#{tc} {winner[0]+1}')
    
    