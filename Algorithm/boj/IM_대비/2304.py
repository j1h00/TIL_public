def make_warehouse(loop):
    now = 0
    for i in loop:
        if arr[i] > now:
            now = arr[i]
        warehouse[i] = now

N = int(input())

warehouse = [0]*1001
arr = [0] * 1001
max_h = 0
max_idx = 0 
for i in range(N):
    idx, h = map(int, input().split())
    arr[idx] = h 
    if h > max_h:
        max_h = h
        max_idx = idx 


    make_warehouse(range(max_idx+1))
    make_warehouse(range(1000, max_idx, -1))
print(sum(warehouse))
