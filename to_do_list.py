"""Project 1: TKinter GUI To-Do List."""

from tkinter import *
import tkinter.messagebox
import pickle

# Creates the main window
window = Tk()
window.title("Praneel's Project To-Do List")

# Functionality for each button
def add_task():
    task = task_entry.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        task_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except: 
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except: 
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

# Creates listbox frame
frame_listbox = Frame(window)
frame_listbox.pack()

# Hold tasks in a listbox
listbox_tasks = Listbox(frame_listbox, bg="black", fg ="white", height=15, width=50, font="Helvetica")  
listbox_tasks.pack(side="left")

# Task entry text box
task_entry = Entry(window, width=50)
task_entry.pack()
task_entry.bind("<Return>", lambda event: add_task())

# Scroll up and down through list
scrollbar = Scrollbar(frame_listbox)
scrollbar.pack(side="right", fill="y")
listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

# Buttons
button_add_task = Button(window, text="Add Task", width=30, command=add_task)
button_add_task.pack()

button_delete_task = Button(window, text="Delete Task", width=30, command=delete_task)
button_delete_task.pack()

button_save_tasks = Button(window, text="Save Tasks", width=30, command=save_tasks)
button_save_tasks.pack()

button_load_tasks = Button(window, text="Load Tasks", width=30, command=load_tasks)
button_load_tasks.pack()

window.mainloop()