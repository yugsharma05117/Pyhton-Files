'''
 Q15 Accept the percentage from the user and display the grade according to the following
criteria.
●
Below 25 - D
●
25 to 45 - C
●
45 to 65 - B
●
65 to 85 - A
●
Above 85 - A+
'''

percentage= int(input("Enter your percentage: "))
if percentage <25:
    print("Your grade is D")
elif 25 <= percentage < 45:
    print("Your grade is C")
elif 45 <= percentage < 65:
    print("Your grade is B")
elif 65 <= percentage < 85:
    print("Your grade is A")
elif percentage >= 85:
    print("Your grade is A+")
else:
    print("Invalid percentage entered.")