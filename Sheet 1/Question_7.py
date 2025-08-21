# Q7 Read three angles of triangle and determine their types(Right Angle, Obtuse Angle, Acute Angle).

angle1= int(input("Enter Angle 1: "))
angle2= int(input("Enter Angle 2: "))
angle3= int(input("Enter Angle 3: "))
if angle1 > 90 or angle2 > 90 or angle3> 90:
    print("It is an Obtuse Angle Triangle")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("It is a Right Angle Triangle")
elif angle1 < 90 and angle2 < 90 and angle3 < 90:
    print("It is an Acute Angle Triangle")
else:
    print("The angles do not form a triangle")