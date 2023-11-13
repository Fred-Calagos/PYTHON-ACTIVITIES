while True:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    sum = num1 + num2
    print("The Sum of ", num1,"and ", num2,"is ", sum)
    confirm = input("Do You Want to Try again? (Y/N) : ")

    if confirm == "Y" or confirm == "y":
        print()
    if confirm == "N" or confirm == "n":
        print("Thank You")
        break