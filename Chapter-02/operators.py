#  1. Arithematic Operator : +, - , *, /
#  2. Assignment Operator: =, +=, -= ....
#  3. Comparision Operator: ==, <, >, <=, >=, !=
#  4. Logical Operators: and, or, not

a = 2
b = 2
print("Addition :", a+b)
print("Subtraction :", a-b)
print("Product :", a*b)
print("Division :", a/b)
a += 1 
print("Increment: ", a)
a -= 2
print("Decrement: ", a)
c = a == b
print(" == : ", c)
c = a >= b
print(" >= : ", c)
c = a <= b
print(" <= : ", c)
c = a != b
print(" != : ", c)


# Logical Operators

A, B = True, False

print(A and B)  # False
print(A or B)   # True
print(not A)    # False
