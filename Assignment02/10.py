# 10. To accept the lengths of three sides of a triangle to check whether
# the given lengths can be valid lengths of three sides of a triangle
# and to categorize the triangle as ‘Equilateral’ or ‘Isosceles’ or
# ‘Scalene’ one.

length_01 , length_02, length_03 = input("Enter 3 length of triangle(separated by space) :").split()
if ((length_01+length_02)>length_03 or (length_01+length_03)>length_02 or (length_02+length_03)>length_01):
    if (length_01 == length_02 == length_03):
        print("The triangle is Equilateral.")
    elif ((length_01==length_02) or (length_02==length_03) or (length_01==length_03)):
        print("The triangle is Isosceles.")
    elif (length_01 != length_02 != length_03):
        print("The triangle is Scalene. ")    
else :
    print("Invalid Triangle.")    