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
        # 스트라이크 체크
        visited = [0]*3
        for i in range(3) :
            if N[i] == t[i] :
                s += 1
                visited[i] = 1
        # 2st 이상일때 1b이 나올 수 없다!
        if sum(visited) < 2 :
            for j in range(3) :
                if visited[j] == 1 :
                    continue
                for k in range(3) :
                    if k == j :
                        continue
                    if t[j] == N[k] :
                        b+=1 
                        break
        # 전체 체크
        if S == s and B == b :
            match(t,baseball[1:])

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