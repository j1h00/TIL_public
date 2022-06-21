def solution(periods, payments, estimates):
    answer = [0, 0]

    ps = [24, 60] # Period Standard

    pv_dict = {
        24: 900000,
        60: 600000, 
    } # period-vip dict

    for i in range(len(periods)):
        period = periods[i]
        payment = payments[i]
        estimate = estimates[i]

        cur_payment = sum(payment)
        nxt_payment = cur_payment - payment[0] + estimate if len(payment) == 12 else cur_payment + estimate
        
        if period < ps[0]: # 기간이 2년 미만인 경우, 이번 달은 VIP 아님. 
            if period == ps[0] - 1 and nxt_payment >= pv_dict[ps[0]]: # 다음 달에 2년 이상이고, VIP 조건 만족하는 경우
                answer[0] += 1
                continue
            continue

        if ps[0] <= period < ps[1]: # 기간이 2년 이상 5년 미만인 경우 
           
            # 이번 달은 아니지만, 다음 달에 VIP 가 될 수 있는 경우 
            if cur_payment < pv_dict[ps[0]]:
                # 1. 다음 달에 5년 이상이고, VIP 조건 만족하는 경우
                if period == ps[1] - 1 and nxt_payment >= pv_dict[ps[1]]:
                    answer[0] += 1
                    continue
                # 1. 다음 달에 5년 미만이지만, VIP 조건 만족하는 경우 
                if nxt_payment >= pv_dict[ps[0]]:
                    answer[0] += 1
                    continue

            # 이번 달 VIP 이지만, 다음 달은 아닌 경우
            if cur_payment >= pv_dict[ps[0]]:
                if period == ps[1] - 1 and nxt_payment < pv_dict[ps[1]]:
                    answer[1] += 1
                    continue
                if nxt_payment < pv_dict[ps[0]]:
                    answer[1] += 1
                    continue
            continue
        
        if ps[1] <= period: # 5년 이상인 경우
            # 이번 달은 아니지만, 다음 달에 VIP 가 될 수 있는 경우 
            if cur_payment < pv_dict[ps[1]] and nxt_payment >= pv_dict[ps[1]]:
                answer[0] += 1
                continue

            # 이번 달 VIP 이지만, 다음 달은 아닌 경우 
            if cur_payment >= pv_dict[ps[1]] and nxt_payment < pv_dict[ps[1]]:
                answer[1] += 1
                continue
            continue

        return answer

            
                


            
        

            

    return answer