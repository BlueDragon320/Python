#Q4. Write a program to find whether a given username contains less than 10 characters or not.
word = input("Enter a word: ")
num_of_char = len(word)
if(num_of_char > 10):
    print("The username contains more than 10 characters.")
else: 
    print("User name is good")