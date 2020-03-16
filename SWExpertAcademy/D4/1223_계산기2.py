"""
계산기2
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD&categoryId=AV14nnAaAFACFAYD&categoryType=CODE

[중위 표기법 => 후위 표기법 변환]
1) 피연산자가 들어오면 바로 출력합니다.
2) 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담습니다.

3+4+5*6+7

34 +
34+ +
34+5 +
34+5 *+
34+56*+ +

34+56*+7+
"""
for test_case in range(1, 11):
    L = int(input())
    S = " ".join(input()).split()

    # [1] 후위 표기법 저장
    idx = 0
    notation = [0]*L
    opers = []

    for i in range(L) :
        if S[i] == '*' :
            while opers :
                # 자신보다 우선 순위가 낮은 건 그대로
                if opers[-1] == '+':
                    break
                # 우선 순위가 높거나 같은건 빼서 배열에 넣기
                notation[idx] = opers.pop()
                idx += 1
            opers.append(S[i])           

        elif S[i] == "+" :
            while opers :
                # 우선 순위가 높거나 같은건 빼서 배열에 넣기
                notation[idx] = opers.pop()
                idx += 1
            opers.append(S[i])  
        else :
            notation[idx] = int(S[i])
            idx += 1
    # 남은 연산자 넣기
    while opers :
        notation[idx] = opers.pop()
        idx += 1
    
    # [2] 후위 표기법 연산
    stack = []
    for i in range(L) :
        if notation[i] == "*" :
            stack.append(stack.pop()*stack.pop())
        elif notation[i]  == "+" :
            stack.append(stack.pop()+stack.pop())
        else :
            stack.append(notation[i])

    print(f'#{test_case} {stack[0]}')