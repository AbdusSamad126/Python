basic_salary=float(input("Enter the basic salary: "))
DA=0.7*basic_salary
TA=0.3*basic_salary
HRA=0.1*basic_salary
Gross_salary=basic_salary+DA+TA+HRA
print("\nSalary Details")
print("Basic Salary:",basic_salary)
print("Dearness Allowance :",DA)
print("Travel Allowance :",TA)
print("House Rent Allowance :",HRA)
print("Gross Salary :",Gross_salary)