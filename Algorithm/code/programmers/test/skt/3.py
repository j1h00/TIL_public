def solution(n, plans, clients):
    m = len(plans)
    answer = [0] * len(clients)

    plans_dict = {}
    for i, plan in enumerate(plans): # plans 를 parsing 
        plan_list = plan.split(" ")
        data, add = plan_list[0], plan_list[1:]
        if i in plans_dict:
            add += plans_dict[i][1]
        plans_dict[i+1] = [int(data), add]
    
    for i, client in enumerate(clients): # clients 를 parsing
        client_list = client.split(" ")
        data, add = int(client_list[0]), client_list[1:]
        for key, value in plans_dict.items(): # 어느 plan 에 해당하는지 찾는다. 
            plan_data, plan_add = value[0], value[1]
            
            if plan_data >= data and set(add).issubset(set(plan_add)):
                answer[i] = key
                break

    return answer