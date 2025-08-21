# Q12 You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.
angle1= int(input("Enter the first angle of the triangle: "))
angle2 = int(input("Enter the second angle of the triangle: "))
angle3 = int(input("Enter the third angle of the triangle: "))
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")