x = "Y"
c = 0
Name = []
while x == "Y" or x == "y":
    c += 1
    Name.append(input("Enter Name: "))
    x = input("Try again? (Y/y or N/n): ")

print("", c, " Names Entered")
for n in Name:
    print(n)
