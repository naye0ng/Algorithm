"""
재귀함수를 이용한 순열생성

- a의 숫자에서 R개의 순열을 뽑아내기
"""
a =[1,2,3]
R = 2

N = len(a)
visited = [False]*N
t = [0]*R

def perm(k) :
    if k == R :
        print(t)
    else :
        for i in range(N) :
            if visited[i] :
                continue
            t[k] = a[i]
            visited[i] = True
            perm(k+1)
            visited[i] = False
perm(0)