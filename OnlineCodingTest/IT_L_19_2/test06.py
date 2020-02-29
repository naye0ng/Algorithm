# 시작x,y, 크기 k
def draw0(x,y,t,k) :
    for i in range(2*k-1) :
        for j in range(k) :
            if j == k-1 : board[x+i][t][y+j] = '#'
            else : board[x+i][t][y+j] = '.'

N, O = input().strip().split(' ')
N = int(N)
size , numbers = [], []
for _ in range(N) :
    s, n = input().strip().split(' ')
    s = int(s)
    size.append(s)
    numbers.append(n)
board = [ [ [ ['.']*w for w in size ] for i in range(N) ] for _ in range(max(size)*2-1)]

#  TODO : TOP, MIDDEL, BOTTOM 조절
x, y = 0, 0
for i in range(N) :
    for number in numbers :
        for j in range(len(number)) :
            if number[j] == '1' :
                draw0(x,y,i,size[i])
    


for i in range(max(size)*2-1) :
    print(board[i])
