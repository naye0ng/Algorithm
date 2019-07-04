"""
다리를 지나는 트럭
"""
def solution(bridge_length, weight, truck_weights):
    time = 0 
    queue = [0]*bridge_length 

    while queue :
        time += 1
        queue.pop(0)
        if truck_weights :
            if truck_weights[0] + sum(queue) <= weight :
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    return time

print(solution(2, 10, [7, 4, 5, 6]))



# from collections import deque 
# 
# def solution(bridge_length, weight, truck_weights):
#     pass_bridge = deque([0]*(bridge_length*len(truck_weights)))
#     time = 0
#     truck = 0

#     while truck < len(truck_weights) :
#         if pass_bridge[time] + truck_weights[truck] <= weight :
#             for l in range(bridge_length) :
#                 pass_bridge[time+l] += truck_weights[truck]
#             truck += 1
#         time += 1 
#     return time + bridge_length