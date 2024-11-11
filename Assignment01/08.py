# 8. To determine the area of the walls of a rectangular room and hence
# the cost of its painting on the basis of charge per square unit.
#    ___________
#    |\_________\ 2(width)
#    | |        |  4(height)
#     \|________| 
        #    5(length)
length = eval(input("Enter the length of room(m) :"))
width = eval(input("Enter the width of wall(m) :"))
height = eval(input("Enter the height of wall(m) :"))

print("____Big wall____")
area01 = (2* length * height)
print(f"Area of 2 big wall : {area01} m^2")

print("____Small wall____")
area02 = (2* width * height)
print(f"Area of 2 small wall : {area02} m^2")

print("Area of silling :",(length * width)," m^2")
print("Area of walls :",(area01+area02)," m^2")




