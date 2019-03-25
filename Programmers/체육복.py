"""
체육복
"""
maxNum = 0
def share(p,n,num, clothes) :
    if p >= n :
        global maxNum
        if num > maxNum :
            maxNum = num
    else :
        if clothes[p] != 0 :
            num += 1
        if clothes[p] == 2 :
            # 앞
            check = 0
            if p-1 >= 0 and clothes[p-1] == 0 :
                check += 1
                clothes[p-1] +=1
                clothes[p] -= 1
                # 이전꺼에 +1하므로 num값 증가
                share(p+1,n,num+1,clothes)
                clothes[p] += 1
                clothes[p-1] -= 1
            if p+1 < n and clothes[p+1] == 0 :
                check += 1
                clothes[p+1] +=1
                clothes[p] -= 1
                # 코드 줄이기 가능, +2로 점프
                share(p+2,n,num+1,clothes)
                clothes[p] += 1
                clothes[p+1] -= 1
            # 양 옆에 옷 줄곳이 없는 경우
            if check == 0 :
                share(p + 1, n, num, clothes)
        else :
            share(p+1,n,num,clothes)

def solution(n, lost, reserve):
    clothes = [1]*n
    for r in reserve :
        clothes[r-1] += 1
    for l in lost :
        clothes[l-1] -= 1

    share(0,n,0,clothes)
    return maxNum

print(solution(	5, [1,2,5], [1, 3, 5]))