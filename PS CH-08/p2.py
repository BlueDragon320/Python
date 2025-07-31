def temp(c):
    f = c * (9/5) + 32
    return f

c = int(input("Enter the temperature in Degree Celcius: "))
print(f"Temperature in calsius {c} to Fahrenheit is {temp(c)}")