def solution(s):
    target = s[2:-2].split("},{")
    tuple_set = [0]*(len(target)+1)

    for t in target:
        subSet = t.split(",")
        tuple_set[len(subSet)] = list(map(int,subSet))

    answer = tuple_set[1]
    for i in range(2, len(tuple_set)) :
        for t in tuple_set[i] :
            if t not in answer :
                answer.append(t)
                break
        
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))