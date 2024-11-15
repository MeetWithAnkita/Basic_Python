# 5. To determine whether a quadrilateral is a square, rhombus, parallelogram, 
# square or irregular on the basis of only the lengths of all the sides and one internal angle.

# Square:
# All four sides are equal.
# Any one internal angle is 90∘ .

# Rhombus:
# All four sides are equal.
# The given internal angle is not 90∘ .

# Rectangle:
# Opposite sides are equal (two pairs of equal sides).
# Any one internal angle is 90∘ .

# Parallelogram:
# Opposite sides are equal (two pairs of equal sides).
# The given internal angle is not 90∘ .

# Irregular Quadrilateral:
# None of the above conditions apply
# (the sides do not satisfy the conditions of square, rhombus, rectangle, or parallelogram).

#          a
    #  ________
  # d |       |  b
    # |_______|
#          c

a,b,c,d = input("Enter the length of 4 side (separated by space):").split()
a= eval(a) 
b= eval(b)
c= eval(c)
d= eval(d)
internal_angle = eval(input("Enter the internal angle in degree :"))
if(internal_angle == 90) :
    if ( a==b==c==d ):
        print("It is Square.")
    elif (a==c and b==d):
        print("It is Rectangle.")
    else :
        print("Irregular Quadrilateral.")    
else :    
    if ( a==b==c==d ):
        print("It is Rhombus.")
    elif (a==c and b==d):
        print("It is Parallelogram.")
    else :
        print("Irregular Quadrilateral.") 
