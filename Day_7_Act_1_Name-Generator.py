import random
from random import choice
fname = ["Frederick", "April", "Jason", "Trexie", "Charmie", "Revin", "Joseph", "Klent", "Jinky", "Maria"]
mname = ["Dadap", "Sumalinog", "Mapana", "Abuyan", "Anghag", "Humalatag", "Erong", "Paiz", "Ostria", "Tangog"]
lname = ["Aninon", "Acido", "Bagood", "Melchor", "Eno", "Calagos", "Estorgio", "Tamiat", "Calvar", "Bugais"]
nbank = []
while True:

    new = input("Do you want a new name yes/no: ")
    if new == "y":
        random = int(input("Select number from 0-9: "))
        if random <= 9:
            new_name = " ".join(["%s %s %s" % (choice(fname), choice(mname), choice(lname)) for _ in range(1)])
            print("Congratulations! Your new name is: " + new_name)
            nbank.append(new_name)
            continue
    if new == "n":
        print("Thank you")
        for i in nbank:
            print(i)
