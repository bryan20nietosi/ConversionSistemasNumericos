from convertidor import Convertidor
while True:
    base=input("¿Qué base es? \n1)'Decimal'\n2)'Binario'\n3)'Hexadecimal'\n4)'Octal'\n5)'Terminar programa'\nOpcion: ")
    if base=="1":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Binario'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ") 
        if op=="1":
            valor=Convertidor(num,op)
            valor.infod()
            input("Enter para continuar...")
        elif op=="2":
            valor=Convertidor(num,op)
            valor.infod()
            input("Enter para continuar...")
        elif op=="3":
            valor=Convertidor(num,op)
            valor.infod()
            input("Enter para continuar...")
    elif base=="2":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ")
        if op=="1":
            valor=Convertidor(num,op)
            valor.infob()
            input("Enter para continuar...")
        elif op=="2":
            valor=Convertidor(num,op)
            valor.infob()
            input("Enter para continuar...")    
        elif op=="3":
            valor=Convertidor(num,op)
            valor.infob()
            input("Enter para continuar...")
    elif base=="3":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'binario'\n3)'Octal'\nOpcion: ")
        if op=="1":
            valor=Convertidor(num,op)
            valor.infoh()
            input("Enter para continuar...")
        elif op=="2":
            valor=Convertidor(num,op)
            valor.infoh()
            input("Enter para continuar...")    
        elif op=="3":
            valor=Convertidor(num,op)
            valor.infoh()
            input("Enter para continuar...")
    elif base=="4":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'Hexadecimal'\n3)'binario'\nOpcion: ")
        if op=="1":
            valor=Convertidor(num,op)
            valor.infoo()
            input("Enter para continuar...")
        elif op=="2":
            valor=Convertidor(num,op)
            valor.infoo()
            input("Enter para continuar...")    
        elif op=="3":
            valor=Convertidor(num,op)
            valor.infoo()
            input("Enter para continuar...")
    elif base=="5":
            break