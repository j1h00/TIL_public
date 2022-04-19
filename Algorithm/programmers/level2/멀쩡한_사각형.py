import math

def solution(w,h):
    ratio = h / w
    ratio_ceil = math.ceil(ratio)

    return w * (h - ratio_ceil)


answer1 = solution(8, 12)

print(answer1)
