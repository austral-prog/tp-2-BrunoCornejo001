def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = (vuelto - pesos)*100
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(int(centavos))
change()
