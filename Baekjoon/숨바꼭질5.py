"""
숨바꼭질5
https://www.acmicpc.net/problem/17071
---
[2019 하반기 라인 코딩테스트]
https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/?fbclid=IwAR1ir65FqVmmCcdn-5JaF78lO2BmPY7-F3h9HciuB4_CBp_XwhCdDzseaAo
"""
# BFS로 풀어보자
T = 500000
def catch_cony(cony, brown) :
    global T
    queue = []
    queue.append(brown)
    t = 0
    while t < T and cony <= 500000:
        cony += t
        for _ in range(len(queue)) :
            B = queue.pop(0)
            if B == cony :
                T = t
                break
            else : 
                if B+1 <= 500000 :
                    queue.append(B+1)
                if B-1 > 0 :
                    queue.append(B-1)
                if B*2 <= 500000 :
                    queue.append(B*2)
        t += 1

brown, cony = map(int, input().split())
catch_cony(cony, brown)
if T == 500000 :
    print(-1)
else :
    print(T)


"""
[입력]
1396 388270
[답]
451
"""