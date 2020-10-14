def generatorPrime():
    
    init = int(input("Enter first value: "))
    final = int(input("Enter last value: "))
    
    list_resumed = []
    my_list = []

    for x in range(init, final):
        lista.append(x)
        lista

    for number in list_resumed:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                my_list.append(number)

    print("This sequence of prime numbers:", myList)

generatorPrime()
