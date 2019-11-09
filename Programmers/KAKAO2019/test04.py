def solution(k, room_number):
    answer = []
    rooms = [ i for i in range(k+1)]
    for number in room_number :
        index = 0
        while rooms :
            if rooms[index] >= number :
                answer.append(rooms[index])
                rooms.pop(index)
                break
            index += 1
    return answer

print(solution(10,[1,1,1,3,4,1,3,1]))

# def solution(k, room_number):
#     answer = []
#     visited = [False]*(k+1)
#     for number in room_number :
#         while number < k+1 :
#             if visited[number] == False :
#                 visited[number] = True
#                 answer.append(number)
#                 break
#             number += 1
  
#     return answer

# print(solution(10,[1,1,1,3,4,1,3,1]))