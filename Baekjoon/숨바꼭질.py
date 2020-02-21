"""
숨바꼭질
https://www.acmicpc.net/problem/1697
"""
def jump() :
    """
    t-N < 0 이여도 -1로 움직일 수 있다.
    """
    time = [ t-N if t >= N else (t-N)*(-1) for t in range(100001)]
    for i in range(N,100001) :
        t = time[i]
        if i-1 >= 0 :
            t = min(t, time[i-1]+1)
        if i+1 <= 100000 :
            t = min(t, time[i+1]+1)
        if i%2 == 0 and i//2 >= 0 :
            t = min(t, time[i//2]+1)
        if i*2 <= 100000 :
            t = min(t, time[i*2]+1)

        time[i] = t

        if i-1 >= 0 :
            time[i-1] = min(t+1,time[i-1])
        if i+1 <= 100000 :
            time[i+1] = min(t+1,time[i+1])
        if i%2 == 0 and i//2 >= 0 :
            time[i//2] = min(t+1, time[i//2])
        if i*2 <= 100000 :
            time[i*2] = min(t+1, time[i*2])
    return time[K]


N, K = map(int, input().split())
# [1] 수빈 >= 동생
if N >= K :
    print(N-K)
# [2] 수빈 < 동생 
else :
    print(jump())
