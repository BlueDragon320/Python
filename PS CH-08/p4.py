def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
     

n = int(input("Enter the value of n: "))
print(f"Sum of {n} natural numbers is {sum(n)}")