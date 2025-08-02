class Employee:
    language = "Python"
    salary = 120000
    
    def __init__(self): # dunder method which is called automatically
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")
        
harry = Employee()
harry.name = "Harry"
print(harry.name, harry.salary)