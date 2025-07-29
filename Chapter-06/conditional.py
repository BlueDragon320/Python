a = int(input("Enter your age: "))
if(a>=18):
    print("You are a major")
    print("You can get a license")
elif(a<0):
    print("Age cannot be less than 0")
else: 
    print("You are a minor")