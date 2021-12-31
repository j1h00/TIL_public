N, M = map(int, input().split())

n_cut = int(input())

r_cuts = [0, M]
c_cuts = [0, N]
for i in range(n_cut):
    rc, num = map(int, input().split())
    if rc:
        c_cuts.append(num)
    else:
        r_cuts.append(num)

r_cuts.sort()
c_cuts.sort()

r_max = 0 
c_max = 0
for i in range(len(r_cuts)-1):
    r_max = max(r_cuts[i+1] - r_cuts[i], r_max)
for j in range(len(c_cuts)-1):
    c_max = max(c_cuts[j+1] - c_cuts[j], c_max)

print(r_max * c_max)

