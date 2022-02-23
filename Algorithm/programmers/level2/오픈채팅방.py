def solution(record):
    answer = []
    dict = {}
    for sentence in record:
        words = sentence.split(" ")
        if words[0] == "Enter":
            dict[words[1]] = words[2]
        elif words[0] == "Change":
            dict[words[1]] = words[2]
    for sentence in record:
        words = sentence.split(" ")
        if words[0] == "Enter":
            answer.append(dict[words[1]] + "님이 들어왔습니다.")
        elif words[0] == "Leave":
            answer.append(dict[words[1]] + "님이 나갔습니다.")
    return answer