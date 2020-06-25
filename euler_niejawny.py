from tkinter import *
from tkinter import messagebox
from math import *
import numpy
import scipy.optimize

root = Tk()
root.title("Euler niejawny")
root.geometry("470x180")
root.resizable(width=False, height=False)

#----FUNCTIONS-----

def eulerNiejawny():
    #odczyt informacji
    if(fy1Input.get()=="" or fy2Input.get()=="" or gy1Input.get()=="" or gy2Input.get()=="" or inputy1.get()=="" or inputy2.get()=="" or inputX.get()=="" or inputKrok.get()==""):
        messagebox.showinfo("Błąd!", "Brak danych!")
    else:
        y1 = float(inputy1.get())
        y2 = float(inputy2.get())
        krok = float(inputKrok.get())
        fy1 = float(fy1Input.get())
        fy2 = float(fy2Input.get())
        gy1 = float(gy1Input.get())
        gy2 = float(gy2Input.get())
        wf = float(wfInput.get())
        wg = float(wgInput.get())

        A = numpy.array([[(fy1-1),fy2],[gy1,(gy2-1)]])
        B = numpy.array([y1-wf,y2-wg])
        Z = numpy.linalg.solve(A,B)*-1
        messagebox.showinfo("Wynik", "Wynik to:\nY1="+str(round((Z[0]),8))+"\nY2="+str(round((Z[1]),8)))
        #messagebox.showinfo("Błąd!", "Błędne dane!")

#------GUI------
Label(root,text="f = ").grid(row=0,column=0)
fy1Input = Entry(root,bg="#FDFDFD")
fy1Input.insert(END,'1')
fy1Input.grid(row=0,column=1)
Label(root,text="y1+ ").grid(row=0,column=2)
fy2Input = Entry(root,bg="#FDFDFD")
fy2Input.insert(END,'-3')
fy2Input.grid(row=0,column=3)
Label(root,text="y2+ ").grid(row=0,column=4)
wfInput = Entry(root,bg="#FDFDFD")
wfInput.insert(END,'0')
wfInput.grid(row=0,column=5)

Label(root,text="g = ").grid(row=1,column=0)
gy1Input = Entry(root,bg="#FDFDFD")
gy1Input.insert(END,'3')
gy1Input.grid(row=1,column=1)
Label(root,text="y1+ ").grid(row=1,column=2)
gy2Input = Entry(root,bg="#FDFDFD")
gy2Input.insert(END,'-1')
gy2Input.grid(row=1,column=3)
Label(root,text="y2+ ").grid(row=1,column=4)
wgInput = Entry(root,bg="#FDFDFD")
wgInput.insert(END,'0')
wgInput.grid(row=1,column=5)

Label(root,text="y1(0):").grid(row=2,column=0)
inputy1 = Entry(root, bg="#FDFDFD")
inputy1.insert(END,'2')
inputy1.grid(row=2,column=1)

Label(root,text="y2(0):").grid(row=3,column=0)
inputy2 = Entry(root, bg="#FDFDFD")
inputy2.insert(END,'1')
inputy2.grid(row=3,column=1)

Label(root,text="Krok:").grid(row=4,column=0)
inputKrok = Entry(root, bg="#FDFDFD")
inputKrok.insert(END,'1')
inputKrok.grid(row=4,column=1)

Label(root,text="X:").grid(row=5,column=0)
inputX = Entry(root, bg="#FDFDFD")
inputX.insert(END,'1')
inputX.grid(row=5,column=1)

#Buttons
button1 = Button(root, text="Oblicz",command=eulerNiejawny)
button1.grid(row=6,column=3)

root.mainloop()
