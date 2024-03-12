import pyautogui
import time
import tkinter as tk

def screen_shot():
    time.sleep(3)
    name = time.time()
    img = pyautogui.screenshot()
    img.save("f{name}.png")
    img.show()




root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="Take screen shot",command=screen_shot)
button.pack(side=tk.LEFT)
close = tk.Button(frame,text="Quit" ,command=quit)
close.pack(side=tk.LEFT)
root.mainloop()