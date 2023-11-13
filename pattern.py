# rows = 5
# b = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('\r')
# print()
#
# rows = 5
# num = rows
# # reverse for loop
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")
#
# rows = int(input("Enter the number of rows:"))
# k = 2 * rows - 2  # It is used for number of spaces
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2   # decrement k value after each iteration
#     for j in range(0, i + 1):
#         print("* ", end="")  # printing star
#     print("")
#
# rows = int(input("Enter the number of rows: "))
#
# # the outer loop is executing in reversed order
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# rows = 5
#
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print("")
#
# rows = int(input("Enter the number of rows: "))
#
# # It is used to print space
# k = 2 * rows - 2
# # Outer loop in reverse order
# for i in range(rows, -1, -1):
#     # Inner loop will print the number of space.
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     # This inner loop will print the number o stars
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

rows = int(input("Enter the number of rows: "))

# It is used to print the space
k = 2 * rows - 2
# Outer loop to print number of rows
for i in range(0, rows):
    # Inner loop is used to print number of space
    for j in range(0, k):
        print(end=" ")
        # Decrement in k after each iteration
    k = k - 1
    # This inner loop is used to print stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

# Downward triangle Pyramid
# It is used to print the space
k = rows - 2
# Output for downward triangle pyramid
for i in range(rows, -1, -1):
    # inner loop will print the spaces
    for j in range(k, 0, -1):
        print(end=" ")
        # Increment in k after each iteration
    k = k + 1
    # This inner loop will print number of stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")