"""
4839.이진탐색
"""
def search(l,r,c,ab):
    if ab == c :
        return 1
    elif ab < c :
        r = c
        c = (l+r)//2
        return search(l,r,c,ab)+1
    elif ab > c :
        l = c
        c = (l+r)//2
        return search(l,r,c,ab)+1


T = int(input())

for test_case in range(1, T + 1):
    p, a, b = map(int,input().split())
    c = p//2
    
    ra = search(1,p,c,a)
    rb = search(1,p,c,b)

    winner = 'A'
    if ra > rb :
        winner = 'B'
    elif ra ==rb :
        winner = 0

    print(f'#{test_case} {winner}')