"""
후위 표기식
https://www.acmicpc.net/problem/1918
"""

N = " ".join(input()).split()

answer = []
stack = []
for i in range(len(N)) :
    # 괄호
    if N[i] == '(' :
        stack.append(N[i])
        
    elif N[i] == ")" :
        s = stack.pop()
        while s != "(" :
            answer.append(s)
            s = stack.pop()
    # 연산자
    elif N[i] == "*" or N[i] == "/" :
        for s in range(len(stack)-1,-1,-1) :
            if stack[s] in ["(", "+", "-"] :
                break
            answer.append(stack.pop())
        stack.append(N[i])
    elif N[i] == "+" or N[i] == "-" :
        for s in range(len(stack)-1,-1,-1) :
            if stack[s] == "(" :
                break
            answer.append(stack.pop())
        stack.append(N[i])
    # 피연산자
    else :
        answer.append(N[i])

for _ in range(len(stack)) :
    answer.append(stack.pop())

print("".join(answer))

"""
문제 : a+b*((c-d)+f)*e
답 : abcd-f+*e*+


+
*
e
*
+  *
f  // )
   // + 
-
d // )
c // -
  // (
  // (
b // *
a + 
"""