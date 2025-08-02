class Employee:
    language = "Py"
    salary = 1299999

harry = Employee()
harry.language = "JavaScript" #This is instance attribute
print(harry.language, harry.salary)

# This will print instance attribute as it has priority over class attribute