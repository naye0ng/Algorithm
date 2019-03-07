"""
5356.의석이의 세로로 말해요
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,1+T):
    words = [input().replace(""," ").split() for _ in range(5)]
    length = [len(words[i]) for i in range(5)]
    maxlen = max(length)
    result = ""
    for y in range(maxlen) :
        for x in range(5) :
            if y >= length[x] :
                continue
            else :
                result += words[x][y]

    print('#{} {}'.format(test_case, result))
