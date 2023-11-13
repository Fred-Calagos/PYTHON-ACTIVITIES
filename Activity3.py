name = input("Name: ")
mg = (float(input("Math Grade: ")))
sg = (float(input("Science Grade: ")))
eg = (int(input("English Grade: ")))

average = float(mg + sg + eg)/3
avg = "Average: %.2f " %(average)
print(avg)

if average >= 75:
    print("Status: Passed")
else:
    print("Status: Failed")
