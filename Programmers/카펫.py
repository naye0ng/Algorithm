"""
카펫
"""
def solution(brown, red):
    for i in range(1,int(red**(1/2))+1) :
        height = i
        width = red/i
        if (height+width)*2+4 == brown :
            return [int(width)+2, int(height)+2]

print(solution(10,2))