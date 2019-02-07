"""
2005.파스칼의 삼각형

- 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
"""
# 삼각형의 크기가 주어졌으므로 미리 만들어 놓고 시작
def triangle() :
    triangles = [[1],[1,1]]
    for i in range(2,11):
        sub = [1 for k in range(i+1)]
        for j in range(1,len(sub)-1) :
            sub[j] = triangles[i-1][j-1]+triangles[i-1][j]
        triangles.append(sub)
    
    return triangles

tt = triangle() 

T = int(input())
for test_case in range(1, T+1) :
    n = int(input())
    print(f'#{test_case}')
    for i in range(n) :
        print(" ".join(map(str,tt[i])))

        

