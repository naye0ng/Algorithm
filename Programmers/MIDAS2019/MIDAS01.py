def computeHCF_euc(x, y):
   # y가 0이 될 때까지 반복
   while(y):
       # y를 x에 대입
       # x를 y로 나눈 나머지를 y에 대입
       x, y = y, x % y
   return x
def lcm(x, y):
   lcm = (x*y)//computeHCF_euc(x,y)
   return lcm

print(lcm(2,3))