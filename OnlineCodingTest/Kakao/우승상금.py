from itertools import permutations
import re

def solution(expression):
    number = list(map(int,re.findall(r"[\w']+", expression)))
    operator = re.findall(r"[\-',\+',\*']+", expression)

    answer = 0
    for p1, p2, p3 in list(permutations([1,2,3])) :
        priority = {"*":p1, "+":p2, "-":p3}

        num_stack = []
        oper_stack = []
        i, j = 0, 0
        while i < len(number) :
            num_stack.append(number[i])
            i += 1
            # 우선순위가 큰 연산자 계산
            if j < len(operator) :
                while oper_stack :
                    if priority[oper_stack[-1]] >= priority[operator[j]] :
                        oper = oper_stack.pop()
                        x2 = num_stack.pop()
                        x1 = num_stack.pop()
                        if oper == "*" :
                            num_stack.append(x1*x2)
                        elif oper == "+" :
                            num_stack.append(x1+x2)
                        elif oper == "-" :
                            num_stack.append(x1-x2)
                    else :
                        break
                oper_stack.append(operator[j])
                j += 1

        # 남은 계산
        while oper_stack :
            oper = oper_stack.pop()
            x2 = num_stack.pop()
            x1 = num_stack.pop()
            if oper == "*" :
                num_stack.append(x1*x2)
            elif oper == "+" :
                num_stack.append(x1+x2)
            elif oper == "-" :
                num_stack.append(x1-x2)
        answer = max(answer, abs(num_stack[0]))
    return answer
print(solution("50*6-3*2"))