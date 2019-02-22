"""
1979.어디에 단어가 들어갈 수 있을까
"""
# 아래로
def down(x,y,length) :
    # 갈 곳이 있다면
    if x+1 != n and blanks[x+1][y] !=0 :
        # 지나왔음을 마킹
        blanks[x+1][y] -=1
        length += 1
        return down(x+1,y,length)
    return length

# 오른쪽으로 
def right(x,y,length) :
    # 갈 곳이 있다면
    if y+1 != n and blanks[x][y+1] !=0 :
        # 지나왔음을 마킹
        blanks[x][y+1] -=2
        length += 1
        return right(x,y+1,length)
    return length

T = int(input())
for test_case in range(1, T+1) :
    n, k = map(int,input().split())
    blanks = [ [ 3 if i==1  else i for i in map(int,input().split()) ] for _ in range(n)]
    numBlank = {i:0 for i in range(1,n+1)}
  
    for x in range(n) :
        for y in range(n) :
            if blanks[x][y] == 0 :
                continue
            if blanks[x][y] == 3 :
                numBlank[down(x,y,1)] +=1
                numBlank[right(x,y,1)] +=1
            elif blanks[x][y] == 2 :
                numBlank[right(x,y,1)] +=1
            elif blanks[x][y] == 1 :
                numBlank[down(x,y,1)] +=1


    print(f'#{test_case} {numBlank[k]}')