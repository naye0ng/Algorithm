dx = [1, 0, -1]
dy = [0, 1, -1]
def is_not_wall(x, y, N) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= N : return False
    return True

def solution(n):
    layers = [[0]*k for k in range(1,n+1)]

    x, y, d, number = 0, 0, 0, 1
    while True :
        layers[x][y] = number
        is_end = True
        for i in range(3) :
            if x+dx[(d+i)%3] < len(layers) and is_not_wall(x+dx[(d+i)%3], y+dy[(d+i)%3], x+dx[(d+i)%3]+1) and layers[x+dx[(d+i)%3]][y+dy[(d+i)%3]] == 0 :
                x += dx[(d+i)%3]
                y += dy[(d+i)%3]
                d = (d+i)%3
                is_end = False
                break

        if is_end :
            break

        number += 1


    answer = []
    for layer in layers :
        answer.extend(layer)
    return answer


print(solution(100))

