"""
5176.이진탐색
"""
import sys
sys.stdin = open('input.txt', 'r')

def inorder(t) :
    global n
    if t :
        inorder(tree[t][1])
        # 값 넣기
        tree[t][0] = n
        n+=1
        inorder(tree[t][2])

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    tree = [ [0]*3 for i in range(N+1) ]
    # 크기가 N인 완전 이진 트리
    for i in range(1,N+1) :
        if i*2 > N :
            break
        tree[i][1] = i*2
        if i*2+1 > N :
            break
        tree[i][2] = i*2+1

    n = 1
    inorder(1)
    print('#{} {} {}'.format(test_case,tree[1][0],tree[N//2][0]))

# def searchValue(index,target, n=0) :
#     nextTarget = []
#
#     for i in range(len(target)) :
#         if len(target[i]) == 1 :
#             pm = 0
#             n+=1
#         elif len(target[i]) == 2 :
#             # 두개 남으면 두번째가 선택됨, 첫번째 값 삽입
#             nextTarget.append(target[i][:1])
#             pm =1
#             n+=1
#         else :
#             pl = 0
#             pr = len(target[i])
#             pm = (pl+pr)//2
#             nextTarget.append(target[i][:pm])
#             nextTarget.append(target[i][pm+1:])
#             n +=1
#
#         # 트리에서 알고 싶은 값
#         if n == index :
#             # target[i][pm]이 결국 이번 순서에서 삽입될 값
#             return target[i][pm]
#     if len(nextTarget) :
#         return searchValue(index, nextTarget, n)


# # 같은 높이엔서 같이 처리
# def searchValue(target,index, check=1) :
#     nextTarget = []
#
#     for k in range(len(target)) :
#         if len(target[k]) == 1:
#             pm = 0
#             check +=1
#         elif len(target[k]) == 2 :
#             nextTarget.append(target[k][0])
#             pm = 1
#             check +=1
#         else :
#             pl = 0
#             pr = len(target[k])
#             pm = (pl+pr)//2
#             nextTarget.append(target[k][:pm])
#             nextTarget.append(target[k][pm+1:])
#             check += 1
#         if check == index :
#             return target[k][pm]
#     if len(nextTarget) :
#         return searchValue(nextTarget,index, check)
#
#
#
# # 1000이하까지 만들어 놓고 시작
# depth = [1]
# i = 0
# while i < 9 :
#     depth += [depth[i]+2**(i+1)]
#     i += 1
#
# T = int(input())
# for test_case in range(1,1+T) :
#     N = int(input())
#     searchList = [ i for i in range(1,N+1) ]
#
#     # 시작 높이 찾기
#     for h in range(len(depth)) :
#         if depth[h] >= N :
#             break
#     # 완전 이진 트리에서 루트 노드는 다음과 같다.
#     root = searchList[depth[h-1]]
#     middle = searchValue([searchList[:depth[h-1]],searchList[depth[h-1]+1:]], N//2)
#
#     print('#{} {} {}'.format(test_case, root, middle))