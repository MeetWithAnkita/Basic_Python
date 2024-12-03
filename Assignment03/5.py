# 5. To find out the series of five consecutive numbers within 1000,for
# which the sum of the squares of the first three is equal to the sum of
# the squares of the last two. For example, (−2)^2+(−1)^2+0^2 = 1^2+2^2
# limit = 1000
# result = []
# for a in range(0,limit-4) :
#     b= a+1
#     c= a+2
#     d= a+3
#     e= a+4
#     if (pow(a,2)+pow(b,2)+pow(c,2)) == (pow(d,2)+pow(e,2)) :
#         # print(f"{(a,b,c,d,e)}")
#         result.append((a,b,c,d,e))
#         print(result)
limit = 1000
result = []
for a in range(0,limit-4):
    b = a+1
    c = a+2
    d = a+3
    e = a+4
    sum_first_three = a**2 + b**2 + c**2
    sum_last_two = d**2 + e**2
    if sum_first_three == sum_last_two:
        result.append((a,b,c,d,e))
        print(result)
    elif sum_first_three > sum_last_two:  # Early termination
        break