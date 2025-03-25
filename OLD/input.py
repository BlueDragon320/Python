"""# Double quote can be given as output by using the below code
# To use multiple vairables we can use ' , ' instead of +
# input [it is used to take input from user]
# name = [assign vaiable]

# name = input("What's your name? ")
# print("Hello," + name)
# print("Hello, ", name)

# print("hello, \"friend\"")


#Use function in the main input
name = input ("What's your name? ").strip().title()
# OR
#name = input("What's your name? ")
# Removes whitespace from str
#name = name.strip()
# Capitalize user's name
#name = name.capitalize()
# OR
# way to use both function
name = name.strip().title()
# Say hello to user 
print(f"hello, {name}")
"""




# Ask User to input
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split()

# Say hello to user
print(f"hello, {first}")

# Input was given as ben dover output Ben 