"""
1983.조교의 성적 매기기
"""
import math 

T = int(input())
for test_case in range(1,T+1):
    n, k =map(int,input().split())
    result = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    scores = []
    for i in range(n) :
        subject = list(map(int,input().split()))
        scores += [subject[0]*0.35+subject[1]*0.45+subject[2]*0.2]

    value = scores[k-1]
    scores.sort(reverse=True)
    
    print(f'#{test_case} {result[math.ceil((scores.index(value)+1)/(n//10))-1]}')


