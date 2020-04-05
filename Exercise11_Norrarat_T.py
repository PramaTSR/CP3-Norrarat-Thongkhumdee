UserInput = int(input("number:"))
for x in range(UserInput):
    print(" " * (UserInput - x - 1)+((2*x)+1) * "*")