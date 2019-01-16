"""
4828.min max
"""
t = int(input())

for i in range(1,t+1) :
    n = int(input())
    an = list(map(int, input().split()))
    
    print(f'#{i} {max(an)-min(an)}')
