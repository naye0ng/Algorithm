'''
5052 전화번호목록
https://www.acmicpc.net/problem/5052
'''
def insert_child(keys, flags, numbers, index) :
    keys.append([numbers[index]])
    if index == len(numbers)-1 : 
        flags.append([True])
    else :
        flags.append([False])
        insert_child(keys[-1], flags[-1], numbers, index+1)


def make_trie(keys, flags, numbers, index = 0) :
    # 이 지점에서 끝나는 번호가 있을 때
    if flags[0]: return False
    if index == len(numbers)-1 : 
        # 내가 여기서 끝나는데, 나랑 같으면서 더 긴 번호가 존재할 때
        if len(keys) >= 1 : return False
        return True

    for i in range(1, len(keys)) :
        if numbers[index+1] == keys[i][0] :
            return make_trie(keys[i], flags[i], numbers, index+1)

    insert_child(keys, flags, numbers, index+1)
    return True

T = int(input())
for test_case in range(T) :
    N = int(input())
    # [중요] 트라이는 동일한 root를 가지도록 만드는 것이 중요하다!!!!!!!
    phone_numbers = [' '+input() for _ in range(N)]
    trie_key, trie_flag = [' '], [False]

    answer = 'YES'
    break_flag = False
    for numbers in phone_numbers :
        if make_trie(trie_key, trie_flag, numbers) : continue
        answer = 'NO'
        break

    print(answer)