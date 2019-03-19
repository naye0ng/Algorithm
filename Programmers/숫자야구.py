"""
숫자야구
# 중복되는 수와 0은 포함되지 않아야 한다. >> 102, 121 이런거 안됨
- 입력: [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
- 결과: 2
"""
answer = 0
def match(t,baseball) :
    if len(baseball) == 0 :
        global answer
        answer+=1
    else :
        N = str(baseball[0][0])
        S = baseball[0][1]
        B = baseball[0][2]
        s, b = 0, 0
        for i in range(3) :
            # 스트라이크
            if N[i] == t[i] :
                s += 1
            # 볼체크
            if i == 0 :
                if N[1] == t[2] :
                    b += 1
                if N[2] == t[1] :
                    b += 1
            elif i == 1:
                if N[0] == t[2] :
                    b += 1
                if N[2] == t[0] :
                    b += 1
            elif i == 2:
                if N[0] == t[1] :
                    b += 1
                if N[1] == t[0] :
                    b += 1
            if S == s and B == b :
                match(t,baseball[1:])
                break
def is_ok(t) :
    if '0' in t :
        return False
    if t[0] in t[1:] or t[2] in t[:2] :
        return  False
    return True

def solution(baseball):
    global answer
    for t in range(111,1000) :
        # 중복 케이스와 0 포함하는 수 제거
        if is_ok(str(t)) :
            match(str(t),baseball)

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))