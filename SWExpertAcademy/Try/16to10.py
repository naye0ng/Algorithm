"""
16진수로 들어온 문자열을 앞에서부터 7개씩 변환하여 십진수로 출력하자

- 예를 들어 : 0F97A3이 들어올 경우 >> (2진수 변환)0000111111... >> 7, 101, 116, 3을 출력한다.

[입력]
'01D06079861D79F9F99F'
"""
arr = input()
arr = arr.replace('0','0000')
arr = arr.replace('1','0001')
arr = arr.replace('2','0010')
arr = arr.replace('3','0110')
arr = arr.replace('4','0100')
arr = arr.replace('5','0101')
arr = arr.replace('6','0110')
arr = arr.replace('7','0111')
arr = arr.replace('8','1000')
arr = arr.replace('9','1001')
arr = arr.replace('A','1010')
arr = arr.replace('B','1011')
arr = arr.replace('C','1100')
arr = arr.replace('D','1101')
arr = arr.replace('E','1110')
arr = arr.replace('F','1111')