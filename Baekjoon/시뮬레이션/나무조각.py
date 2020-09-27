'''
나무조각
https://www.acmicpc.net/problem/2947
'''
wood_blocks = input().split()
while wood_blocks != ['1','2','3','4','5'] :
    for i in range(4) :
        if wood_blocks[i] < wood_blocks[i+1] : continue
        wood_blocks[i], wood_blocks[i+1] = wood_blocks[i+1], wood_blocks[i]
        print(" ".join(wood_blocks))
