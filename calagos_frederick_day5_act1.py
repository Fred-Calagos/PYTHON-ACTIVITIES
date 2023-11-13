def reverse(s):
    name=input()
    str=""
    for i in s:
        str = i + str
    return str
s = input("Input: ")
upperstring = reverse(s)
scount = len(s)
print("The Original text: " + s)
print("The Reverse string: " + upperstring.upper())
print("No. of Characters: ", scount)
