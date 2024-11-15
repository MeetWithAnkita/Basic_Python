# 9. To categorize a triangle on the basis of its three given angles. The
# triangle may be in an ‘invalid triangle’, ’Equiangular’, ‘ rightangle ’, ‘ acute angled ’ or ‘obtuse angled’.
angle01 , angle02 , angle03 = input("Enter three angle of a triangle (in degree) , separated by space:").split()
angle01 = eval(angle01)
angle02 = eval(angle02)
angle03 = eval(angle03)

if ((angle01 + angle02 + angle03) != 180):
    {
        print("It is an invalid triangle. ")
    }
else:
    if(angle01 == angle02 == angle03 == 60):
        print("It is a Equiangular triangle. ")    
    elif (angle01 == 90 or angle02 == 90 or angle03 == 90) :
        print("It is rightangle triangle. ")    
    elif (angle01 > 90 or angle02 > 90 or angle03 > 90) :
        print("It is acute angled triangle. ")
    elif (angle01 < 90 or angle02 < 90 or angle03 < 90) :
        print("It is obtuse angled triangle. ")  
    else :
        print("It is an invalid triangle. ")       
