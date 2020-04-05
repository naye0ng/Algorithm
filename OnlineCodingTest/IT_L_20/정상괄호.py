def solution(inputString):
    answer = 0
    opened = [0]*4

    for i in range(len(inputString)) :
        if inputString[i] == "(" :
            opened[0] += 1
        elif inputString[i] == "{" :
            opened[1] += 1
        elif inputString[i] == "[" :
            opened[2] += 1
        elif inputString[i] == "<" :
            opened[3] += 1

        elif inputString[i] == ")" :
            if opened[0] >= 1 :
                opened[0] -= 1
                answer += 1
            else : 
                return -1
        elif inputString[i] == "}" :
            if opened[1] >= 1 :
                opened[1] -= 1
                answer += 1
            else : 
                return -1
        elif inputString[i] == "]" :
            if opened[2] >= 1 :
                opened[2] -= 1
                answer += 1
            else : 
                return -1
        elif inputString[i] == ">" :
            if opened[3] >= 1 :
                opened[3] -= 1
                answer += 1
            else : 
                return -1
    
    return answer

print(solution("([)]"))