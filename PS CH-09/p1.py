r1 = open("poems.txt", "r")
ram = r1.read()
find1 = ram.find("Jonny")

if (find1>=0):
    print("Yes it contains Jonny")
r1.close()
