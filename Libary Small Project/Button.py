from tkinter import *
window=Tk()
window.title("Output")
def btnf():
    btlable=Label(window,text='Working').grid(row=3,column=0)
btn=Button(window,text="Click Me", fg='red',bg='black',
           padx=5,pady=5,command=btnf).grid(row=2,column=2)

window.mainloop()