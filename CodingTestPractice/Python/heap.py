"""
우선순위 큐
- python에서 제공하는 heap은 최소힙
- 시간복잡도는 nlogn
- 관련문제) https://www.acmicpc.net/problem/11279
"""
import heapq

"""
[최소 힙]
"""
h = []
heapq.heappush(h, (3, "Go to home"))
heapq.heappush(h, (10, "Do not study"))
heapq.heappush(h, (1, "Enjoy!"))
heapq.heappush(h, (4, "Eat!"))

print(h) # [(1, 'Enjoy!'), (4, 'Eat!'), (3, 'Go to home'), (10, 'Do not study')]

"""
[주의]
항상 h 내부의 값의 정렬이 순서대로인 것이 아님, 
[0]값만 최소값이 나오는 것이므로 순서대로 출력하고 싶다면 heappop()을 사용해야한다.
"""

first = heapq.heappop(h)
second = heapq.heappop(h)
third = heapq.heappop(h)

print("first:", first)      # first: (1, 'Enjoy!')
print("second:", second)    # second: (3, 'Go to home')
print("third:", third)      # third: (4, 'Eat!') 


"""
[최대 힙]
"""
# [1] -1을 곱하는 방법으로 구현
items = [3,5,7,2,4,1]
h = []
for item in items :
    heapq.heappush(h, -item)

print(h)    # [-7, -4, -5, -2, -3, -1]

for _ in range(len(h)) :
    print(-heapq.heappop(h), end=' ')    # 7 5 4 3 2 1
print()

# [2] 만약 -1을 곱할 수 없는 값을 넣어야한다면? 튜플을 이용하자
items = ['A', 'C', 'B', 'F', 'G']
h = []
for item in items :
    idx = ord(item)*(-1)
    heapq.heappush(h, (idx, item))

print(h)    # [(-71, 'G'), (-70, 'F'), (-66, 'B'), (-65, 'A'), (-67, 'C')]
for _ in range(len(h)) :
    print(heapq.heappop(h)[1], end=' ')     # G F C B A 
print()

"""
[배열 => 힙] 
- 시간복잡도 n을 가지도록 만들어짐
"""
items = [3,5,7,2,4,1]
heapq.heapify(items)
print(items)   # [1, 2, 3, 5, 4, 7]

for _ in range(len(items)) :
    print(heapq.heappop(items), end=' ')    # 1 2 3 4 5 7 
print()