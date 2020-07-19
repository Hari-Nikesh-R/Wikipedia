from tkinter import *
import webbrowser
import wikipedia
def wiki():
    w=wikipedia.random(1)
    var.set(w)
def yeah():
    su=Label(app, text="Summary")
    w=e.get()
    s=wikipedia.summary(w)
    u=""
    s=s.split(" ")
    c=0
    for i in s:
        u+=i
        u=u+" "
        c+=1
        if c==7:
            u=u+"\n"
            c=0
    v.set(u)
    su.grid(row=4,column=1)
    lab=Label(app, text="Do you want see it in webpage?")
    he=Button(app, text="Yes", command=web, width=20)
    lab.grid(row=6,column=1)
    he.grid(row=7, column=1)

def web():
    w=e.get()
    wikiload=wikipedia.page(w)
    url=wikiload.url
    webbrowser.open(url)


app=Tk()
app.title("Wikipedia")
var=StringVar()
v=StringVar()
l=Label(app, text="Article :")
e=Entry(app, textvariable=var, width=40)
b1=Button(app, text="Refresh", width=25, command=wiki)
k=Label(app, text="Are you insterested?")
y=Button(app, text="Yes", width=25, command=yeah)
summa=Label(app, textvariable=v, height=20, width=60)
summa.grid(row=5,column=1)
y.grid(row=3, column=1)
k.grid(row=2,column=1)
b1.grid(row=1, column=2)
e.grid(row=1,column=1)
l.grid(row=1,column=0)
app.mainloop()