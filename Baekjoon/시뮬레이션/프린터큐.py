'''
프린터큐
https://www.acmicpc.net/problem/1966
'''
test_case = int(input())
for _ in range(test_case) :
    N, M = map(int, input().split())
    numbers = list(map(int,input().split()))
    out_order = [0]*N

    front, out = 0, 0
    while out < N :
        bigger_exist = False
        for i in range(1, N) :
            if out_order[(front+i)%N] == 0 and numbers[(front+i)%N] > numbers[front] :
                front = (front+i)%N
                bigger_exist = True
                break
        if bigger_exist : continue

        out += 1
        out_order[front] = out

        for i in range(1, N) :
            if out_order[(front+i)%N] == 0 :
                front = (front+i)%N
                break
        
    print(out_order[M])
   
        
'''
1
38 29
7 1 8 4 7 1 3 4 6 5 7 8 3 2 8 5 9 4 6 8 2 1 8 7 4 8 5 3 7 6 3 4 6 1 5 2 8 5

답 15
'''