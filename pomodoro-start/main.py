
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
tm1=None



def reset_timer():
    w.after_cancel(tm1)
    c.itemconfig(timer_txt,text ="00:00")
    ttl.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break)
        ttl.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break)
        ttl.config(text="BREAK",fg=PINK)

    else:
        count_down(work_sec)
        ttl.config(text="WORK",fg=GREEN)





def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    c.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
         global tm1
         tm1=w.after(1000,count_down,count-1)

    else:
        start()
        mark = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            mark += "✔"
            check.config(text=mark)





w = Tk()

w.title("tomato")
w.config(padx=100,pady=50, bg=YELLOW)
ttl = Label(fg=GREEN ,font=(FONT_NAME, 50, "bold"),bg=YELLOW,highlightthickness=0)
ttl.grid(column =1,row=0)


c = Canvas(width=200, height=224, bg =YELLOW, highlightthickness=0)
i = PhotoImage(file="tomato.png")
c.create_image(100, 112, image=i)
timer_txt = c.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
c.grid(column=1, row=1)

s = Button(text="Start", highlightthickness=0, command=start)
s.grid(column=0, row=2)
e = Button(text="Reset",highlightthickness=0,command=reset_timer)
e.grid(column=2, row=2)
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,10))
check.grid(column=1, row=3)




w.mainloop()