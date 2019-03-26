"""
후보키
"""
# set을 이용하자
# 작은 단위별로 조사
def solution(relation):
    l = len(relation)
    att = len(relation[0])
    visitied = [0] * att
    # 후보키가 가능한 부분집합 조사
    keys = [[] for _ in range(att)]
    for i in range(1 << att) :
        subkey = []
        for j in range(att) :
            if i & ( 1<< j) :
                subkey.append(j)
        if len(subkey) > 0 :
            keys[len(subkey)-1].append(subkey)

    # # 해당 튜플 검사하기 >> 이방법은 아닌듯하오!
    # for key in keys :
    #     for k in key :
    #


    # cols = []
    # for r in range(R) :
    #     local = set()
    #     for c in range(C) :
    #         local.add(relation[c][r])
    #     if len(local) == C  :
    #         visitied[r] = 1
    #         continue
    #     cols.append(local)
    # print(visitied)
    # print(cols)



    answer = 0
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))