"""
1259.금속막대
"""
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    an = list(map(int,input().split()))
    bn = []

    kn = []
    vn = []
    for i in range(n):
        kn.append(an[i*2])
        vn.append(an[i*2+1])

    # 첫번째 노드 찾기
    pt = 0
    for i in range(n) :
        if kn[i] not in vn :
            pt = i
            bn.append(kn[pt])
            bn.append(vn[pt])
            break
    # 나머지 돌리기
    while len(bn) < n*2 :
        if vn[pt] in kn :
            pt = kn.index(vn[pt])
            bn.append(kn[pt])
            bn.append(vn[pt])


    print(f'#{test_case} {" ".join(map(str,bn))}')

        

        

 