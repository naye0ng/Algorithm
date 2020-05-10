keypad = {
    1:[0,0], 2:[0,1], 3:[0,2],
    4:[1,0], 5:[1,1], 6:[1,2],
    7:[2,0], 8:[2,1], 9:[2,2],
    '*':[3,0], 0:[3,1], '#':[3,2],
}
def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    for n in numbers :
        if n in [1,4,7] :
            left = n
            answer += 'L'
        elif n in [3,6,9] :
            right = n
            answer += 'R'
        else :
            DL = abs(keypad[left][0]-keypad[n][0])+abs(keypad[left][1]-keypad[n][1])
            DR = abs(keypad[right][0]-keypad[n][0])+abs(keypad[right][1]-keypad[n][1])
            if DL < DR :
                left = n
                answer += 'L'
            elif DL > DR :
                right = n
                answer += 'R'
            # DL == DR
            elif hand == 'left' :
                left = n
                answer += 'L'
            else :
                right = n
                answer += 'R'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))