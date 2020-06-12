N, K = map(int,input().split())

length = []
stick = []
k = K-N+1
for _ in range(N) :
    f = float(input())
    stick.append(f)
    length.extend([float(format(f/i, '.4f')[:5]) for i in range(2, k+1)])

# TODO : 이분탐색으로 고치기
stick.sort(reverse=True)
for l in sorted(length, reverse=True) :
    cnt = 0
    for i in range(N) :
        c = int(stick[i]//l)
        if c == 0 :
            break
        cnt += c
    if cnt >= K :
        print(format(round(l,2),'.2f'))
        break