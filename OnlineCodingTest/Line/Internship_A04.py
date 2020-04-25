# 가장 긴것부터 아래로 내려가서 찾기
maxL,maxR = 0, 0
def left(i,width) :
    if i == 0 :
        global maxL
        maxL = width
    else :
        maxI= 0
        maxW, w =0,0
        #i-1 ~0까지 봤을때 가장 긴 값 찾기
        for k in range(i-1,-1,-1) :
            w+=1
            if maxI==0 or height[maxI]< height[k] :
                maxI = k
                maxW = w
        if width < maxW :
            left(maxI,maxW)
        else :
            left(maxI,width)

def right(i, width) :
    global N
    if i >= N-1 :
        global maxR
        maxR = width
    else :
        # i+1부터 N-1까지 중에 가장 긴 값
        maxI= 0
        maxW, w =0,0
        for k in range(i+1,N) :
            w+=1
            if maxI == 0 or height[maxI]< height[k] :
                maxI = k
                maxW = w
        if width < maxW :
            right(maxI,maxW)
        else :
            right(maxI,width)


N = int(input())
height = [int(input()) for _ in range(N)]

# 가장긴높이 찾기
maxH = 0
start = 0
for i in range(N) :
    if height[i] > maxH :
        maxH = height[i]
        start = i

left(start,0)
right(start,0)

print(max(maxL,maxR))
'''
10
8
4
7
4
3
2
9
7
12
8
'''