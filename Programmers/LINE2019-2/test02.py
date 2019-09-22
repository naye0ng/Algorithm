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

"""
입력 형식
- 첫 번째 행에 공백(space)을 구분자로 숫자가 주어진다
- 각 숫자는 한 자리 숫자로 주어진다 (0과 같거나 크고, 10보다 작은 숫자)
같은 숫자가 중복되어 나타나지 않는다
두 번째 행에 찾으려는 수열의 순서(k)가 주어진다
k는 조합된 순열의 개수보다 크거나 작지 않다
출력 형식
조합된 순열을 오름차순으로 정렬 했을 때 k번째 순열
맨 앞자리가 0인 경우는 0을 그대로 유지한다
입출력 예제
"""