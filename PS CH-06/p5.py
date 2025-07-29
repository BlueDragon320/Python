#Q5. Write a program which finds out whether a given name is present in a list or not.
name = input("Enter your name: ").lower()
names = ["john", "golu", "gian", "sunio"]

if name in names:
    print("Villain is there")
else:
    print("Not a villain")
