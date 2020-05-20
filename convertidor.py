class Convertidor:
    def __init__(self,numero,opcion):
        self.__n=numero
        self.__o=opcion
    def infod(self):
        op=self.__o
        if op=="1":
            lista=bin(int(self.__n)).split('b')
            print("El numero binario es : ",lista[1])
        elif op=="2":
            lista=hex(int(self.__n)).split('x')
            print("El numero Hexadecimal es : ",lista[1])
        elif op=="3":
            lista=oct(int(self.__n)).split('o')
            print("El numero Hexadecimal es : ",lista[1])
    def infob(self):
        op=self.__o
        if op=="1":
            print("El numero Decimal es :",int(self.__n,2)) 
        elif op=="2":
            valor=hex(int(self.__n,2)).split("x")
            print("El numero Hexadecimal es :", valor[1]) 
        elif op=="3":
            valor=oct(int(self.__n,2)).split("o")
            print("El numero Octal es :", valor[1])
    def infoh(self):
        op=self.__o
        if op=="1":
            print("El numero Decimal es :",int(self.__n,16)) 
        elif op=="2":
            valor=bin(int(self.__n,16)).split("b")
            print("El numero Hexadecimal es :", valor[1]) 
        elif op=="3":
            valor=oct(int(self.__n,16)).split("o")
            print("El numero Octal es :", valor[1])
    def infoo(self):
        op=self.__o
        if op=="1":
            print("El numero Decimal es :",int(self.__n,8)) 
        elif op=="2":
            valor=hex(int(self.__n,8)).split("x")
            print("El numero Hexadecimal es :", valor[1]) 
        elif op=="3":
            valor=bin(int(self.__n,8)).split("b")
            print("El numero Octal es :", valor[1])