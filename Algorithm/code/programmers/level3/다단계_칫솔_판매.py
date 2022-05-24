def solution(enroll, referral, seller, amount):
    parent = {} 
    result = {}

    N = len(enroll)
    for i in range(N):
        parent[enroll[i]] = referral[i]
        result[enroll[i]] = 0

    for i in range(len(seller)):
        total = amount[i] * 100 
        distribution = total // 10
        income = total - distribution
        result[seller[i]] += income
        p = parent[seller[i]] 
        
        while distribution > 0 and p != "-":
            total = distribution
            distribution = total // 10
            income = total - distribution

            result[p] += income
            p = parent[p]

    return list(result.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))