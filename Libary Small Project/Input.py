from tkinter import *
window=Tk()
window.title('Python')
def ibf():
    pass


def ibf():
    p=input.get()
    print(p)
    lablep=Label(window,text=p).pack()

input=Entry(window,width=50,borderwidth=50)
input.pack()
input.focus_set()
input.insert(0,'Enter Your Name: ')
button=Button(window,text='Click Me',width=50,command=ibf).pack()


window.mainloop()