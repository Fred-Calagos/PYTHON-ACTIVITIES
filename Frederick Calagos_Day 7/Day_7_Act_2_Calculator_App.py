while True:
    operand = input("A: Add, \nM: Multiply,\nD: Divide,\nS: Subtraction \nChoose Operations: ")
    match operand:
        case "A":
            try:
                num1 = int(input("Enter First Input: "))
                num2 = int(input("Enter Second Input: "))
                add = num1 + num2
                print("Result: ", add)
            except ValueError as add:
                print("Error: Invalid Input, Cannot add numbers to Letters")

        case "M":
            try:
                num1 = int(input("Enter First Input: "))
                num2 = int(input("Enter Second Input: "))
                multiply = num1 * num2
                print("Result: ", multiply)
            except ValueError as add:
                print("Error: Invalid Input, Cannot Multiply numbers to Letters")
        case "D":
            try:
                num1 = int(input("Enter First Input: "))
                num2 = int(input("Enter Second Input: "))
                div = num1 / num2
                print("Result: ", div)
            except ZeroDivisionError and ValueError as div:
                print("Error: Cannot Divide by Zero")
            except ValueError as div:
                print("Error: Invalid Input")

        case "S":
            try:
                num1 = int(input("Enter First Input: "))
                num2 = int(input("Enter Second Input: "))
                sub = num1 - num2
                print("Result: ", sub)
            except ValueError as sub:
                print("Error: Invalid Input, Cannot Subtract numbers to Letters")

