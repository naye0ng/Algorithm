def solution(p,s):
    number = list(map(int," ".join(p).split()))
    passwd = list(map(int," ".join(s).split()))
    
    answer = 0
    for i in range(len(number)) :
        answer += min(number[i]+(9-passwd[i])+1,(9-number[i])+passwd[i]+1,abs(number[i]-passwd[i]))

    return answer

print(solution("82195", "64723"))