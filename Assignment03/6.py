# 6. To find out Pythagorean numbers x, y, z within 100 such that z^2 = x^2 + y^2 .
limit = 100
result=[]
for x in range (0,limit-2) :
    y = x + 1
    z = x + 2
    if pow(z,2) == (pow(x,2) + pow(y,2)) :
        result.append((x,y,z))

print(result)

