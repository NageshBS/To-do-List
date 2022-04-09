#importing modules

import tkinter 
import tkinter.messagebox
import json
from PIL import ImageTk,Image
# funtions <---Main--->

tasks = []

def add_task():
    task = task_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
    task_input.delete(0,"end")

def delete_task():
    task = listbox_tasks.get("active")
    if tkinter.messagebox.askyesno(title="Confirm:Done", message="This task is completed !"):
        if task in tasks:
            tasks.remove(task)
    update_listbox()

def load_tasks():
    with open('tasks.txt', 'r') as f:
        saved_tasks = json.loads(f.read())
    for task in saved_tasks:
        tasks.append(task)
    update_listbox()
    tkinter.messagebox.showinfo(title="Successfull", message="Tasks are Loaded")

def clear_tasks():
    global tasks
    if tkinter.messagebox.askyesno(title="Confirm:Delete All", message="Do you really want to delete all"):
        tasks =[]
    update_listbox()

def save_tasks():
    with open('tasks.txt', 'w') as f:
        f.write(json.dumps(tasks))
    tkinter.messagebox.showinfo(title="Successfull", message="Tasks are Saved")    

def update_listbox():
    clear_listbox()
    for task in tasks:       
        listbox_tasks.insert("end",task)

def clear_listbox():
    listbox_tasks.delete(0,"end")

#creating root window
root = tkinter.Tk()
root.geometry("550x650")
root.title("To-Do List")

img = Image.open("BG.jpeg")
bg = ImageTk.PhotoImage(img)
lbl_title = tkinter.Label(root,image=bg)
lbl_title.place(x = 0, y = 0)

# label for tittle
lbl_title = tkinter.Label(root,text="To-do-List",font=("Arial Bold",35),bg="black",fg="white")
lbl_title.pack(pady=5)

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

# list box for the tasks
listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=55, font=("Arial Bold",13),bg="White",justify=tkinter.CENTER)
listbox_tasks.pack(side=tkinter.LEFT,border=None)

#scroll bar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# task input
task_input = tkinter.Entry(root,width=60)
task_input.pack(padx=10, pady=10)

#buttons
button_add_task = tkinter.Button(root, text="Add task", font=("Arial Bold",12),width=18,bg="black",fg="white",command=add_task)
button_add_task.pack(padx=10, pady=7)

button_delete_task = tkinter.Button(root, text="Delete Task",font=("Arial Bold",12),width=18,bg="black",fg="white",command=delete_task)
button_delete_task.pack(padx=10, pady=7)

button_load_tasks = tkinter.Button(root, text="Load tasks",font=("Arial Bold",12),width=18,bg="black",fg="white",command=load_tasks)
button_load_tasks.pack(padx=10, pady=7)

button_clear_tasks = tkinter.Button(root, text="Clear tasks",font=("Arial Bold",12),width=18,bg="black",fg="white",command=clear_tasks)
button_clear_tasks.pack(padx=10, pady=7)

button_save_tasks = tkinter.Button(root, text="Save tasks",font=("Arial Bold",12),width=18,bg="black",fg="white",command=save_tasks)
button_save_tasks.pack(padx=10, pady=7)

#starting main event window loop
root.mainloop()
