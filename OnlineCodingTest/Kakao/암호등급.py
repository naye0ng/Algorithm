security = [False]*5
password = input()
if len(password) >= 10 :
    security[4] = True

for s in password :
    if 'a' <= s <= 'z' :
        security[0] = True
    elif 'A' <= s <= 'Z' :
        security[1] = True
    elif '0' <= s <= '9' :
        security[2] = True
    else :
        security[3] = True

print('LEVEL{}'.format(sum(security)))

"""
aq%~9P2!@@s!v#&&KM^lFf
"""