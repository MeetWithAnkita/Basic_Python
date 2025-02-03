# Prompt user for input
feet = float(input("Enter length in feet: "))
print("Choose conversion: 1 for inches, 2 for yards, 3 for miles, 4 for mm, 5 for cm, 6 for meters, 7 for km")

conversion_type = int(input("Enter choice (1-7): "))
conversions = [feet * 12, feet / 3, feet / 5280, feet * 304.8, feet * 30.48, feet * 0.3048, feet * 0.0003048]
if 1 <= conversion_type <= 7:
    print("Converted value:", conversions[conversion_type - 1])
else:
    print("Invalid choice.")