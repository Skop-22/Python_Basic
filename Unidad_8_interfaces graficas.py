from tkinter import *
raiz=Tk()#primera ventana
raiz.title("Primera ventana")
#raiz.resizable(False,False)#Para cambier si se quiere hacer mas grande la bentana
raiz.iconbitmap("camara.ico")#para icono principal
#raiz.geometry("500x300")#para las dimenciones
raiz.config(bg="blue")
#s=sur
#n=norte
#e=este
miPrimer_Frame=Frame()#parasaber lo que va dentro
miPrimer_Frame.pack(side="right",ancho="e")#isquierda sur
miPrimer_Frame.config(bg="green")
miPrimer_Frame.config(width="500",height="300")
miPrimer_Frame.config(bd=20)
miPrimer_Frame.config(relief="groove")#relieve
miPrimer_Frame.config(cursor="pirate")#cursor manita
#siempre debe estar al final el mainloop
raiz.mainloop()#fin de la primera ventana
#raiz2=Tk()
#raiz2.mainloop()#segunda ventana
