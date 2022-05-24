# Time x: Go straight ym and turn direction
directions = {"E":0, "S":1, "W":2, "N":3}

def direction_check(d1, d2):
    if directions[d2] == (directions[d1] + 1) % 4:
        return "right"
    return "left"

def solution(path):
    answer = []
    i = 0
    total_len = len(path)
    while i < total_len:
        j = i 
        while j < total_len and path[j] == path[i]:
            j += 1

        if j == total_len:
            break

        if j-i > 5:
            time = str(j - 5) 
            now_d = direction_check(path[j-1], path[j])
            answer.append("Time " +  time + ": Go straight 500m and turn " + now_d)
        else:
            time = str(i)
            now_d = direction_check(path[j-1], path[j])
            now_len = str((j-i) * 100)
            answer.append("Time " +  time + ": Go straight " + now_len + "m and turn " + now_d)
        
        i = j 

solution("EEESEEEEEENNNN")
# solution("SSSSSSWWWNNNNNN")