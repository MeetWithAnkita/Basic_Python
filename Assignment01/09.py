# 9. To determine the area of a cone
# area = (pi * r * l) + (pi * r^2) = pi * r (l + r)
# l^2 = (h^2 + r^2)

import math
pi = 22/7
radius = eval(input("Radius of cone(cm) :"))
height = eval(input("Height of cone(cm) :"))
l = math.sqrt((height**2 + radius**2))
area_of_curved_area = pi * radius * l 
area_of_round_surface = pi * pow(radius,2)
area = pi * radius * (l + radius)

print(f"Area of curved-cone :{area_of_curved_area:.2f} cm^2")
print(f"Area of curved-cone :{area_of_round_surface:.2f} cm^2")
print(f"Area of cone :{(area_of_curved_area+area_of_round_surface):.2f} cm^2")

