import tkinter

win=tkinter.Tk()
win.title("batch8")
win.configure(bg="green")
win.minsize(400,500)
win.maxsize(500,500)
def save():
    l3.config(text=u1.get())



l1=tkinter.Label(win,text='welcome to all',bg="green",fg="blue")
l1.pack()
l1.place(x=100,y=20)
l1.grid(row=0,column=0)

l2=tkinter.Label(win,text='welcome to all')
l2.pack()
l2.place(x=100,y=200)
l2.grid(row=1,column=1)

# for crating a single program in a single page 

l1=tkinter.Label(win,text='welcome to all',bg="green",fg="blue")
l1.place(x=150,y=10)

l2=tkinter.Label(win,text="name" )
l2.place(x=75,y=50)

u1=tkinter.Entry(win)
u1.place(x=150,y=50)

btn=tkinter.Button(win,text="save",bg='gray',activebackground='black',activeforeground='white',command=s)
btn.place(x=150,y=80)

l3=tkinter.Label(win)
l3.place(x=150,y=100)



win.mainloop()



