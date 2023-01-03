from tkinter import *
window = Tk()

window.title("test application")
window.geometry('400x200')

lbl1 = Label(window, text="displacements :")
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Final velocity")
lbl2.grid(column=1, row=0)
lbl3 = Label(window, text="Initial velocity")
lbl3.grid(column=2, row=0)
lbl4 = Label(window, text="time")
lbl4.grid(column=3, row=0)
result = Label(window, text="Result : ")
result.grid(column=1, row=3)

txt1 = Entry(window,width=10)
txt1.grid(column=1, row=1)
txt2 = Entry(window,width=10)
txt2.grid(column=2, row=1)
txt3 = Entry(window,width=10)
txt3.grid(column=3, row=1)



def clicked():
    # res = "Welcome to " + txt.get()
    v = txt1.get()
    v = int(v)
    u = txt2.get()
    u = int(u)
    t = txt3.get() 
    t = int(t)
    r1 = v + u
    r2 = r1 / 2
    r3 = r2 * t
    result.configure(text = r3)
    print("f = ", r3, " | v = ", v, " | u = ", u, " | t = ", t)

def clear():
    # txt3 = Label(window, text="Result : ")
    txt1.configure(text = "")
    txt2.configure(text = "")
    txt3.configure(text = "")
    result.configure(text = "0")
    print("log cleard")

btn = Button(window, text="view calculate", command=clicked)
btn.grid(column=0, row=3)

btnClear = Button(window, text="clear", command=clear)
btnClear.grid(column=2, row=3)

window.mainloop()



'''
f = (v+u/2)t
    v - awasana prawegaya (ms-1)
    u - arambaca prawegaya (ms-1)
    t - time

    v-10 u-20 t-5
    20 / 2 * t
'''


