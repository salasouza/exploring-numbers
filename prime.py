def generatorPrime():
    
    init = int(input("Enter first value: "))
    final = int(input("Enter last value: "))
    
    lista = []
    myList = []

    for x in range(0, final):
        lista.append(x)
        lista

    for number in lista:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                myList.append(number)

    print("This sequence of prime numbers:", myList)

generatorPrime()
