import tkinter as tk


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tarefas")

        self.task_label = tk.Label(master, text="Tarefa:")
        self.task_entry = tk.Entry(master)
        self.add_button = tk.Button(
            master, text="Adicionar", command=self.add_task)
        self.remove_button = tk.Button(
            master, text="Remover", command=self.remove_task)
        self.task_list = tk.Listbox(master)

        self.task_label.grid(row=0, column=0)
        self.task_entry.grid(row=0, column=1)
        self.add_button.grid(row=1, columnspan=2)
        self.remove_button.grid(row=2, columnspan=2)
        self.task_list.grid(row=3, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_text = self.task_list.get(task_index)
            self.task_list.delete(task_index)

    def update_tasks_listbox(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)


root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
