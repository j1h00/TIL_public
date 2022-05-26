import collections

def solution(participant, completion):
    answer = ""
    part_dict = collections.Counter(participant)
    for c in completion:
        if c in part_dict:
            part_dict[c] -= 1
    
    for name, count in part_dict.items():
        if count > 0:
            answer = name 
            break 

    return answer


# fail 

# import collections

# def solution(participant, completion):
#     answer = "" 
#     subtracted = list(set(participant) - set(completion))
#     if len(subtracted):
#         answer = subtracted[0]
#     else:
#         part_dict = collections.Counter(participant)
#         for name, count in part_dict.items():
#             if count > 1:
#                 answer = name 

#     return answer
