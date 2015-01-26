from dateinput import *
import ttk

win = tk.Tk()
win.title('DateEntry demo')

dentrys = DateEntry(win)
dentrys.pack()

def show_contents(e):
        print dentrys.get()

win.bind('<Return>', show_contents)
win.mainloop()