from tkinter import *
from tkinter import messagebox
from math import *
from matplotlib import *

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

        h = (abs(x2-x1))/n
        suma_pola = 0
        xstart = x1
        xnext = x1+h

        try:
            while(xstart<x2):
                #oblicz pole
                a = funkcja(wzor,xstart)
                b = funkcja(wzor,xnext)
                pole_trapezu = ((a+b)*h)/2
                suma_pola += pole_trapezu

                #skok do następnego trapezu
                xstart += h
                xstart = round(xstart,6)
                xnext += h
                xnext = round(xnext,6)

            messagebox.showinfo("Wynik", "Wynik to: \n Pole pod funkcją na przedziale <" + "%.3f" % x1 + ";" + "%.3f" % x2 + "> = " +"%.6f" % suma_pola)

        except:
            messagebox.showinfo("Błąd!", "Błędne dane!")

#------GUI------

Label(root,text="Wzór:").pack()
inputformula = Entry(root, bg="#FDFDFD")
inputformula.insert(END,'sin(x**2)+2')
inputformula.pack()

Label(root,text="Zakres:").pack()

Label(root,text="X1:").pack()
inputx1 = Entry(root, bg="#FDFDFD")
inputx1.insert(END,'0')
inputx1.pack()

Label(root,text="X2:").pack()
inputx2 = Entry(root, bg="#FDFDFD")
inputx2.insert(END,'3')
inputx2.pack()

Label(root,text="Ilość trapezów:").pack()
inputn = Entry(root, bg="#FDFDFD")
inputn.insert(END,'20')
inputn.pack()

#Buttons
button1 = Button(root, text="Oblicz",command=trapez)
button1.pack()

messagebox.showinfo("Uwaga!", "Uwaga, program został wypełniony przykładowymi danymi, aby pokazać w jaki sposób należy wypełniać pola. \nAby lepiej zapoznać się ze sposobem działania programu należy przeczytać dokumentację.")

root.mainloop()
