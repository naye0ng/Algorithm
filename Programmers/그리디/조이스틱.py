"""
조이스틱
"""


def UpDown(name) :
    count = 0
    for i in range(len(name)):
        if name[i] == 'A' :
            continue
        c = ord(name[i]) - 65
        if c <=  13 :
            count += c
        else : 
            count += 26-c
    return count 

def LeftRight(name, before) :
    count = 0

    while True :
        left = right = indexR = indexL =30
        for i in range(1,len(name)//2+1) :
            if right == 30 and name[(before+i)%len(name)] != 'A' :
                indexR = (before+i)%len(name)
                right = i
            elif left == 30 and name[(before-i)%len(name)] != 'A' :
                indexL = (before-i)%len(name)
                left = i
            
        if right == 30 and left == 30 :
            break

        # 가장 가까운 곳으로 이동
        if right <= left :
            count += right
            name[indexR] = 'A'
            before = indexR
        else :
            count += left
            name[indexL] = 'A'
            before = indexL

    return count 

def solution(name):
    answer = 0
    name = list(name)

    answer += UpDown(name)
    name[0] = 'A'
    answer += LeftRight(name,0)
    return answer

print(solution("JAN"))

