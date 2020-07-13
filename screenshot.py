import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:/python/screenshots data/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="take screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="quit",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()






