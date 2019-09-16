"""
3820 - 롤러코스터
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
"""

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    arr = [[0]*3 for _ in range(N)]
    for i in range(N) :
        a, b = map(int, input().split())
        arr[i] = [(a-1)/b,a,b]
    arr.sort(reverse=True)
    v = 1
    for i in range(N) :
        v = arr[i][1]*v + arr[i][2]
        v = v%(1000000007)
    print('#{} {}'.format(test_case,v))