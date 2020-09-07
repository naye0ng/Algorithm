"""
반복문으로 순열, 조합, 중복순열, 중복조합 만들기
"""
#순열
def perm() :
    for i in range(N) :
        for j in range(N) :
            if i != j :
                print(a[i],a[j])

# 조합
def comb():
    for i in range(N-1) :
        for j in range(i+1,N) :
            print(a[i],a[j])

# 중복순열
def pi() :
    for i in range(N) :
        for j in range(N) :
            print(a[j],a[i])

# 중복조합
def h() :
    for i in range(N) :
        for j in range(i, N) :
            print(a[i],a[j])

N = 3 
a = [1,2,3]


print("--순열--")
perm()
print("--조합--")
comb()
print("--중복순열--")
pi()
print("--중복조합--")
h()
