"""
단어변환
"""
def diffOne(a,b) :
    count = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            count += 1
            if count > 1 :
                return False
    if count == 1 :
        return True
    return False 

def DFS(start, target, words, depth, visited) :
    if start == target :
        global answer
        if answer == 0 or answer > depth :
            answer = depth
    elif answer == 0 or answer > depth :
        for i in range(len(words)) :
            if not visited[i] and diffOne(start, words[i]):
                visited[i] = True
                DFS(words[i], target, words, depth+1, visited)
                visited[i] = False

def solution(begin, target, words):
    global answer
    answer = 0
    if target in words :
        visited = [ False for _ in range(len(words))]
        DFS(begin, target, words, 0, visited)
    return answer

print(solution("hit", "cog", ["hit","hot", "hog", "cog"]))