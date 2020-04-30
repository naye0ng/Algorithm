p1 = [1,2,3,4,5]
p2 = [2,1,2,3,2,4,2,5]
p3 = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    s1, s2, s3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == p1[i%5] :
            s1 += 1
        if answers[i] == p2[i%8] :
            s2 += 1
        if answers[i] == p3[i%10] :
            s3 += 1
    
    S = max(s1,s2,s3)
    answer = []
    if S == s1 :
        answer.append(1)
    if S == s2 :
        answer.append(2)
    if S == s3 :
        answer.append(3)

    return answer
        