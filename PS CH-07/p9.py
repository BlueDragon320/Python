#Q9. Write a program to print the following star pattern.
# * * *
# *   *  for n = 3
# * * *

n = 3
for i in range (1, n):
    print("*" * 3)
    for i in range ((i+1)%2==0):
        print("* *")
