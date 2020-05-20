import tkinter
from convertidor import Convertidor

ventana=tkinter.Tk()
ventana.geometry("400x200")
ventana.title("Programa de Conversiones")
etiqueta = tkinter.Label(ventana, text="Bryan Nieto Silva, 1745637", bg="green")
etiqueta.pack(fill = tkinter.X)

informacion=tkinter.Label(ventana,text="Conversiones de: Decimal,Binario,Octal,Hexadecimal", bg="orange")
informacion.pack(side= tkinter.BOTTOM)
etiqueta2= tkinter.Label(ventana, text="Base Inicial")
etiqueta2.pack(fill= tkinter.X)

cajatexto=tkinter.Entry(ventana)
cajatexto.pack()

etiqueta3= tkinter.Label(ventana, text="Numero")
etiqueta3.pack(fill=tkinter.X)
cajatexto2=tkinter.Entry(ventana)
cajatexto2.pack()

etiqueta4= tkinter.Label(ventana, text="Base a convertir")
etiqueta4.pack(fill=tkinter.X)
cajatexto3=tkinter.Entry(ventana)
cajatexto3.pack()

resultado=tkinter.Label(ventana)
resultado.pack()

def convierte():
    base_inicial=cajatexto.get()
    numero=cajatexto2.get()
    base_convertir=cajatexto3.get()
    if base_inicial=="10":
        valor=Convertidor(numero,base_convertir)
        mostrar=valor.infod()
        resultado["text"]= mostrar
    elif base_inicial=="2":
        valor=Convertidor(numero,base_convertir)
        mostrar=valor.infob()
        resultado["text"]= mostrar
    elif base_inicial=="8":
        valor=Convertidor(numero,base_convertir)
        mostrar=valor.infoo()
        resultado["text"]= mostrar
    elif base_inicial=="16":
        valor=Convertidor(numero,base_convertir)
        mostrar=valor.infoh()
        resultado["text"]= mostrar

boton=tkinter.Button(ventana, text="Convertidor", command = convierte)
boton.pack()
ventana.mainloop()