import tkinter as tk
import vlc
from tkinter import *


def main():
    root = tk.Tk()
    root.title('Timer')
    w = 400
    h = 300
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    master_icon = PhotoImage(file='resourses/clock.png')
    root.iconphoto(True, master_icon)
    top_text = tk.Label(text='Enter the time for the timer, or exit this window to quit')
    input_prompt = Entry(root)
    input_prompt.pack()
    top_text.pack()
    input_prompt.focus_set()
    label = tk.Label(root, font=('Ariel', 50))
    label['text'] = ''
    label.place(x=125, y=100)

    def timer():
        def countdown(count):
            Count = int(count)
            label['text'] = str(count)
            label.place(x=125, y=100)
            label.config(font=('Ariel', 100))
            if Count > 0:
                root.after(1000, countdown, Count - 1)
            elif Count == 0:
                label.config(font=('Ariel', 50))
                label.place(x=50, y=125)
                label['text'] = 'Times Up!'
                p = vlc.MediaPlayer('resourses/alarm.m4a')
                p.play()

        Time = input_prompt.get()
        countdown(Time)

    b = tk.Button(root, text="OK", width=10, command=timer)
    b.pack()
    root.mainloop()


main()
