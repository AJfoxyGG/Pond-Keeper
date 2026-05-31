import tkinter as tk

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

        input_frame = tk.Frame(root)
        input_frame.pack(fill="x", padx=15, pady=10)

        self.todo_entry = tk.Entry(input_frame, font=("Arial", 16))
        self.todo_entry.pack(side="left", fill="x", expand=True)
        self.todo_entry.bind("<Return>", lambda _event: self.add_todo())

        tk.Button(
            input_frame,
            text="+",
            width=4,
            font=("Arial", 16, "bold"),
            command=self.add_todo
        ).pack(side="left", padx=(10, 0))

        self.todo_frame = tk.Frame(root)
        self.todo_frame.pack(fill="both", expand=True)

        self.todos = [
            {"title": "Wasser nachfüllen", "done": False},
            {"title": "Rose einsetzen", "done": True}
        ]

        self.draw_todos()

        nav = tk.Frame(root)
        nav.pack(fill="x", pady=15)

        tk.Button(nav, text="🌊 Teich", width=8).pack(side="left", padx=10)
        tk.Button(nav, text="✓ To-Do", width=8).pack(side="left", padx=10)
        tk.Button(nav, text="🌿 Pflanzen", width=8).pack(side="left", padx=10)

    def add_todo(self):
        text = self.todo_entry.get().strip()

        if text:
            self.todos.append({
                "title": text,
                "done": False
            })

            self.todo_entry.delete(0, tk.END)
            self.draw_todos()

    def draw_todos(self):
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        for todo in self.todos:
            if todo["done"]:
                continue

            row = tk.Frame(self.todo_frame)
            row.pack(fill="x", pady=10, padx=15)

            var = tk.BooleanVar(value=todo["done"])

            cb = tk.Checkbutton(
                row,
                variable=var,
                font=("Arial", 28),
                width=2,
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
        self.draw_todos()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
