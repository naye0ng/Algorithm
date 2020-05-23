import math
def solution(x1, y1, r, d, target):  
    angle = math.atan2(y1,x1)*(180/3.14)
    min_bound = angle-d if angle-d >= 0 else (180+(-1)*angle-d)%360
    max_bound = angle+d if angle+d >= 0 else (180+(-1)*angle+d)%360

    answer = 0
    for x2, y2 in target :
        # [1] 범위
        if math.sqrt((x2*x2)+(y2*y2)) <= r :
            # [2] 각도
            a = math.atan2(y2,x2)*(180/3.14)
            angle2 = a if a >= 0 else (180+(-1)*a)%360
            if min_bound <= angle2 <= max_bound :
                answer += 1

    return answer

print(solution(-2, 0, 3, 60, [[-1,2]]))

print(solution(0, -2, 3, 60, [[-1,-1]]))