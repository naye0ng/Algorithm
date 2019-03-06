"""
4751.다솔이의 다이아몬드 장식
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1) :
    string = input().replace(""," ").split()
    n = len(string)

    s1 = "."+".".join([".#."]*n)+"."
    s2 ="."+".".join(["#"]*2*n)+"."

    print(s1)
    print(s2)
    print("#."+".#.".join(string)+".#")
    print(s2)
    print(s1)
