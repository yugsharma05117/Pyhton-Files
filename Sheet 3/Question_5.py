#Print the following pattern
#*_ _ _*
#*_ _ _*
#*_ _ _*
#*_ _ _*
#*_ _ _*


for i in range(4):
    for j in range(5):
        if j==0 or j==4:
            print("*" ,end="")
        else:
            print("_",end="")
    print()