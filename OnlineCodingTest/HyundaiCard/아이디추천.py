def solution(registered_list, new_id):
    if new_id not in registered_list :
        return new_id
    
    S, N = '', 0
    for i in range(len(new_id)) :
        if ord(new_id[i]) >= 97 and ord(new_id[i]) <= 122 :
            S += new_id[i]
        else :
            N = int(new_id[i:])
            break

    return solution(registered_list, S+str(N+1))

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))