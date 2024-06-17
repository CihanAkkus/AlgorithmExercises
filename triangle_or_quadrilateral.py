Type = input("Do you want to find the type of triangle or quadrilateral ?\n")

if (Type == "quadrilateral"):
    side1 = float(input("Please enter the first side = "))
    side2 = float(input("Please enter the second side = "))
    side3 = float(input("Please enter the third side = "))
    side4 = float(input("Please enter the fourth side = "))
    if (side1 == side2 == side3 == side4):
        print("It is square")
    elif ((side1 == side2 and side1 != side3 and side1 != side4) and side3 == side4):
        print("It is rectangle")
    elif ((side1 == side3 and side1 != side2 and side1 != side4) and side2 == side4):
        print("It is rectangle")
    elif ((side1 == side4 and side1 != side2 and side1 != side3) and side3 == side2 ):
        print("It is rectangle")
    else:
        print("It is a normal quadrilateral")
elif (Type == "triangle"):
    sideTri1 = float(input("Please enter the first side = "))
    sideTri2 = float(input("Please enter the second side = "))
    sideTri3 = float(input("Please enter the third side = "))
    if (sideTri1 == sideTri2 == sideTri3):
        print("It is equilateral triangle")
    elif ((sideTri1 == sideTri2 and sideTri1 != sideTri3) and (abs(sideTri1 - sideTri2) < sideTri3 < (sideTri1 + sideTri2) and abs(sideTri1 - sideTri3) < sideTri2 < (sideTri1 + sideTri3))):
        print("It is isosceles triangle")
    else:
        if(abs(sideTri1 - sideTri2) < sideTri3 < (sideTri1 + sideTri2) and abs(sideTri1 - sideTri3) < sideTri2 < (sideTri1 + sideTri3) and abs(sideTri2 - sideTri3) < sideTri1 < (sideTri2 + sideTri3)):
            print("It is a normal triangle")
        else:
            print("You cannot create a triangle with sides of this length, it would be good for you to look at the conditions for creating a triangle.")