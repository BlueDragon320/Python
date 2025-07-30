#Q6. Write a program to find the factorial of given number using for loop.
n = int(input("Enter the value: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"Factorial of {n} = {product}")