import tkinter as tk
from tkinter import ttk
import urls

# root window
root = tk.Tk()
root.geometry('475x150')
root.resizable(False, False)
root.title('ESP APP')

# Boton windows
windows_button = ttk.Button(
    root,
    text='Abrir HTML',
    command=lambda: urls.openwindows()
)

windows_button.pack(
    ipadx=2,
    ipady=2,
    side="left"
)
windows_button.place(
    x=75,
    y=75
)


#Boton Start
start_button = ttk.Button(
    root,
    text='Empezar a grabar',
    command=lambda: urls.startrecord()
)

start_button.pack(
    ipadx=2,
    ipady=2
)
start_button.place(
    x=175,
    y=75
)


#Boton Stop

stop_button = ttk.Button(
    root,
    text='Detener Grabación',
    command=lambda: urls.stoprecord()
)

stop_button.pack(
    ipadx=5,
    ipady=5,
    side="right"
)

stop_button.place(
    x=300,
    y=75
)
root.mainloop()