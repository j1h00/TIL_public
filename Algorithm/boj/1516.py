from collections import deque 

# initialize
N = int(input())
d = { k:[] for k in range(1, N+1) } # d for dependencies
for a in range(1, N+1):
    info = input().split()
    time = info[0]
    for b in info[1:]:
        if b == "-1":
            break 
        else:
            d[a].append(int(b))


# use stack 
stack = []
visited = [[0] for _ in range(N+1)]
for i in range(1, N+1):
    if not d[i]:
        stack.append(i)
        visited[i] = 1
        continue
    else:
  
            
print(d)
            
        
        