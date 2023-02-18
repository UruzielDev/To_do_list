import os
import pickle
import tkinter as tk

class TodoItem:
    def __init__(self, task, completed=False, category=None):
        self.task = task
        self.completed = completed
        self.category = category

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    # rest of the code

    def mark_complete(self, item):
        item.completed = True

    def edit_item(self, item, task=None, completed=None, category=None):
        if task:
            item.task = task
        if completed is not None:
            item.completed = completed
        if category:
            item.category = category

    def get_items_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.items, f)

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.items = pickle.load(f)


class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo App")

        self.list = TodoList()

        self.load_list()

        self.todo_var = tk.StringVar()
        self.todo_entry = tk.Entry(self.master, textvariable=self.todo_var)
        self.todo_entry.pack()

        self.add_button = tk.Button(self.master, text="Add", command=self.add_item)
        self.add_button.pack()

        self.category_var = tk.StringVar()
        self.category_entry = tk.Entry(self.master, textvariable=self.category_var)
        self.category_entry.pack()

        self.category_button = tk.Button(self.master, text="Filter", command=self.filter_items)
        self.category_button.pack()

        self.show_all_button = tk.Button(self.master, text="Show All", command=self.show_all_items)
        self.show_all_button.pack()

        self.todo_list = tk.Listbox(self.master)
        self.todo_list.pack()

        self.update_listbox()

        self.todo_list.bind("<<ListboxSelect>>", self.select_item)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.master, textvariable=self.task_var)
        self.task_entry.pack()

        self.mark_complete_button = tk.Button(self.master, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack()

        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_item)
        self.delete_button.pack()

        self.save_button = tk.Button(self.master, text="Save List", command=self.save_list)
        self.save_button.pack()

        self.master.protocol("WM_DELETE_WINDOW", self.exit)

    def load_list(self):
        self.list.load("todo_list.pkl")

    def update_listbox(self, category=None):
        self.todo_list.delete(0, tk.END)
        if category:
            items =self.list.get_items_by_category(category)
        else:
            items = self.list.items
        for item in items:
            status = "[x]" if item.completed else "[ ]"
            self.todo_list.insert(tk.END, f"{status} {item.task}")

    def add_item(self):
        task = self.todo_var.get().strip()
        if task:
            item = TodoItem(task)
            self.list.add_item(item)
            self.update_listbox()
            self.todo_var.set("")

    def filter_items(self):
            category = self.category_var.get().strip()
            self.update_listbox(category)

    def show_all_items(self):
            self.update_listbox()

    def select_item(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            item = self.list.items[index]
            self.task_var.set(item.task)

    def mark_complete(self):
        selection = self.todo_list.curselection()
        if selection:
            index = selection[0]
            item = self.list.items[index]
            self.list.mark_complete(item)
            self.update_listbox()

    def delete_item(self):
        selection = self.todo_list.curselection()
        if selection:
            index = selection[0]
            item = self.list.items[index]
            self.list.remove_item(item)
            self.update_listbox()

    def save_list(self):
        self.list.save("todo_list.pkl")

    def exit(self):
        self.save_list()
        self.master.destroy()


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
