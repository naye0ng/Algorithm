def solution(gems):
    type_of_gem = { key:0 for key in set(gems)}
    T = len(type_of_gem)

    start, end, dist = 0,0,len(gems)
    for i in range(len(gems)) :
        # if type_of_gem[gems[i]] == 0 :
        #     T -= 1
        type_of_gem[gems[i]] = i+1
        
        if T == 0 :
            s, e = min(type_of_gem.values()), max(type_of_gem.values())
            if e-s < dist :
                start, end, dist = s, e, e-s
    return [start, end]


print(solution(["AA", "AB", "AC", "AA", "AC"]))