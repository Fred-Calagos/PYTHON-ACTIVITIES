import csv
from tabulate import tabulate

def add_customer():
    print("\n\n ********** || ADD RESERVATION || *********")
    name = input("Enter customer name: ")
    date = input("Enter reservation date (yyyy-mm-dd): ")
    time = input("Enter reservation time (hh:mm): ")
    num_adults = int(input("Enter number of adults: "))
    num_children = int(input("Enter number of children: "))
    num_tables = int(input("Enter number of tables: "))
    with open("reservations.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time, num_adults, num_children, num_tables])

def view_all():
    print("\n\n ********** || VIEW RESERVATION || *********")
    with open("reservations.csv", mode="r") as file:
        reader = csv.reader(file)
        headers = ["Name", "Date", "Time", "Adults", "Children", "Tables"]
        data = list(reader)
        print("\n List of Reservations\n")
        print("\n", tabulate(data, headers=headers))
        print("\n\n")

def delete_customer():
    print("\n\n ********** || DELETE RESERVATION || *********")
    name_or_number = input("Enter name or reservation number of customer to delete: ")
    with open("reservations.csv", mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    with open("reservations.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            if name_or_number != row[0] and name_or_number != row[1]:
                writer.writerow(row)

def generate_report():
    print("\n\n ********** || GENERATE REPORT OF ALL RESERVATION || *********")
    with open("reservations.csv", mode="r") as file:
        no_adults, no_kids, no_tbl, subtotal, num = 0, 0, 0, 0, 0
        reader = csv.reader(file)
        headers = ["#", "Name", "Date", "Time", "Adults", "Children", "No. of Tables", "SubTotal"]
        data = list(reader)
        total_profit = 0
        for row in data:
            no_adults += int(row[3])
            no_kids += int(row[4])
            no_tbl += int(row[5])
            total_profit += (int(row[3]) * 500) + (int(row[4]) * 300)
            subtotal = (int(row[3]) * 500) + (int(row[4]) * 300)
            row.append(str(subtotal))
            if row[0] == "#":
                num = 1
            else:
                num += 1
            row.insert(0, num)
        print("\nReservation List:")
        print("\n", tabulate(data, headers=headers))
        print("\nTotal number of children: ", no_kids)
        print("Total number of adults: ", no_adults)
        print("Total number of Table: ", no_tbl)
        print("\nTotal Profit: ₱", total_profit)
        print("\n\n")

def generate_individual_report():
    print("\n\n ********** || GENERATE INDIVIDUAL REPORT OF RESERVATION || *********")
    name = input("Enter name of customer: ")
    with open("reservations.csv", mode="r") as file:
        reader = csv.reader(file)
        headers = ["Name", "Date", "Time", "Adults", "Children", "No. of Tables"]
        data = list(reader)
        total_profit = 0
        customer_data = []
        for row in data:
            if name == row[0]:
                customer_data.append(row)
                no_adults = row[3]
                no_kids = row[4]
                no_tbl = row[5]
                total_profit += (int(row[3]) * 500) + (int(row[4]) * 300)
        print("\nReservation List for", name + ":")
        print("\n", tabulate(customer_data, headers=headers))
        print("\nTotal number of children: ", no_kids)
        print("Total number of adults: ", no_adults)
        print("Total number of Table: ", no_tbl)
        print("\nGrand Total for", name + ": ₱", total_profit)
        print("\n\n")
        print("--------------------------------|| END OF REPORT ||------------------------------------")
        print("\n\n")

while True:
    print("\n\n******* || Welcome to the BARRIO RESTAURANT Reservation System! || *******")
    print("1. Add Customer")
    print("2. View All Reservations")
    print("3. Delete Reservation")
    print("4. Generate Report")
    print("5. Generate Individual Report")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_customer()
    elif choice == 2:
        view_all()
    elif choice == 3:
        delete_customer()
    elif choice == 4:
        generate_report()
    elif choice == 5:
        generate_individual_report()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
