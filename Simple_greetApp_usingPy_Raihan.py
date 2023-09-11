import tkinter as tk
from tkinter import ttk

root=tk.Tk()
main=ttk.Frame(root)
main.pack(side="bottom",fill="both",expand=True)

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

user_name=tk.StringVar()

name_label=ttk.Label(root,text="Name: ")
name_label.pack(side="left", padx=(0, 10),expand=True)

name_entry=ttk.Entry(root,width=15,textvariable=user_name)
name_entry.pack(side="left",expand=True)
name_entry.focus()

greet_button=ttk.Button(main,text="Greet",command=greet)
greet_button.pack(side="left",fill="x",expand=True)

quit_button=ttk.Button(main,text="Quit",command=root.destroy)
quit_button.pack(side="left",fill="x",expand=True)


root.mainloop()