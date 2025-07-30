#Q10. Write a program to print multiplication table of n using for loops in reversed order.
num = int(input("Enter value of n: "))
for i in range(11, 1, -1):
    print(f"{num} x {i - 1} = {num * i}")