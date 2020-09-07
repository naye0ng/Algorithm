"""
전위순회
"""
# def preorder_traverse(T) :
#     if T :
#         print(T)
#         preorder_traverse(tree[T][0])
#         preorder_traverse(tree[T][1])

# n = 13
# inputData = [1,2,1,3,2,4,3,5,3,6,4,6,5,8,5,9,6,10,6,11,7,12,11,13]

# tree = [[0]*2 for i in range(13+1)]

# for i in range(0,len(inputData),2) :
#     if tree[inputData[i]][0] == 0 :
#         tree[inputData[i]][0] = inputData[i+1]
#     else :
#         tree[inputData[i]][1] = inputData[i+1]

# print(tree)
# preorder_traverse(1)

def preorder_traverse(i) :
    if i < len(T) :
        print(T[i], end=" ")
        preorder_traverse(i*2)
        preorder_traverse(i*2+1)

T = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
preorder_traverse(1)