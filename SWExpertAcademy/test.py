# def d() :
#     return [3,4], 5

# an, sum = d()

# print(an, sum)


# def minvalue(an) :
#     k = len(an)
#     if k == 1 :
#         return an, 0
#     else :
#         if k == 2 :
#             return [an[0][0], an[1][1]] , an[0][0]*an[0][1]*an[1][1]
#         else :
#             minsum = 0
#             for i in range(k-1):
#                 print(i)
#                 bn, s = minvalue(an[:i]+an[i+1:])
#                 s += an[i][0]*an[i][1]*bn[1]
#                 if minsum == 0 :
#                     minsum = s
#                 if minsum > s :
#                     minsum = s
#             return minsum


def minvalue(an) :
    k = len(an)

    if k == 1 :
        return an, 0
    min_s = 0
    min_kn = []
    for i in range(k-1) :
        bn, s1= minvalue(an[:i+1])
        cn, s2= minvalue(an[i+1:])

        s = bn[0][0]*bn[0][1]*cn[0][1]+s1+s2
        kn = [[bn[0][0],cn[0][1]]]

        if min_s == 0 :
            min_s = s
            min_kn =kn
        if min_s > s :
            min_s =s
            min_kn = kn
    return min_kn, min_s


an = [[1, 2], [2, 3]]
print(minvalue(an))