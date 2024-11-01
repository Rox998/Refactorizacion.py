def num():
    num = 0
    while num < 3:
        if num == 1:
            print("es igual a ")
        elif num == 2:
            print("es igual a 2")
        elif num == 3:
            print("finalizando")
            break
        else:
            print("introduzca un numero del 1 al 6")
            num +=1 
    num()
