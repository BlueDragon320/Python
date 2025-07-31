def grt():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))
    if(a > b and a > c):
        print(f"{a} is greater than {b} and {c}") 
    elif(b > a and b > c):
        print(f"{b} is greater than {a} and {c}")
    elif(c > a and c > b):
        print(f"{c} is greater than {a} and {b}")
    else:
        print("Error")
    
grt()