from tkinter import *
from tkinter import messagebox
from math import *

root = Tk()
root.title("Metoda trapezów")
root.geometry("250x230")
root.resizable(width=False, height=False)

#----FUNCTIONS-----

def funkcja(wzor,x):
    wz = lambda x: eval(wzor)
    return wz(x)

def trapez():
    if(inputformula.get()=="" or inputx1.get()=="" or inputx2.get()=="" or inputn.get()==""):
        messagebox.showinfo("Błąd!", "Brak danych!")
    else:
        #odczyt informacji
        wzor = inputformula.get()
        x1 = float(inputx1.get())
        x2 = float(inputx2.get())
        n = float(inputn.get())

        h = (x2-x1)/n

        suma_pola = 0

        xstart = x1
        xnext = x1+h

        while(xstart<=x2):
            #oblicz pole
            a = funkcja(wzor,xstart)
            b = funkcja(wzor,xnext)
            pole_trapezu = ((a+b)*h)/2
            suma_pola += pole_trapezu
            #skok do następnego trapezu
            xstart += h
            xnext += h

        messagebox.showinfo("Wynik", "Wynik to: \n Pole pod funkcją na przedziale <" + str(int(x1)) + ";" + str(int(x2))+ "> =" +"%.10f" % suma_pola)

#------GUI------

formulaLabel = Label(root,text="Wzór:")
formulaLabel.pack()
inputformula = Entry(root, bg="#FDFDFD")
inputformula.pack()

zLabel = Label(root,text="Zakres:")
zLabel.pack()

x1Label = Label(root,text="X1:")
x1Label.pack()
inputx1 = Entry(root, bg="#FDFDFD")
inputx1.pack()

x2Label = Label(root,text="X2:")
x2Label.pack()
inputx2 = Entry(root, bg="#FDFDFD")
inputx2.pack()

nLabel = Label(root,text="Ilość trapezów:")
nLabel.pack()
inputn = Entry(root, bg="#FDFDFD")
inputn.pack()

#Buttons
button1 = Button(root, text="Oblicz",command=trapez)
button1.pack()

root.mainloop()
