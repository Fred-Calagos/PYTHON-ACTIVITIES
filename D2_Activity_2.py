name = input("Employee Name: ")
hours = int(input("Enter number of Hours: "))
sss =int(input("SSS contribution: "))
ph = int(input("Phil Health: "))
hloan = int(input("Housing Loan: "))
rateph = 500
gsalary = hours * rateph
gtax = gsalary * .10
tdeduction = sss + ph + hloan + gtax
nsalary = gsalary - tdeduction
print("=======================PAYSLIP==============================")
print("")
print("Employee Name: ", name)
print("Rendered Hours: {:0,.2f}" .format(hours))
print("Rate per Hour: {:0,.2f}" .format(rateph))
print("Gross Salary: Php {:0,.2f}".format(gsalary))
print("")
print("=======================DEDUCTIONS==============================")
print("")
print("SSS: {:0,.2f}" .format(sss))
print("PhilHealth: {:0,.2f}" .format(ph))
print("Other Loan: {:0,.2f}" .format(hloan))
print("Tax: {:0,.2f}" .format(gtax))
print("Total Deduction: {:0,.2f}" .format(tdeduction))
print("")
print("Net Salary: PHP {:0,.2f}" .format(nsalary))


# print("Gross Salary: Php {:0,.2f}".format(Salary))