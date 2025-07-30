#Q2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]
for naam in l:
    if(naam.startswith("S")):
        print(f"Hello {naam}")