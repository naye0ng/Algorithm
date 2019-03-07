"""
10163.색종이
"""
N = int(input())
space = [[0]*101 for _ in range(101)]
size = [[0]]*N

for n in range(N) :
    size[n] = list(map(int,input().split()))
    for dx in range(size[n][2]) :
        for dy in range(size[n][3]) :
            space[size[n][0]+dx][size[n][1]+dy] = n+1

for i in range(N) :
    x = size[i][0]
    y = size[i][1]
    w = size[i][2]
    h = size[i][3]

    total = 0
    for dx in range(w) :
        for dy in range(h) :
            if space[x+dx][y+dy] ==  i+1 :
                total+=1
    print(total)

