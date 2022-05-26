for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4= map(int, input().split())
    x = (set(range(x1, x2+1)), set(range(x3, x4+1)))
    y = (set(range(y1, y2+1)), set(range(y3, y4+1)))
    common = [x[0] & x[1], y[0] & y[1]] 
    
    if len(common[0]) == 0 or len(common[1]) == 0:
        print('d')
    elif len(common[0]) * len(common[1]) == 1:
        print('c')
    elif len(common[0]) == 1 or len(common[1]) == 1:
        print('b')
    else:
        print('a')