"""
전화번호목록
"""

def solution(phone_book):
    phone_book = sorted(phone_book)
    front = 0

    while front < len(phone_book) :
        for target in phone_book[front+1:]:
            if phone_book[front].startswith(target) :
                return False
        front += 1
    return  True

print(solution(["117","976742","449", "97674223", "5521144921"]))