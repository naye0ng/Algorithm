"""
itertools 라이브러리를 활용한 순열, 조합, 중복순열, 중복조합 구하기
"""
from itertools import permutations, combinations, product, combinations_with_replacement

items = ['A', 'B', 'C']

"""
[순열]
- 순서가 존재
- ex) AB != BA
"""
# [1]items의 모든 원소를 가지고 순열을 만든다.
# ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
perm = permutations(items)
print(list(map(''.join, perm))) 

# [2] items의 원소 2개를 뽑라서 순열을 만든다.
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
perm = permutations(items, 2)
print(list(map(''.join, perm)))  

"""
[조합]
- 순서가 존재하지 않음
- ex) AB == BA
"""
# [1] items의 원소 중 2개를 뽑아 조합을 만든다.
# ['AB', 'AC', 'BC']
comb = combinations(items, 2)
print(list(map(''.join, comb)))  

# [2] 모든 조합을 구한다.
# ['A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']
comb = []
for i in range(len(items)) :
   comb.extend(list(map(''.join, combinations(items, i+1))))
print(comb)


"""
중복순열
- 순서가 있지만 같은 원소가 여러번 뽑혀도 된다.
- ex) AA
"""
# [1] 중복가능한 최대 수를 repeat으로 넘겨 준복순열을 구한다.
# ['AAA', 'AAB', 'AAC', 'ABA', 'ABB',
#   'ABC', 'ACA', 'ACB', 'ACC', 'BAA', 'BAB', 
#   'BAC', 'BBA', 'BBB', 'BBC', 'BCA', 'BCB', 
#   'BCC', 'CAA', 'CAB', 'CAC', 'CBA', 'CBB', 
#   'CBC', 'CCA', 'CCB', 'CCC']
perm = product(items, repeat=3)
print(list(map(''.join, perm))) 


"""
중복조합
- 순서가 없지만 같은 원소가 여러변 뽑힌다.
- ex) AAB == ABA
"""
# [1] 중복가능한 최대 수를 인자로 넘겨 중복조합을 구한다.
# ['AAA', 'AAB', 'AAC', 'ABB', 'ABC', 'ACC', 'BBB', 'BBC', 'BCC', 'CCC']
comb = combinations_with_replacement(items, 3)
print(list(map(''.join, comb)))  