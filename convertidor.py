class Convertidor:
    def __init__(self,numero,base):
        self.__n=numero
        self.__b=base
    def infod(self):
        op=self.__b
        if op=="2":
            lista=bin(int(self.__n)).split('b')
            return f"El numero binario es : {lista[1]}"
        elif op=="16":
            lista=hex(int(self.__n)).split('x')
            return f"El numero Hexadecimal es : {lista[1]}"
        elif op=="8":
            lista=oct(int(self.__n)).split('o')
            return f"El numero Octal es : {lista[1]}"
    def infob(self):
        op=self.__b
        if op=="10":
            return f"El numero Decimal es : {int(self.__n,2)}" 
        elif op=="16":
            valor=hex(int(self.__n,2)).split("x")
            return f"El numero Hexadecimal es : {valor[1]}" 
        elif op=="8":
            valor=oct(int(self.__n,2)).split("o")
            return f"El numero Octal es : {valor[1]}"
    def infoh(self):
        op=self.__b
        if op=="10":
            return f"El numero Decimal es : {int(self.__n,16)}" 
        elif op=="2":
            valor=bin(int(self.__n,16)).split("b")
            return f"El numero Hexadecimal es : {valor[1]}" 
        elif op=="8":
            valor=oct(int(self.__n,16)).split("o")
            return f"El numero Octal es : {valor[1]}"
    def infoo(self):
        op=self.__b
        if op=="10":
            return f"El numero Decimal es : {int(self.__n,8)}" 
        elif op=="16":
            valor=hex(int(self.__n,8)).split("x")
            return f"El numero Hexadecimal es : {valor[1]}" 
        elif op=="2":
            valor=bin(int(self.__n,8)).split("b")
            return f"El numero Octal es : {valor[1]}"