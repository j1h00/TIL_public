def solution(atmos):
    mask_left = 0
    total_mask = 0
    for dust, micro_dust in atmos:
    
        if dust <= 80 and micro_dust <= 35:
            pass
        elif not mask_left and dust >= 151 and micro_dust >= 76:
            total_mask += 1
            mask_left = 1
        elif mask_left and dust >= 151 and micro_dust >= 76:
            mask_left = 0
        elif not mask_left:
            total_mask += 1
            mask_left = 3

        if mask_left > 0:
            mask_left -= 1

    return total_mask


answer1 = solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]])
print(answer1)

answer3 = solution([[30, 15], [80, 35]])
print(answer3)

answer2 = solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]])
print(answer2)
