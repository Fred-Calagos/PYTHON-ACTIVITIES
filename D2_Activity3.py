name = input("Please Enter Name: ")
mg = input("Please Enter Math Grade: ")
eg = input("Please Enter English Grade: ")
sg = input("Please Enter Science Grade: ")
avg1 = ((float(mg) + float(eg) + float(sg))/3)
# avg1 = float(avg)
# avg2 = round(avg)
print("Your Grade is: ", float(avg1))

if (avg1 < 75):
    print("Letter Equivalent: D    -   Failed")
elif (avg1 >= 75) and (avg1 < 78):
    print("Letter Equivalent: C    -   Passing")
elif (avg1 >= 78) and (avg1 < 84):
    print("Letter Equivalent: B    -   Average")
elif (avg1 >= 84) and (avg1 < 90):
    print("Letter Equivalent: B+    -   Above Average")
elif (avg1 >= 90) and (avg1 < 99):
    print("Letter Equivalent: A-    -   Very Good")
elif (avg1 >= 99 and avg1 <=100):
    print("Letter Equivalent: A+    -   Excellent")
