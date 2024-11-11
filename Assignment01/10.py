# 10. To determine the perimeter of a triangular plot
side01,side02,side03 = input("Enter the 3 side of triangle plot (cm)(separated by coma(,)) : ").split(',')
side01 = eval(side01)
side02 = eval(side02)
side03 = eval(side03)

perimeter = side01 + side02 + side03
print(f"The perimeter of a triangular plot :{perimeter} cm")
