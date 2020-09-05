'''
이진 트리
https://www.acmicpc.net/problem/4256
'''
def postorder(preorder, inorder) :
    if len(preorder) <= 1 :
        return preorder[:1]
    
    i = inorder.index(preorder[0])
    return postorder(preorder[1:i+1],inorder[:i]) + postorder(preorder[i+1:], inorder[i+1:]) + preorder[:1]


T = int(input())
for _ in range(T) :
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    print(" ".join(map(str, postorder(preorder, inorder))))
