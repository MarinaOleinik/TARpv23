from tkinter import *
from tkinter import messagebox as mb

k=0
def vajuta():
    global k
    k+=1
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k)
def tst_psse(event):
    t=textbox.get()
    if t=="":
        mb.showerror("Tähelepanu!","On vaja sisestada numbrid!")
    else:
        pealkiri.configure(text=t,width=len(t))
        textbox.delete(0,END)
        mb.showinfo("Aruanne","Tekst oli lisatud pealkijasse")
def valik():
    arv=var.get()
    textbox.insert(END,arv)

aken=Tk()
aken.configure(bg="yellow")
aken.geometry("400x600")
aken.iconbitmap('icon.ico')
aken.title("Tkinteri kasutamine")
tekst="Pealkiri"
pealkiri=Label(aken,
               text=tekst,
               bg="#ff7373",
               fg="#133337",
               font="Algerian 20",
               height=3,width=len(tekst),
               cursor="watch")
textbox=Entry(aken,
              bg="#133337",
              fg="#ff7373",
              font="Algerian 20",
              width=20,
              justify=CENTER) #show="*"
nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED,
            bg="lightblue",
            command=vajuta) #SUNKEN, GROOVE
f=Frame(aken)
var=IntVar() #StringVar()
e=Radiobutton(f,text="Esimene",variable=var,value=1,font="Arial 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",command=valik)
k_=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",command=lambda:valik)
nupp.bind("<Button-3>",vajuta_) #PKM
textbox.bind("<Return>",tst_psse) #Enter

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()
obj2=[e,t,k_]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)

aken.mainloop()