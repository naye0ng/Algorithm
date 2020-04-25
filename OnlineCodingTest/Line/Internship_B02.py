def collection(N,depth,n):
    if N == depth :
        target.append(n)
    else :
        for i in range(N) :
            if visited[i] == False :
                visited[i] = True
                collection(N,depth+1,n+numbers[i]*(10**(depth)))
                visited[i] = False


# 입력
numbers = list(map(int,input().strip().split(' ')))
k = int(input())

# 수열
target = []
N = len(numbers)
visited = [False]*N
collection(N,0,0)

target.sort()
result = str(target[k-1])
print("0"*(N-len(result))+result)