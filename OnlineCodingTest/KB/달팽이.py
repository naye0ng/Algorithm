import math
H, U, D, F = map(int, input().split())
UF = U*F/100

U += UF
day, height = 0, 0
while True :
    day += 1
    U = math.trunc((U-UF)*100)/100
    if U < 0 :
        U = 0
    else :
        height = math.trunc((height + U)*100)/100
    
    if height > H :
        print("Success", day)
        break
    # 내려감
    height = math.trunc((height-D)*100)/100

    # 처음 바닦에 내려왔을 때 출력
    if height <= 0 :
        print("Failure", day)
        break



    
    

   
