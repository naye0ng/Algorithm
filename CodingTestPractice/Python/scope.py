"""
Python 스코프 정리
"""

# [1] python는 합수 내부에 지역변수를 확인 한 뒤, 전역을 살핀다.

a = 2

def test_01():
    a = 3   # 지역변수 a가 존재
    print("inside test 01: ", a)

def test_02():
    # 지역변수가 존재하지 않음, a는 전역
    print("inside test 02: ", a)

def test_03():
    # 지역변수가 함수 내부에 존재하지만 선언 전에 사용했음으로 에러!
    # python으로 문제 풀때, 전역 변수를 그냥 사용하는 것은 가능하지만 
    # global 키워드 없이 값을 변경하면 
    # local variable 'a' referenced before assignment 에러가 발생한다.
    print("inside test 03: ", a) 
    a = 4

def test_04():
    # test_03의 문제를 global 키워드를 사용하여 해결
    global a
    print("inside test 04", a)
    a = 5

test_01()
print("after test 01", a)

test_02()
print("after test 02", a)

# test_03()
print("after test 03", a)

test_04()
print("after test 04", a)


"""
[답]
inside test 01: 3
after test 01: 2

inside test 02: 2
after test 02: 2

local variable 'a' referenced before assignment
after test 03: 2

inside test 04: 2
after test 04: 5
"""

d = set()
d.add(1)
d.add(10)

for i in d :
    print(i)

print(len(d))