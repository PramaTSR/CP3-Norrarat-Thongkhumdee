def Vatcalculator (total):
    result = total+(total*7/100)
    return result
print(Vatcalculator(int(input("price:"))))