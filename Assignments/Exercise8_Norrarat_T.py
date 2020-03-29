username = input("username :")
password = input("password :")
if username == "admin" and password == "admin":
    print("welcom BBGUNS Shop")
    print("1.M4 = 200 USD")
    print("2.M416 = 300 USD")
    print("3.M1911 = 160 USD")
    print("4.AK47 = 1 EGG")
    print("Choose your weapon!")
    SelecetInput = int(input(">>"))
    if SelecetInput == 1:
        print("M4 = 200 USD")
        Unit = int(input("Unit = "))
        Total = Unit * 200
        print((Total),"USD")
    elif SelecetInput == 2:
        print("M416 = 300 USD")
        Unit = int(input(">>"))
        Total = Unit * 300
        print((Total),"USD")
    elif SelecetInput == 3:
        print("M1911 = 160 USD")
        Unit = int(input(">>"))
        Total = Unit * 160
        print((Total),"USD")
    elif SelecetInput == 4:
        print("AK47 = 1 EGG")
        Unit = int(input(">>"))
        Total = Unit * 1
        print((Total),"EGG")