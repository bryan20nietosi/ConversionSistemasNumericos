while True:
    base=input("¿Qué base es? \n1)'Decimal'\n2)'Binario'\n3)'Hexadecimal'\n4)'Octal'\n5)'Terminar programa'\nOpcion: ")
    
    if base=="1":
        numero=int(input("Dame el numero:"))
        lista1=bin(numero).split("b")
        lista2=oct(numero).split("o")
        lista3=hex(numero).split("x")
        base_convertir=input("¿Que base lo quieres convertir?\n1)'Binario'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ")
        if base_convertir=="1":
            print("Numero: ",lista1[1])
            input("Enter para continuar...")
        elif base_convertir=="2":
            print("Numero: ",lista3[1])
            input("Enter para continuar...")
        elif base_convertir=="3":
            print("Numero: ",lista2[1])
            input("Enter para continuar...")
    
    elif base=="2":
        numero=input("Dame el numero:")
        base_convertir=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ")
        if base_convertir=="1":
            print("Numero: ",int(numero,2))
            input("Enter para continuar...")
        elif base_convertir=="2":
            listah=hex(int(numero,2)).split("x")
            print("Numero: ",listah[1])
            input("Enter para continuar...")
        elif base_convertir=="3":
            listao=oct(int(numero,2)).split("o")
            print("Numero: ",listao[1])
            input("Enter para continuar...")
            
    elif base=="3":
        numero=input("Dame el numero:")
        base_convertir=input("¿Que base lo quieres convertir?\n1)'Binario'\n2)'Decimal'\n3)'Octal'\nOpcion: ")
        if base_convertir=="1":
            listab=bin(int(numero,16)).split("b")
            print("Numero: ",listab[1])
            input("Enter para continuar...")
        elif base_convertir=="2":
            print("Numero: ",int(numero,16))
            input("Enter para continuar...")
        elif base_convertir=="3":
            listao=oct(int(numero,16)).split("o")
            print("Numero: ",listao[1])
            input("Enter para continuar...")
            
    elif base=="4":
        numero=input("Dame el numero:")
        base_convertir=input("¿Que base lo quieres convertir?\n1)'Binario'\n2)'Hexadecimal'\n3)'Decimal'\nOpcion: ")
        if base_convertir=="1":
            listao=bin(int(numero,8)).split("b")
            print("Numero: ",listao[1])
            input("Enter para continuar...")
        elif base_convertir=="2":
            listah=hex(int(numero,8)).split("x")
            print("Numero: ",listah[1])
            input("Enter para continuar...")            
        elif base_convertir=="3":
            print("Numero: ",int(numero,8))
            input("Enter para continuar...")
    elif base=="5":
        break
