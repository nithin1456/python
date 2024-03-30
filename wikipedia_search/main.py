
from tkinter import *
import wikipedia

def on_click():
    q = get_q.get()
    text.insert(INSERT,wikipedia.summary(q))




window  = Tk()
window.title("WIKI Search App")
question = Label(window,text="qustion" , font=("Arial",24, "bold"))
question.pack()

get_q = Entry(window,width= 50 ,bd =2 )
get_q.pack()
submit = Button(window,text="search",command=on_click)
submit.pack()
text = Text(window)
text.pack()
window.mainloop()
