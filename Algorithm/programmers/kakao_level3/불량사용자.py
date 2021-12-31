import re # regex module 
import itertools

def solution(user_id, banned_id):
    possible = {}
    if len(user_id) == len(banned_id):
        return 1
    for i, banned in enumerate(banned_id):
        reg_banned = re.compile(banned.replace("*", ".")) # return regex object
        possible[i] = []
        for user in user_id:
            m = reg_banned.match(user) # if regex match current user
            if len(banned) == len(user) and m: # and also matches length
                possible[i].append(user) 

    result = list(itertools.product(*possible.values())) 
    result2 = []
    result2 = [set(e) for e in result if (set(e) not in result2) and (len(set(e)) == len(banned_id))]
    new = []
    for i in result2:
        if i not in new:
            new.append(i)
    return len(new)