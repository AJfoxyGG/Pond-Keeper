import json
import tkinter as tk
from pathlib import Path

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teich App")
        self.root.geometry("400x700")
        self.root.configure(bg="#F4F7EF")
        self.todo_file = Path(__file__).with_name("todos.json")

        self.colors = {
            "background": "#F4F7EF",
            "card": "#FFFFFF",
            "primary": "#5A8F2C",
            "primary_dark": "#3F6F1D",
            "muted": "#8A977D",
            "text": "#203018",
            "border": "#DDE8D2",
        }

        title_frame = tk.Frame(root, bg=self.colors["background"])
        title_frame.pack(fill="x", padx=22, pady=(24, 12))

        tk.Label(
            title_frame,
            text="Teich Aufgaben",
            font=("Arial", 28, "bold"),
            fg=self.colors["text"],
            bg=self.colors["background"]
        ).pack(side="left")

        tk.Label(
            title_frame,
            text="🌿",
            font=("Arial", 28),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        ).pack(side="right")

        input_frame = tk.Frame(root, bg=self.colors["background"])
        input_frame.pack(fill="x", padx=22, pady=(4, 18))

        self.todo_entry = tk.Entry(
            input_frame,
            font=("Arial", 16),
            bg="#FFFFFF",
            fg=self.colors["text"],
            insertbackground=self.colors["primary"],
            relief="flat",
            highlightthickness=2,
            highlightbackground=self.colors["border"],
            highlightcolor=self.colors["primary"]
        )
        self.todo_entry.pack(side="left", fill="x", expand=True)
        self.todo_entry.bind("<Return>", lambda _event: self.add_todo())

        tk.Button(
            input_frame,
            text="+",
            width=4,
            font=("Arial", 16, "bold"),
            bg=self.colors["primary"],
            fg="#FFFFFF",
            activebackground=self.colors["primary_dark"],
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.add_todo
        ).pack(side="left", padx=(10, 0))

        self.todo_frame = tk.Frame(root, bg=self.colors["background"])
        self.todo_frame.pack(fill="both", expand=True)

        self.todos = self.load_todos()

        self.draw_todos()

        nav = tk.Frame(root, bg="#EAF2E1")
        nav.pack(fill="x", padx=18, pady=(8, 18))

        self.create_nav_button(nav, "🌊", "Teich")
        self.create_nav_button(nav, "✓", "To-Do")
        self.create_nav_button(nav, "🌿", "Pflanzen")

    def add_todo(self):
        text = self.todo_entry.get().strip()

        if text:
            self.todos.append({
                "title": text,
                "done": False
            })

            self.todo_entry.delete(0, tk.END)
            self.save_todos()
            self.draw_todos()

    def load_todos(self):
        default_todos = [
            {"title": "Wasser nachfüllen", "done": False}
        ]

        if not self.todo_file.exists():
            return default_todos

        try:
            with self.todo_file.open("r", encoding="utf-8") as file:
                todos = json.load(file)
        except (json.JSONDecodeError, OSError):
            return default_todos

        if not isinstance(todos, list):
            return default_todos

        cleaned_todos = []
        for todo in todos:
            if not isinstance(todo, dict):
                continue

            title = str(todo.get("title", "")).strip()
            if not title or todo.get("done", False):
                continue

            cleaned_todos.append({
                "title": title,
                "done": False
            })

        return cleaned_todos

    def save_todos(self):
        open_todos = [todo for todo in self.todos if not todo.get("done", False)]

        with self.todo_file.open("w", encoding="utf-8") as file:
            json.dump(open_todos, file, ensure_ascii=False, indent=2)

    def draw_todos(self):
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        for todo in self.todos:
            row = tk.Frame(
                self.todo_frame,
                bg=self.colors["card"],
                highlightthickness=1,
                highlightbackground=self.colors["border"]
            )
            row.pack(fill="x", pady=8, padx=22)

            self.create_circle_button(row, todo).pack(side="left", padx=(14, 8), pady=14)

            tk.Label(
                row,
                text="💧",
                bg=self.colors["card"],
                fg=self.colors["primary"],
                font=("Arial", 18)
            ).pack(side="left", padx=(0, 8))

            card = tk.Label(
                row,
                text=todo["title"],
                bg=self.colors["card"],
                fg=self.colors["text"],
                font=("Arial", 16, "bold"),
                anchor="w",
                pady=16
            )
            card.pack(side="left", fill="x", expand=True, padx=(0, 14))

    def create_circle_button(self, parent, todo):
        circle = tk.Canvas(
            parent,
            width=34,
            height=34,
            bg=self.colors["card"],
            highlightthickness=0,
            cursor="hand2"
        )
        circle.create_oval(
            6,
            6,
            28,
            28,
            outline=self.colors["primary"],
            width=3,
            fill="#F8FBF4"
        )
        circle.bind("<Button-1>", lambda _event: self.toggle(todo))
        return circle

    def create_nav_button(self, parent, icon, label):
        button = tk.Button(
            parent,
            text=f"{icon}\n{label}",
            font=("Arial", 12, "bold"),
            fg=self.colors["primary_dark"],
            bg="#EAF2E1",
            activebackground="#DDECCD",
            activeforeground=self.colors["primary_dark"],
            relief="flat",
            cursor="hand2",
            width=9,
            pady=8
        )
        button.pack(side="left", expand=True, fill="x", padx=4, pady=6)

    def toggle(self, todo):
        self.todos.remove(todo)
        self.save_todos()
        self.draw_todos()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
