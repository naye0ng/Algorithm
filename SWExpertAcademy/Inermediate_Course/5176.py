"""
5176.이진탐색
"""

def searchValue(index,target, n=0) :
    nextTarget = []

    for i in range(len(target)) :
        if len(target[i]) == 1 :
            pm = 0
            n+=1
        elif len(target[i]) == 2 :
            # 두개 남으면 두번째가 선택됨, 첫번째 값 삽입
            nextTarget.append(target[i][:1])
            pm =1
            n+=1
        else :
            pl = 0
            pr = len(target[i])
            pm = (pl+pr)//2
            nextTarget.append(target[i][:pm])
            nextTarget.append(target[i][pm+1:])
            n +=1

        # 트리에서 알고 싶은 값
        if n == index :
            # target[i][pm]이 결국 이번 순서에서 삽입될 값
            return target[i][pm]
    if len(nextTarget) :
        return searchValue(index, nextTarget, n)

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    searchList = [ i for i in range(1,N+1) ]

    print('#{} {} {}'.format(test_case,searchValue(1,[searchList]),searchValue(N//2,[searchList])))
