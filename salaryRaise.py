
salary = float(input("Please enter your salary: "))

if salary < 0:
    print("Invalid Value!")

else:

    if 0 < salary <= 1000:
        salary = salary + salary * 0.15
    elif 1000 < salary <= 2000:
        salary = salary + salary * 0.10
    elif 2000 < salary <= 3000:
        salary = salary + salary * 0.05
    else:
        salary = salary + salary * 0.025

print("Your raised salary is: " , salary)
