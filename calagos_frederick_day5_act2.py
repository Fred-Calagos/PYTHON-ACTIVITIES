words = []
while True:
    wordle = input("Enter a Word: ")
    words.append(wordle)
    cont = input("Do you want to try again? y/n: ")
    if cont == 'y':
            print()
    if cont == "n":
            wcount = len(words)
            print("The total number of words: ", wcount)
            print("The inserted words: ",", ".join(words))
            break


