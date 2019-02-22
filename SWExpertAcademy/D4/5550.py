"""
5550.나는 개구리로소이다.

"""


T = int(input())

for test_case in range(1, T + 1):
    an = input().replace(""," ").split()

    count = 1
    result = [[]]
    for a in an :
        if a == 'c' :
            check = 1
            for i in range(len(result)) :
                if result[i] == [] :
                    result[i].append(a)
                    check = 0
                    break
            if check :
                count += 1
                result.append([a])
        elif a == 'r' :
            check = 1
            for i in range(len(result)) :
                if len(result[i]) == 1 and result[i][0] == 'c' :
                    result[i].append(a)
                    check = 0
                    break
            if check :
                count = -1
                break
        elif a == 'o' :
            check = 1
            for i in range(len(result)) :
                if len(result[i]) == 2 and result[i][1] == 'r' :
                    result[i].append(a)
                    check = 0
                    break
            if check :
                count = -1
                break               
        elif a == 'a' :
            check = 1
            for i in range(len(result)) :
                if len(result[i]) == 3 and result[i][2] == 'o' :
                    result[i].append(a)
                    check = 0
                    break
            if check :
                count = -1
                break                           
        elif a == 'k' :
            check = 1
            for i in range(len(result)) :
                if len(result[i]) == 4 and result[i][3] is 'a' :
                    # 해당 리스트 원소 제거
                    result[i] = []
                    check = 0
                    break
            if check :
                count = -1
                break 

    # 빈배열이 아닌 것이 있다면 망이야.
    for i in result :
        if len(i) != 0 :
            count = -1
            break
            
    print(f'#{test_case} {count}')

