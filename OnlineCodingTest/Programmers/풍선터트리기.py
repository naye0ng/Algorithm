def solution(a):
    N = len(a)
    leftMin = [0]*N
    rightMin = [0]*N
    leftMin[0] = a[0]
    rightMin[-1] = a[-1]
    for i in range(1, N) :
        leftMin[i] = min(a[i], leftMin[i-1]) 
        rightMin[N-i-1] = min(a[N-i-1], rightMin[N-i])
    
    answer = N
    for i in range(N) :
        if leftMin[i] < a[i] and a[i] > rightMin[i] : 
            answer -= 1
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))