from tkinter import *
from tkinter import messagebox
from math import *

root = Tk()
root.title("Euler jawny")
root.geometry("250x250")
root.resizable(width=False, height=False)

#----FUNCTIONS-----

def funkcja(wzor,x,y):
    wz = lambda x,y: eval(wzor)
    return wz(x,y)

def eulerJawny():
    if(inputformula.get()=="" or inputx.get()=="" or inputx0.get()=="" or inputy0.get()=="" or inputh.get()==""):
        messagebox.showinfo("Błąd!", "Brak danych!")
    else:
        #odczyt informacji
        wzor = inputformula.get()
        x = float(inputx.get())
        x0 = float(inputx0.get())
        y0 = float(inputy0.get())
        h = float(inputh.get())


        xk=(x*1000000)-(x0*1000000)
        xk = int(xk)
        hk=int(h*1000000)

        if xk%hk==0 and h>0 and x>x0:
            try:
                tablicaX= [x0]
                while(tablicaX[-1]<x):
                    tablicaX.append(tablicaX[-1]+h)
                tablicaY = [y0]
                for i in range(1,len(tablicaX)-1):
                    tablicaY.append(tablicaY[-1]+h*funkcja(wzor,tablicaX[i],tablicaY[-1]))
                messagebox.showinfo("Wynik", "Wynik to Y="+str(round((tablicaY[-1]),8)))
            except:
                messagebox.showinfo("Błąd!", "Błędne dane! Niepoprawny zapis funkcji!")
        else:
            messagebox.showinfo("Błąd!", "Błędne dane! Krok nigdy nie dotrze do oczekiwanego X'sa!")

#------GUI------

Label(root,text="Wzór:").pack()
inputformula = Entry(root, bg="#FDFDFD")
inputformula.insert(END,'x+2*y')
inputformula.pack()

Label(root,text="X:").pack()
inputx = Entry(root, bg="#FDFDFD")
inputx.insert(END,'0.4')
inputx.pack()

Label(root,text="X0:").pack()
inputx0 = Entry(root, bg="#FDFDFD")
inputx0.insert(END,'0')
inputx0.pack()

Label(root,text="Y0:").pack()
inputy0 = Entry(root, bg="#FDFDFD")
inputy0.insert(END,'0')
inputy0.pack()

Label(root,text="Krok:").pack()
inputh = Entry(root, bg="#FDFDFD")
inputh.insert(END,'0.1')
inputh.pack()

#Buttons
button1 = Button(root, text="Oblicz",command=eulerJawny)
button1.pack()

messagebox.showinfo("Uwaga!", "Uwaga, program został wypełniony przykładowymi danymi, aby pokazać w jaki sposób należy wypełniać pola. \nAby lepiej zapoznać się ze sposobem działania programu należy przeczytać dokumentację.")

root.mainloop()
