import heapq

def solution(dataSource, tags):
    tags = dict.fromkeys(tags, 1)
    h = []
    for d in range(len(dataSource)) :
        n = 0
        for i in range(1, len(dataSource[d])) :
            if dataSource[d][i] in tags :
                n -= 1
        if n < 0 :
            heapq.heappush(h, (n, dataSource[d][0]))
    answer = []
    for _ in range(min(10, len(h))) :
        answer.append(heapq.heappop(h)[1])
    return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]))