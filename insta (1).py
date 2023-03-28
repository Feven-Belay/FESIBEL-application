import tkinter as tk
from tkinter import*
from Managerr import*
global window

window=Tk()
window.title('Fesibel')

window.geometry("400x500")
window.configure(background='ivory')
window.resizable(10,10)
ob1=Manager()


lblTitle=Label(window,text= "FESIBEL APP",fg='darkblue', font=("italic 38"),bg='ivory')
lblTitle.pack(ipadx=20, ipady=20)


register=tk.Button(text="Register", height="2", width="10",command=ob1.user, font=("bold",22))
register.pack(ipadx=15, ipady=15)
register.pack(padx=80, pady=30)

login=tk.Button(text="Login", height="2", width="10",command=ob1.userlogin,font=("bold",22))
login.pack(ipadx=15, ipady=15)
register.pack(padx=80, pady=70)

window.mainloop()










f