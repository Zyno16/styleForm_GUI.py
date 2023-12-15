import tkinter
from tkinter import ttk

form =tkinter.Tk()

form.geometry("700x500")
form.config(background ="#ffffff")

fnt=("tahoma",20)

lbls=ttk.Style()
lbls.configure("TLabel",font =fnt ,background ="#00ff00")

lblname = ttk.Label(form , text="Enter you name" ,style = "TLabel")
txtname = ttk.Entry(form , font = fnt)

lbladdress = ttk.Label(form, text ="Enter your address:",style = "TLabel")
txtaddress = ttk.Entry(form,font =fnt )

lblname.pack()
txtname.pack()
lbladdress.pack()
txtaddress.pack()

form.mainloop()
