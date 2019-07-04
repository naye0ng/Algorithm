"""
더 맵게 - 최소 힙
"""
import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + b*2
        heapq.heappush(scoville, c)
        answer += 1

    if len(scoville) == 1 and scoville[0] < K :
        return -1
    return answer



# def addHeap(heap, v) :
#     heap.append(v)
#     i = len(heap)-1
#     while i > 1 :
#         k = i//2
#         if heap[i] < heap[k] :
#             heap[i], heap[k] = heap[k], heap[i]
#             i = k
#         else : 
#             break

# def removeHeap(heap) :
#     # 최상단 빠지기
#     root = heap[1]
#     heap[1] = heap.pop()
#     i = 1
#     while i < len(heap) :
#         # 이동가능 경로 체크
#         if i*2+1 < len(heap)-1 :
#             if heap[i*2] < heap [i*2+1] :
#                 k = i*2
#             else :
#                 k =i*2+1
#         elif i*2 < len(heap)-1 :
#             k =i*2
#         else : 
#             return root 

#         # 힙 삽입
#         if heap[i] > heap[k] :
#             heap[i], heap[k] = heap[k], heap[i]
#             i = k
#         else :
#             return root

# def solution(scoville, K):
#     answer = 0
#     heap = [0]  # heap의 인덱스를 1부터 시작하도록 0 삽입
#     for s in scoville :
#         addHeap(heap, s)

#     while heap :
#         # 체크 
#         isUpperK = True
#         for h in heap[1:] :
#             if h < K :
#                 isUpperK = False
#                 break
        
#         if isUpperK :
#             break
#         else :
#             a = removeHeap(heap)
#             b = removeHeap(heap)
#             c = a + b*2
#             addHeap(heap, c)
#             answer += 1

#     return answer

print(solution([1, 2, 4, 9, 10, 12], 7))