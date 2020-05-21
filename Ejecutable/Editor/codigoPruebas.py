from convertidor2 import Convertidor2
while True:
    base=input("¿Qué base es? \n1)'Decimal'\n2)'Binario'\n3)'Hexadecimal'\n4)'Octal'\n5)'Terminar programa'\nOpcion: ")
    if base=="1":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Binario'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ") 
        valor=Convertidor2(num,op)
        if op=="1":
            valor.infod()
            input("Enter para continuar...")
        elif op=="2":
            valor.infod()
            input("Enter para continuar...")
        elif op=="3":
            valor.infod()
            input("Enter para continuar...")
    elif base=="2":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'Hexadecimal'\n3)'Octal'\nOpcion: ")
        valor=Convertidor2(num,op)
        if op=="1":
            valor.infob()
            input("Enter para continuar...")
        elif op=="2":
            valor.infob()
            input("Enter para continuar...")    
        elif op=="3":
            valor.infob()
            input("Enter para continuar...")
    elif base=="3":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'binario'\n3)'Octal'\nOpcion: ")
        valor=Convertidor2(num,op)
        if op=="1":
            valor.infoh()
            input("Enter para continuar...")
        elif op=="2":
            valor.infoh()
            input("Enter para continuar...")    
        elif op=="3":
            valor.infoh()
            input("Enter para continuar...")
    elif base=="4":
        num=input("Dame el numero:")
        op=input("¿Que base lo quieres convertir?\n1)'Decimal'\n2)'Hexadecimal'\n3)'binario'\nOpcion: ")
        valor=Convertidor2(num,op)
        if op=="1":
            valor.infoo()
            input("Enter para continuar...")
        elif op=="2":
            valor.infoo()
            input("Enter para continuar...")    
        elif op=="3":
            valor.infoo()
            input("Enter para continuar...")
    elif base=="5":
            break