import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List-Application")
        self.root.geometry("500x600")  # Change the size to 500x600 pixels
        self.root.configure(bg="#d3d3d3")
        self.tasks = []
        self.load_tasks()


        #the title of the app
        self.app_name = tk.Label(text="TO-DO-APPLICATION")

        

        #Task entry frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=5)


        self.task_name = tk.Label(self.frame, text = "Task name:")
        self.task_name.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.frame,width=53)
        self.entry.pack(side=tk.LEFT, padx=10)

        self.add_btn = tk.Button(self.frame , text = "Add task", command = self.add_task)
        self.add_btn.pack(side=tk.LEFT)
        self.add_btn.configure(bg="black",fg="white")

        #Task list frame
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10)
        
 
        

        self.listbox = tk.Listbox(self.list_frame, width = 75, height = 20, selectmode = tk.SINGLE)
        self.listbox.pack(side = tk.LEFT, fill = tk.BOTH)
        self.listbox.configure(bg="#add8e6")  # Example color: light blue

        

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side = tk.RIGHT, fill =tk.BOTH)

        self.listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command= self.listbox.yview)



        #BUTTONS Frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady = 10)
       

        self.edit_btn = tk.Button(self.btn_frame, text = "Edit task",command=self.edit_task)
        self.edit_btn.pack(side=tk.RIGHT,padx =10)

        self.delete_btn = tk.Button(self.btn_frame, text = "Delete task",command=self.delete_task)
        self.delete_btn.pack(side =tk.RIGHT, padx = 10)

        self.mark_btn = tk.Button(self.btn_frame, text ="Mark as complete ",command=self.mark_task)
        self.mark_btn.pack(side=tk.LEFT, padx =10)



        self.load_task_list()

        #LOGIC OF THE APPLICATION
    def add_task(self):
        task = self.entry.get()

        if task:
            self.tasks.append({"name":task ,"completed":False})
            self.save_tasks()
            self.load_task_list()
            self.entry.delete(0, tk.END)

        else:
            messagebox.showwarning("Warning", "You must enter a task")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)


    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

    def load_task_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['name']
            if task['completed']:
                display_text += "(Completed)"
            self.listbox.insert(tk.END,display_text)

    def edit_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            new_task = self.entry.get()
            if new_task:
                task['name'] = new_task
                self.save_tasks()
                self.load_task_list()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning","You must enter a task")
        else:
            messagebox.showwarning("Warning", "You must select a task to edit")
    
    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.save_tasks()
            self.load_task_list()
        else:
            messagebox.showwarning("Warning","You must select a task to delete")


    def mark_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task['completed'] = not task['completed']
            self.save_tasks()
            self.load_task_list()








   

       






if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


        