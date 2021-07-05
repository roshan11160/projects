import tkinter as tk
def num1(p):
    global k1
    global k3
    global old
    if(k3==0):
        v1.set(old+p)
        old=old+p
        k1=0
    else:
        old=""
        v1.set(old+p)
        old=old+p
        k3=0
def opr1(q):
    global k1
    global k2
    global k3
    global old
    if(k1==0):
        v1.set(old+q)
        old=old+q
        k1=1
        k2=0
        k3=0
        
def dot1(q):
    global k2
    global k1
    global k3
    global old
    if(k3==0):
        if(k2==0):
            v1.set(old+q)
            old=old+q
            k2=1
            k1=1
    else:
       old=""
       v1.set(old+q)
       old=old+q
       k3=0 
def equalto():
    global k2
    global k1
    global k3
    global old
    a1=v1.get()
    old=str(eval(a1))
    v1.set(old)
    k1=0
    k2=0
    k3=1
def back():
    global k2
    global k3
    global k1
    global old
    n5=str(v1.get())
    a3=n5[0:len(n5)-1]
    v1.set(a3)
    old=str(a3)
    ch=n5[len(n5)-1:len(n5)]
    ch1=n5[len(n5)-2:len(n5)-1]
    if(ch=='+' or ch=='-' or ch=='*' or ch=='/'):
        k1=0
    elif(ch=='.'):
        k2=0
    else:
        if(ch1=='+' or ch1=='-' or ch1=='*' or ch1=='/'):
            k1=1
        elif(ch1=='.'):
            k2=1
frame1=tk.Tk()
frame1.title("calculator")

v1=tk.StringVar()
v1.set("0")
old=""
k1=0
k2=0
k3=0
tk.Entry(frame1,textvariable=v1,justify="right",bg="powder blue",font=("arial",20,"bold"),bd=10).grid(columnspan=4)
tk.Button(frame1,text="1",font=("arial",20,"bold"),bd=10,command=lambda:num1('1')).grid(row=1,column=0)
tk.Button(frame1,text="2",font=("arial",20,"bold"),bd=10,command=lambda:num1('2')).grid(row=1,column=1)
tk.Button(frame1,text="3",font=("arial",20,"bold"),bd=10,command=lambda:num1('3')).grid(row=1,column=2)
tk.Button(frame1,text="+",font=("arial",20,"bold"),bd=10,command=lambda:opr1('+')).grid(row=1,column=3)
tk.Button(frame1,text="4",font=("arial",20,"bold"),bd=10,command=lambda:num1('4')).grid(row=2,column=0)
tk.Button(frame1,text="5",font=("arial",20,"bold"),bd=10,command=lambda:num1('5')).grid(row=2,column=1)
tk.Button(frame1,text="6",font=("arial",20,"bold"),bd=10,command=lambda:num1('6')).grid(row=2,column=2)
tk.Button(frame1,text="-",font=("arial",20,"bold"),bd=10,command=lambda:opr1('-')).grid(row=2,column=3)
tk.Button(frame1,text="7",font=("arial",20,"bold"),bd=10,command=lambda:num1('7')).grid(row=3,column=0)
tk.Button(frame1,text="8",font=("arial",20,"bold"),bd=10,command=lambda:num1('8')).grid(row=3,column=1)
tk.Button(frame1,text="9",font=("arial",20,"bold"),bd=10,command=lambda:num1('9')).grid(row=3,column=2)
tk.Button(frame1,text="*",font=("arial",20,"bold"),bd=10,command=lambda:opr1('*')).grid(row=3,column=3)
tk.Button(frame1,text=".",font=("arial",20,"bold"),bd=10,command=lambda:dot1('.')).grid(row=4,column=0)
tk.Button(frame1,text="0",font=("arial",20,"bold"),bd=10,command=lambda:num1('0')).grid(row=4,column=1)
tk.Button(frame1,text="=",font=("arial",20,"bold"),bd=10,command=equalto).grid(row=4,column=2)
tk.Button(frame1,text="/",font=("arial",20,"bold"),bd=10,command=lambda:opr1('/')).grid(row=4,column=3)

tk.Button(frame1,text="back",font=("arial",20,"bold"),bd=10,command=back).grid(row=5,column=3)

frame1.mainloop()
