def solution(number, k):
    stack = []
    erase_remain = k

    for i in range(len(number)):
        while stack and stack[-1] < number[i] and erase_remain:
            stack.pop()
            erase_remain -= 1

        if not erase_remain:
            stack += number[i:]
            break 

        stack.append(number[i])

    stack = stack[:-erase_remain] if erase_remain > 0 else stack 
    return "".join(stack)


answer1 = solution("1924", 2)
answer2 = solution("1231234", 3)
answer3 = solution("4177252841", 4)

print(answer1)
print(answer2)
print(answer3)