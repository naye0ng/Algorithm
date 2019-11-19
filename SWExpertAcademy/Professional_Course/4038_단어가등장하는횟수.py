"""
4038 - 단어가 등장하는 횟수
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
https://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220927272165
"""
def rabin(S,W) :
    w = 0
    for w in W :
        w += ord(w)
    s = 0
    for i in range(len(W)) :
        s += ord(S[i])*
    i = 1
    while i <= len(S)-len(W)+1 :
        ()
    




T = int(input())
for test_case in range(1,T+1) :
    S = input()
    W = input()
    
    print('#{} {}'.format(test_case,rabin(S,W)))