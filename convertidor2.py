class Convertidor2:
    def __init__(self,numero,base):
        self.__n=numero
        self.__b=base
    @property
    def n(self):
        return self.__n
    
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,valor):
        self.__b=valor    
    def infod(self):
        if self.__b=="1":
            lista=bin(int(self.__n)).split('b')
            print("El numero binario es : ",lista[1])
        elif self.__b=="2":
            lista=hex(int(self.__n)).split('x')
            print("El numero Hexadecimal es : ",lista[1])
        elif self.__b=="3":
            lista=oct(int(self.__n)).split('o')
            print("El numero Octal es : ",lista[1])
    def infob(self):
        if self.__b=="1":
            print("El numero Decimal es : ",int(self.__n,2))
        elif self.__b=="2":
            valor=hex(int(self.__n,2)).split("x")
            print("El numero Hexadecimal es : ",valor[1])
        elif self.__b=="3":
            valor=oct(int(self.__n,2)).split("o")
            print("El numero Octal es : ",valor[1])
    def infoh(self):
        if self.__b=="1":
            print("El numero Decimal es : ",int(self.__n,16)) 
        elif self.__b=="2":
            valor=bin(int(self.__n,16)).split("b")
            print("El numero Hexadecimal es : ",valor[1]) 
        elif self.__b=="3":
            valor=oct(int(self.__n,16)).split("o")
            print("El numero Octal es : ",valor[1])
    def infoo(self):
        if self.__b=="1":
            print("El numero Decimal es : ", int(self.__n,8)) 
        elif self.__b=="2":
            valor=hex(int(self.__n,8)).split("x")
            print("El numero Hexadecimal es : ",valor[1]) 
        elif self.__b=="3":
            valor=bin(int(self.__n,8)).split("b")
            print("El numero Octal es : ",valor[1])