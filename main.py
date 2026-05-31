import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teich App")
        self.root.geometry("400x700")

        title_frame = tk.Frame(root)
        title_frame.pack(fill="x", pady=10)

        tk.Label(
            title_frame,
            text="ToDo",
            font=("Arial", 30, "bold"),
            fg="#5A8F2C"
        ).pack(side="left", padx=20)

        tk.Label(
            title_frame,
            text="✓",
            font=("Arial", 30),
            fg="#5A8F2C"
        ).pack(side="right", padx=20)

        self.todo_frame = tk.Frame(root)
        self.todo_frame.pack(fill="both", expand=True)

        self.todos = [
            {"title": "Wasser nachfüllen", "done": False},
            {"title": "Rose einsetzen", "done": True}
        ]

        self.draw_todos()

        nav = tk.Frame(root)
        nav.pack(fill="x", pady=15)

        tk.Button(nav, text="🌊", width=8).pack(side="left", padx=10)
        tk.Button(nav, text="✓", width=8).pack(side="left", padx=10)
        tk.Button(nav, text="🌿", width=8).pack(side="left", padx=10)

    def draw_todos(self):
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        for todo in self.todos:
            row = tk.Frame(self.todo_frame)
            row.pack(fill="x", pady=10, padx=15)

            var = tk.BooleanVar(value=todo["done"])

            cb = tk.Checkbutton(
                row,
                variable=var,
                command=lambda t=todo, v=var: self.toggle(t, v)
            )
            cb.pack(side="left")

            card = tk.Label(
                row,
                text=todo["title"],
                bg="#EEEEEE",
                font=("Arial", 16),
                width=20,
                pady=15
            )
            card.pack(side="left", padx=10)

    def toggle(self, todo, var):
        todo["done"] = var.get()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()