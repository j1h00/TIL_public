def solution(s):
    remove = ["}", "{", ","]
    L = s[2:-2].split("},{")
    L2 = [i.split(",") for i in L]
    L3 = sorted(L2, key = lambda x: len(x))
    answer = []
    for l in L3:
        for i in l:
            if int(i) not in answer:
                answer.append(int(i))
    return answer