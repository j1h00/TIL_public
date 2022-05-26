arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

# binary counting
subsets = [] 
for i in range(1<<n):

    temp = []
    total = 0 
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])
            total += arr[j]
    
    if total == 0:
        subsets.append(temp)

print(subsets)