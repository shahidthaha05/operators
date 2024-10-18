import tkinter
import sqlite3
# con=sqlite3.connect("tkinder_data.db")
# con.execute('create table sample (uname text,password text)')
win=tkinter.Tk()
win.title('login')
win.configure(bg="grey")
win.minsize(400,400)
win.maxsize(500,500)
def home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text="Home Page",bg='green',fg='blue')
    l1.place(x=150,y=20)
    btn1=tkinter.Button(win2,text="log out",command=win2.quit)
    btn1.place(x=200,y=0)
    win2.mainloop()


def login():
    con=sqlite3.connect("tkinder_data.db")
    data=con.execute("select * from sample")
    f=0
    for i in data:
        if i[0]==e1.get() and i[1]==e2.get():
            f=1
            home()
    if f==0:
        l3.config(text="invalid username or password")

def reg_form():
    win1=tkinter.Tk()
    win1.title('register')
    win1.configure(bg="green")
    win1.minsize(400,400)
    win1.maxsize(500,500)

    def reg():
        con=sqlite3.connect("tkinder_data.db")
        con.execute("insert into sample(uname,password)values(?,?)",(e3.get(),e4.get()))
        con.commit()
        win1.destroy()

    l3=tkinter.Label(win1,text="register",bg='green',fg="white")
    l3.place(x=150,y=20)
    l5=tkinter.Label(win1,text="Fullname")
    l5.place(x=75,y=50)
    l6=tkinter.Label(win1,text="Address")
    l6.place(x=75,y=75)
    e3=tkinter.Entry(win1)
    e3.place(x=150,y=50)
    e4=tkinter.Entry(win1)
    e4.place(x=150,y=80)
    # l7=tkinter.Label(win1,text="phone no")
    # l7.place(x=75,y=100)
    # e5=tkinter.Entry(win1)
    # e5.place(x=150,y=110)

    
    
    


    btn3=tkinter.Button(win1,text="Submmit",bg="gray",activebackground='blue',activeforeground='black',padx=10,pady=8,command=reg)
    btn3.place(x=200,y=150)
    win1.mainloop()


   


l1=tkinter.Label(win,text="Login",bg='grey',fg="white")
l1.place(x=150,y=20)

l2=tkinter.Label(win,text="username")
l2.place(x=75,y=50)
l4=tkinter.Label(win,text="password")
l4.place(x=75,y=75)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)

e2=tkinter.Entry(win)
e2.place(x=150,y=80)



btn1=tkinter.Button(win,text="login",bg="white",activebackground='green',activeforeground='black',padx=10,pady=8,command="save")
btn1.place(x=200,y=120)

btn2=tkinter.Button(win,text="Register",bg="white",activebackground='green',activeforeground='black',padx=10,pady=8,command=reg_form)
btn2.place(x=200,y=200)





win.mainloop()