import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Task list
        self.tasks = []

        # Create task listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        # Entry for new task
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Mark as Done", command=self.mark_as_done)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] = f"[Done] {self.tasks[task_index]}"
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
